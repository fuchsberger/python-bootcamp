# Automated Message Activity

## Instructions
You work at a company that offers subscriptions for weather enthusiasts, and you have been tasked with sending out a coupon code to each of your members for the yearly sale. You decide to automate the work using Python.

Create a dictionary that stores the information for one of your members. Then, use that dictionary to create a personalized message for them with a discount code. For each member, you should include:
  1. the member's name
  2. the year they joined
  3. the US state they live in
  4. a list of their subscriptions. Here are the subscriptions your company offers (the member may have any/all of these, it's up to you):
     - *Daily weather emails*
     - *Umbrella of the month club*
     - *Snow birds magazine*
     - *The Raining Cats and Dogs Podcast*

Write code that produces a personalized message for this member. The final message should read:

> Hello [name],
>
> Thank you for being a valued member for the last [years of membership] years. We are offering you an exclusive discount on [first subscription in their list].

## Additional Activities
To keep practicing, try these additional exercises:

1. Create a list of several dictionaries containing client information, and loop through them to print out a personalized message for each client.
1. Add additional conditionals to give different discount codes depending on how long they have been a member. The greeting would read:
   - Members who joined in the last year:
      > Hello [name],
      >
      > Welcome to our weather subscription service! We are offering you an exclusive discount on [first subscription in their list].
   - Members who have been a member for more than one year:
      > Hello [name],
      >
      > Thank you for being a valued member for the last [years of membership] years. We are offering you an exclusive discount on [first subscription in their list].
   - Members who have been a member for more than one year and have more than one subscription:
      > Hello [name],
      >
      > Thank you for being a valued member for the last [years of membership] years. We are offering you an exclusive discount on both [first subscription in their list] and [last subscription in their list].
   - Any member with no subscriptions:
      > Hello [name],
      >
      > Thank you for being a valued member for the last [years of membership] years. Would you like to sign up for a subscription?
