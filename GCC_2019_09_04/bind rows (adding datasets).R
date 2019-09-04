# Bind rows
source("dummy_data.R")

# Bind rows isn't really a join but is equivalent to 'add files' in SPSS
# It will stick the first dataframe on top of the second
# and match variables if possible

# This will allign the link_no column
# and then add the death data to the bottom
bind_rows(dummy_smr01, dummy_deaths)

# A more realistic example - add a summary variable to every row

# This will count the discharges per month per year
dis_per_month_year <- dummy_smr01 %>%
  mutate(
    dis_year = year(dis_date),
    dis_month = month(dis_date)
  ) %>%
  group_by(dis_year, dis_month) %>%
  summarise(n_discharges = n())

dis_per_month_year %>% glimpse()

# If we now want a summary row for each year
dis_per_year <- dis_per_month_year %>%
  group_by(dis_year) %>%
  summarise(n_discharges = n())

dis_per_year %>% glimpse()


# And to add them into a single data frame
bind_rows(
  dis_per_month_year,
  dis_per_year %>% mutate(dis_month = 0)
) %>%
  arrange(dis_year, dis_month) %>%
  View()
