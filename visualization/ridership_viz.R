setwd("~/Desktop/BU/Tools for Data Science/MBTA/ds-wgbh-bus-equity/")
library(dplyr)
library(ggplot2)
library(tidyr)
library(forcats)

rs_19 = read.csv("./dataset-documentation/cleaned_data/MBTA_Bus_Ridership_Fall_2019.csv")
rs_22 = read.csv("./dataset-documentation/cleaned_data/MBTA_Bus_Ridership_Fall_2022.csv")


rs_19['total_boardings'] = rs_19['boardings'] * rs_19['sample_size']
rs_19['total_alightings'] = rs_19['alightings'] * rs_19['sample_size']
rs_19 <- rs_19 %>% select(-boardings, -alightings, -sample_size)
rs_22['total_boardings'] = rs_22['boardings'] * rs_22['sample_size']
rs_22['total_alightings'] = rs_22['alightings'] * rs_22['sample_size']
rs_22 <- rs_22 %>% select(-boardings, -alightings, -sample_size)

viz_rs_19 = rs_19 |>
  group_by(route_id) |>
  summarize(
    route_total_boarding = mean(total_boardings),
    route_total_alightings = mean(total_alightings),
    bus_num = n()
  ) |>
  mutate(
    difference = 
      (route_total_boarding - route_total_alightings) / route_total_boarding,
    year = 2019
  )

viz_rs_22 = rs_22 |>
  group_by(route_id) |>
  summarize(
    route_total_boarding = mean(total_boardings),
    route_total_alightings = mean(total_alightings),
    bus_num = n()
  ) |>
  mutate(
    difference = 
      (route_total_boarding - route_total_alightings) / route_total_boarding,
    year = 2022
  )

viz = rbind(viz_rs_19, viz_rs_22)
viz$year = as.factor(viz$year)

ggplot(viz, aes(route_id, route_total_boarding, color = year)) +
  geom_point()

viz_ = viz_rs_19 |> 
  select(route_id, route_total_boarding) |>
  inner_join(select(viz_rs_22, route_id, route_total_boarding), suffix = c("19", "22"), by = "route_id") |>
  mutate(
    difference = (route_total_boarding22 - route_total_boarding19),
    difference_percentage = difference / (route_total_boarding19),
  ) |>
  pivot_longer(
    cols = c("route_total_boarding19", "route_total_boarding22"), 
    names_to = "Year", 
    values_to = "total_boarding"
  ) |>
  mutate(
    Year = as.factor(ifelse(Year == "route_total_boarding19", 2019, 2022)),
    total_boarding = total_boarding
  )

ggplot(viz_, aes(difference_percentage)) +
  geom_histogram()

y_axis_title = "Average Boarding"
viz_ridership = function(df, title, subtitle, desc) {
  p = df |>
    arrange(difference) |>
    ggplot(aes(
      x = fct_reorder(route_id, difference_percentage, .desc = desc), 
      y = total_boarding)
    ) +
    geom_rect(aes(
      xmin = as.numeric(fct_reorder(route_id, difference_percentage, .desc = desc)) - 0.5,
      xmax = as.numeric(fct_reorder(route_id, difference_percentage, .desc = desc)) + 0.5,
      ymin = -Inf, ymax = Inf,
      fill = as.factor(as.numeric(fct_reorder(route_id, difference_percentage, .desc = desc)) %% 2)
    ), alpha = 0.7) +
    scale_fill_manual(values = c("white", "grey90"), guide = "none") +
    geom_point(aes(color = Year)) +
    theme_bw() +
    labs(x = "Route_id", y = y_axis_title, title = title, subtitle = subtitle) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1), 
      plot.title = element_text(hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5)
    )
  return(p)
}

su = summary(filter(viz_, difference > 0)$difference_percentage)
df = viz_ |>
  filter(difference_percentage > su[3]) 

# df = viz_ |>
#   filter(difference_percentage <= su[3], difference > 0) 

su = summary(filter(viz_, difference < 0)$difference_percentage)
df = viz_ |>
  filter(difference_percentage <= su[3])

# df = viz_ |>
#   filter(difference_percentage > su[3], difference < 0)

title = "Ridership by Bus Route 2019 & 2022 (Boarding)"
subtitle = "Increase"
p = viz_ridership(df, title, subtitle, TRUE)
p

