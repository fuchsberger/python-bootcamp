def invest(interest, years, contribution):
  # Replace pass with your code
  total = 0
  for year in range(years):
    total += contribution
    total = total*(1 + interest/100)
    print(f"After Year {year+1} {total}")

# Add tests here

invest(7, 5, 4000)

# invest(0, 5, 4000)
