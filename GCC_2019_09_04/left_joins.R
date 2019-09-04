# Left Join
source("dummy_data.R")
library(magick)

# https://twitter.com/grrrck/status/1029567123029467136

?dplyr::left_join

magick::image_read("animated-left-join.gif")

data1 <- tibble(
  id = c(1, 2, 3),
  data = c("x1", "x2", "x3")
)

data2 <- tibble(
  id = c(1, 1, 2, 6),
  data2 = c("y11", "y12", "y21", "y61")
)

# Left join is the simplest join

# dplyr guesses what to join by
left_join(data1, data2)

# or you can specify
left_join(data1, data2, by = "id")

# Different to SPSS - data doesn't need to be sorted.
left_join(data1, data2 %>% arrange(desc(data2)))

# You get all data from x (data1) and then any from y (data2) which match
# If there are duplicates in x or y it will create a new row for each

left_join(data2, data2, by = "id")

### Some real (fake) examples
dummy_smr01 %>% glimpse()
dummy_deaths %>% glimpse()

# Join death date onto activity

left_join(dummy_smr01, dummy_deaths, by = "link_no")

# right_join(x, y) is the same as left_join(y, x)
# might make sense when chaining commands with pipe

magick::image_read("animated-right-join.gif")

# Filter some data first then join it on the 'main' dataset
test_right <- dummy_deaths %>%
  filter(location_of_death == "Home") %>%
  right_join(dummy_smr01)
test_right

# Exactly the same as 'nesting' the filtering inside the left_join
# Personal preference on which is easiest to read!
test_left <- left_join(dummy_smr01, dummy_deaths %>% filter(location_of_death == "Home"))
test_left

# Produces the same data
all_equal(test_right, test_left, ignore_row_order = FALSE)


## Examples with more variables
full_a %>% glimpse()
full_b %>% glimpse()

# All variables are the same so it will attempt match using everything
left_join(full_a, full_b) %>% glimpse() # End up with just the 'left' (full_a)

# No CHIs match... brings all other variables
left_join(full_a, full_b, by = "x1_fake_chi") %>% View()


inner_a %>% glimpse()
inner_b %>% glimpse()

# Datasets with differently named variables
left_join(inner_a, inner_b, by = c("x1_fake_chi" = "fake_chi")) %>% glimpse()
