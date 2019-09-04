# Left Join
source("dummy_data.R")

data1 <- tibble(id = c(1,2,3),
                data = c("a", "b", "c"))
data2 <- tibble(id = c(1,1,2,6),
                data2 = c("a1", "a2", "b1", "f1"))

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

# right_join(x, y) is the same as left_join(y, x)
# might make sense when chaining commands with pipe
