library(tidyverse)
library(lubridate)
library(tidylog)

# Set a seed so we get the same data every time
set.seed(31459) # With this seed there are 95 / 1000 matching 'link_nos'

# Dummy SMR01 data
# Should probably have a couple more 'variables'
dummy_smr01 <- tibble(
  link_no = sample(10000:20000,
    size = 1000
  ),
  adm_date = as_date(sample(15000:18000,
    replace = TRUE,
    size = 1000
  ))
) %>%
  mutate(dis_date = adm_date + days(sample(1:365)))

# Dummy Deaths data
# Should probably have a couple more 'variables'
dummy_deaths <- tibble(
  link_no = sample(10000:20000, 1000),
  death_date = as_date(sample(15000:18000,
    replace = TRUE,
    size = 1000
  )),
  location_of_death = sample(c("Home", "Hospital", "Hospice", "Care Home"),
    replace = TRUE,
    size = 1000
  )
)

