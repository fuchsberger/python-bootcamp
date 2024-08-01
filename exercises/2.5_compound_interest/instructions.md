# Compound Interest

Early career adults rarely see the value of putting their money into retirement or investment funds. But the compounding of interest in those spaces is powerful. In this problem, we will explore how your investment depends on:
- the interest on an account,
- the number of years that you contribute, and
- the amount that you contribute annually.

Let's assume that you start with $0 after you graduate college. Create a function `invest` to determine the value of your investment given the following parameters:

- `interest` - an integer, the percentage increase in your account each year.
- `years` - an integer, the number of years that you keep the account.
- `contribution` - an integer, the dollar amount that you put into your account each year.

Your function should **return** a float **rounded to the nearest cent** representing the amount of money you will have in the account after the number of years given by `years`.

## Explaining the order of things...

Each year, the function `invest` should work in this order:
- add the yearly contribution to your account
- apply the interest

**After the last year**, round your total to the nearest cent.

So, if my yearly contribution is 4000 dollars and I invest for 5 years at 7%, the value of my account increases over time as...

```
After Year 1 4280.0
After Year 2 8859.6
After Year 3 13759.772
After Year 4 19002.95604
After Year 5 24613.1629628
Total: 24613.16
```

Compare the value of the account if you made the same contributions (4000 dollars annually for 5 years) in a 0% interest account:
```
After Year 1 4000
After Year 2 8000
After Year 3 12000
After Year 4 16000
After Year 5 20000
Total: 20000
```

**!!! The logic in your `invest` function MUST use a for loop !!!**

## How running the functions should look...

### Example 1: Invest 4000 dollars annually for five years at 7%

```bash
> invest(7, 5, 4000)
24613.16
```
### Example 2: Invest 4000 dollars annually for five years at 0%


```bash
> invest(0, 5, 4000)
20000
```

Once you have the function `invest` working, we encourage you to try different interest rates, annual contributions, and lengths of investment. Compare 0% vs 7% interest with annual contributions of $10000 for 35 years. You may be startled at how much is gained by investing early in an interest-bearing account!
