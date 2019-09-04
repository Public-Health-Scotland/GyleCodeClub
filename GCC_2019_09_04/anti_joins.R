# Anti-join
source("dummy_data.R")
library(magick)

 # For filtering a data set by another one
magick::image_read("animated-anti-join.gif")

 # Sort of the opposite of semi-join
magick::image_read("animated-semi-join.gif")

 # Filter data to exclude people with death data
dummy_smr01 %>% glimpse()
dummy_deaths %>% glimpse()

anti_join(dummy_smr01, dummy_deaths) %>% glimpse()

 #
inner_a %>% glimpse()
ICD_10s <- tibble(exclude_icd10 = sample(inner_a$x6_icd10, 15))

anti_join(inner_a, ICD_10s, by = c("x6_icd10" = "exclude_icd10"))

