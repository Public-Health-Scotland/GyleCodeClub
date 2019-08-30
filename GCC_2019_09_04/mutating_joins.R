# Mutating joins
source("dummy_data.R")

# I was thinking some quick examples and discussion on how they are
# similar / different to other joins e.g. left vs. right
# Also examples of when you might use one or another

inner_join(dummy_smr01, dummy_deaths) %>% glimpse()
left_join(dummy_smr01, dummy_deaths) %>% glimpse()
right_join(dummy_smr01, dummy_deaths) %>% glimpse()
full_join(dummy_smr01, dummy_deaths) %>% glimpse()


