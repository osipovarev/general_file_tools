#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(argparse))
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(tidyr))
suppressPackageStartupMessages(library(readr))

author <- "Ekaterina Osipova, 2024."

read_file <- function(file_path) {
  return(readLines(file_path))
}

fisher_exact_test <- function(universe, category1, group1, table) {
  # Calculate category 2 and group 2
  category2 <- setdiff(universe, category1)
  group2 <- setdiff(universe, group1)

  # Create data frame
  category1_group1 = length(intersect(intersect(universe, category1), group1))
  category1_group2 = length(intersect(intersect(universe, category1), group2))
  category2_group1 = length(intersect(intersect(universe, category2), group1))
  category2_group2 = length(intersect(intersect(universe, category2), group2))
  
  data <- data.frame(c(category1_group1, category1_group2), c(category2_group1, category2_group2))

  # Perform Fisher exact test
  result <- fisher.test(data, alternative = "two.sided")

  # Output values in the table if requested
  if (table) {
    print(data)
  }

  return(result)
}

# Define command line arguments
parser <- ArgumentParser()
parser$add_argument("-u",  "--universe", type = "character", help = "total list of elements aka universe")
parser$add_argument("-l1", "--list1",    type = "character", help = "list of elements with category 1")
parser$add_argument("-l2", "--list2",    type = "character", help = "list of elements with GROUP 1")
parser$add_argument("-t",  "--table",    action = "store_true", default = FALSE, help = "specify the flag if you also want to output the numbers in the table")
args <- parser$parse_args()

# Read sets from files
universe <- read_file(args$universe)
category1 <- read_file(args$list1)
group1 <- read_file(args$list2)



# Perform Fisher exact test
tryCatch({
  result <- fisher_exact_test(universe, category1, group1, args$table)
  p_value <- result$p.value
  conf_int <- result$conf.int
  odds_ratio <- result$estimate
}, error = function(e) {
  cat("Error:", e$message, "\n")
})


# Output results
cat("Odds ratio:", odds_ratio, "\n")
cat("CI:", conf_int, "\n")
cat("P-Value:", p_value, "\n")
