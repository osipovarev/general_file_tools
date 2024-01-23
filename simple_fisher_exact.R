#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(tidyr))
suppressPackageStartupMessages(library(dplyr))

# Check if there is exactly one positional argument
if (length(commandArgs(trailingOnly = TRUE)) != 1) {
  cat("Please provide exactly one positional argument with four comma-separated values.\n")
  quit(status = 1)
}

# Parse the positional argument
input_values <- strsplit(commandArgs(trailingOnly = TRUE)[1], ",")[[1]]

# Check if there are four values
if (length(input_values) != 4) {
  cat("Please provide exactly four values separated by commas.\n")
  quit(status = 1)
}

# Create a 2-by-2 data frame
data <- matrix(as.numeric(input_values), nrow = 2, byrow = TRUE)
colnames(data) <- c("Group1", "Group2")
rownames(data) <- c("Category1", "Category2")

# Run Fisher exact test
result <- fisher.test(data, alternative = "two.sided", conf.int = TRUE)

# Output odds ratio, confidence interval, and p-value
cat("Odds Ratio:", result$estimate, "\n")
cat("Confidence Interval (95%):", result$conf.int, "\n")
cat("P-Value:", result$p.value, "\n")
