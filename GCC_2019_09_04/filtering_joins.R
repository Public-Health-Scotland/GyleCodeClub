# Filtering joins
source("dummy_data.R")

semi_join(dummy_smr01, dummy_deaths) %>% glimpse()
anti_join(dummy_smr01, dummy_deaths) %>% glimpse()

