# Taxable Income

Many people misunderstand how tax brackets and taxable income works.... so we're going to create an algorithm to do it for us. The goal of this problem is to compute the amount of tax owed for any given income.

For the tax brackets we'll use for this problem, see [the marginal tax rates for 2019 for **Single Taxable Income**](https://en.wikipedia.org/wiki/Income_tax_in_the_United_States#Marginal_tax_rates_for_2019)

| Tax Rate      | Taxable Income |
| ----------- | ----------- |
| 10%      | $0 – $9,700       |
| 12%   | 	$9,701 – $39,475        |
| 22%   |	$39,476 – $84,200|
| 24%   |	$84,201 – $160,725|
| 32%   |$160,726 – $204,100|
| 35%   |$204,101 – $510,300|
| 37%   |$510,301+|

The key insight here is that an individual pays tax at a given bracket only for each dollar within that tax bracket's range. For example, someone making $10,000 (the 2nd bracket) is **not** taxed 12% on their entire income. They are taxed 10% on the first $9700 of their income (the limit of the first bracket) and then 12% on their salary that exceeds $9700.

So they would be taxed
`(9700 * .10) + (300 * .12) = 1006.0`


**Input:**

- `income` **-** the amount of taxable income you have. A `float`.

**Output**

- the amount of tax that you'd pay, rounded to the nearest cent.
- _Tip: use python's built-in_ `round()` function. This means that instead of an answer like `print( taxes )`, you should have `print( round(taxes, 2) )`. You should only used `round` once - on the final printed number.

## Examples

```
Enter your taxable income: 9800
982.0
```

```
Enter your taxable income: 9500
950.0
```

```
Enter your taxable income: 100000
18174.5
```

```
Enter your taxable income: 500000
150193.5
```

## Tips
- Depending on how you solve this, it might be useful to know about python's `min` function, which can return the smaller of two numbers. For example: `min(30, 12)` outputs `12`.
