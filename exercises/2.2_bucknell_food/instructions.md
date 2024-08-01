# Bucknell Food

In this problem, we're going to create a program that tells us which Bucknell food locations are open at any given time on **Monday-Friday**.

Link to Bucknell food times: https://www.bucknell.edu/about-bucknell/dining-services/dining-locations

We're going to cover 4 locations:
- **Bison Cafe:** 7:30am - 11pm
- **Bostwick:** 7am-10am, 11am-3pm, 5pm-10pm
- **Commons:** 10am - 9pm
- **Terrace:** 11am - 2pm

**Input:**

- A float that represents the time on a 24-hour clock. For example: 11:30am is `11.5`, 4pm is `16.` 11:30pm is `23.5`

**Output:**

- The names of each location (on separate lines) that are open at that time. If a location opens at 12, you can order immediately at 12. But if a location closes at 12, you must order **BEFORE** 12 (you cannot order exactly at 12).
- _NOTE: Because of the way our tests evaluate your answers, the food locations **must** be listed in alphabetical order_

## Examples
```
What time is it? (0 - 24): 7
Bostwick
```

```
What time is it? (0 - 24): 10.5
Bison Cafe
Commons
```

```
What time is it? (0 - 24): 12
Bison Cafe
Bostwick
Commons
Terrace
```

```
What time is it? (0 - 24): 21
Bison Cafe
Bostwick
```
