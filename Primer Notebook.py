# Databricks notebook source
# MAGIC %md
# MAGIC #MARKDOWN - Tips de formato
# MAGIC # Header 1
# MAGIC ## Header 2
# MAGIC **bold text**
# MAGIC *italics text*
# MAGIC ~~strikethrough text~~
# MAGIC `monospace text`
# MAGIC ---
# MAGIC > Block quote
# MAGIC Ordered list:
# MAGIC 1. Item 1
# MAGIC 1. Item 2
# MAGIC 1. Item 3
# MAGIC Unordered list:
# MAGIC - Item a
# MAGIC - Item b
# MAGIC - Item c

# COMMAND ----------

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# COMMAND ----------

print fibonacci (10)

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
