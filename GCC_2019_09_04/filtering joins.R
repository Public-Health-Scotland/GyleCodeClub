# Filtering Joins (makes sense to see mutating joins first)
source("dummy_data.R")

# For filtering a data set by another one
magick::image_read("animated-anti-join.gif")

# Sort of the opposite of semi-join
magick::image_read("animated-semi-join.gif")


dummy_smr01 %>% glimpse()
dummy_deaths %>% glimpse()

# We can use anti join to keep people who are alive
# i.e. if anyone has a death record, remove them
# We are left with only the variables from the 'left'
anti_join(dummy_smr01, dummy_deaths) %>% glimpse()

# This will do the opposite and only keep people who are dead
# i.e. if anyone has a death record, keep only them
semi_join(dummy_smr01, dummy_deaths) %>% glimpse()


# semi and inner are similar
# however inner will also keep variables which are in the 'right' dataset
# it will also create new rows if there are duplicates
inner_join(dummy_smr01, dummy_deaths) %>% glimpse()
