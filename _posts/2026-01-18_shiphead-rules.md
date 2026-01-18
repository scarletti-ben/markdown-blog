---
title: "Shiphead Rules"
date: "2026-01-18"
categories: [
  miscellaneous
]
tags: [
  card games, playing cards, shiphead, shithead
]
---

# Shiphead Rules

## Setup
- The game is played with a 52-card deck, without jokers
- Deal 3 cards to each player, face-down on the table
- Deal 3 cards to each player, face-up on the table
    - One card on top of each of the face-down cards
- Deal 5 cards to each player's hand
    - They can look at these cards and should keep them hidden from the opponents during the game
- Place the rest of the deck off to the side, players will need to draw cards from this during the game

## Starting the Game
- Before the game starts, each player chooses their face-up cards as any combination of three cards from their hand and current face-up cards
    - Each player makes this decision at the same time and the game starts when they are all finished
- The player with a 3 in hand can start the game, if no one has a 3 start with a 4 and so on
    - If multiple players are tied for lowest card then it's essentially a free-for-all
    - Going first is not much of an advantage, you can alternate who goes first if that is easier

## During Your Turn
- You can play any number of a single rank of card, provided that rank is valid
    - You play this card face-up on the pile in the center of the table
    - You do not need to play *all* the cards you have of a given rank, you can play some of them and keep the rest
- If you cannot play, then you must pick up the pile and end your turn
- You can also pick up the pile even if it was possible to play

## Ending Your Turn
- If you played cards from your hand during your turn and there are cards left in the deck, then you must attempt to re-fill your hand to 5 cards
- Play moves clockwise to the next player

## How to Play
The aim of the game is to run out of cards. You do this by playing all of the cards in your hand, each of your three face-up cards, and finally each of your three face-down cards

Before we get into special rules, the general principle is that you want to play card with an equal or higher value than the card on the centre pile. For example, if there is a 5 in the centre you could play your own 5, or a card higher than 5, but you would not be able to play a 4 as it has a lower value. As stated in a previous section you can play any number of cards of a single valid rank, so you could play three 5s or four 6s for instance, but not a combination of 5s *and* 6s together. Multiple cards of the same rank are not "harder to beat", and you don't need to match or beat the quantity of cards played, only the rank.

You must always play the cards from your hand first. This means that if there are cards in your hand you cannot play from your face-up cards or face-down cards. If you have no cards in your hand, and there are no cards in the deck to refill your hand, then you can play from your face-up cards. If there are no cards in your hand, and there are no cards in the deck, and you have no face-up cards, then you can play from your face-down cards.

You cannot combine the cards from your hand with your face-up cards. This means that if the last card in your hand is a 5, and there are no cards in the deck, and you have a 5 on your face-up cards, you cannot play both 5s on the same turn.

If you *were* playing from your face-up or face-down cards but have since picked up from the pile, you must play those cards from your hand before you can go back to playing from your face-up or face-down cards.

## Special Cards
- 2s play on almost every card, every card can play on a 2, and they effectively reset the pile
- 7s play on almost every card, they are invisible, and the value of the pile is the same as the first non-7 card from the top of the pile, known as "invisible sevens"
- 8s play as the value 8, they make the next player wait if they can't also play an eight, known as "eight or wait"
- 9s play as the value 9, they require the next player to play a card that is a lower value than a 9, known as "nine or lower"
- 10s play on almost every card, they burn the pile, removing the cards from the game, and the player takes another turn

## Niche Situations
- 7 on an empty table
- four in a row with 7s

## Card Reference Guide
The `[ ]` and `< >` symbols are symbols to denote different states for cards on top of the pile. `[ ]` denotes that the default state applies, and `< >` suggests a "deactivated" state for the card. Some examples are listed below
- An `[8]` is a "normal" `8` that has just been played, and requires the player to follow the "eight-or-wait" rule, whereas an `<8>` has already been "waited" and the "eight-or-wait" rule no longer applies to it
- A `[9]` is a "normal" `9` that has just been played, and requires the player to follow the "nine-or-lower" rule, whereas a `<9>` has had a `7` played on top and the "nine-or-lower" rule no longer applies to it

```text
# What Can be Played on a...
    [2]   => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [3]   => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [4]   => 2, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [5]   => 2, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [6]   => 2, 6, 7, 8, 9, 10, J, Q, K, A
    [7]   => Look at the number on the pile before the 7
    [8]   => 8
    <8>   => 2, 7, 8, 9, 10, J, Q, K, A
    [9]   => 2, 3, 4, 5, 6, 7, 8, 9
    <9>   => 2, 7, 9, 10, J, Q, K, A
    [10]  => Clears the pile, should never be face up on the pile
    [J]   => 2, 7, 10, J, Q, K, A
    [Q]   => 2, 7, 10, Q, K, A
    [K]   => 2, 7, 10, K, A
    [A]   => 2, 7, 10, A

# What Can it Play On?
    2   => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
    3   => 2, 3, 9
    4   => 2, 3, 4, 9
    5   => 2, 3, 4, 5, 9
    6   => 2, 3, 4, 5, 6, 9
    7   => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
    8   => 2, 3, 4, 5, 6, 8, <8>, 9
    9   => 2, 3, 4, 5, 6, <8>, 9, <9>
    10  => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
    J   => 2, 3, 4, 5, 6, <8>, <9>, J
    Q   => 2, 3, 4, 5, 6, <8>, <9>, J, Q
    K   => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K
    A   => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
```
[card reference guide](#card-reference-guide)

https://en.wikipedia.org/wiki/Shithead_%28card_game%29

![shiphead](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Hand_in_Shithead.jpg/330px-Hand_in_Shithead.jpg)

## Recap
On your turn you can decide to play any number of a single rank of card that is playable, see card reference guide
If you cannot play, and there is not a special rule in play such as "eight-or-wait", then you must pick up the central pile and end your turn
You may also decide to pick up the center pile voluntarily, which you may wish to do for tactical reasons. This assumes that there are cards to pickup and that there is not a special rule in play such as "eight-or-wait"
If you played cards from your hand and there is still a deck left to pick up from, then you must re-fill your hand back to 5 cards
Once you have finished your turn, the game moves onto the next player
If, on your turn, you complete a "four-in-a-row", where there are four of a single card rank in a row on top of the pile, the pile is burned and you take another turn
If, on your turn, you play a 10, the pile is burned and you take another turn
If, at the start of your turn, there is an 7 on top of the pile you must follow the rule "invisible-sevens"
If, at the start of your turn, there is an 8 on top of the pile you must follow the rule "eight-or-wait"
If the 8 has already been "waited" then the "eight-or-wait" rule no longer applies
If, at the start of your turn, there is an 9 on top of the pile you must follow the rule "nine-or-lower"
If the 9 has had a 7 played on top of it then the "nine-or-lower" rule no longer applies
Once you run out of cards in hand you play from your cards in your "shown" pile
If you pick up cards they still go to hand, and you will need to empty your hand again to use "shown" cards
You cannot combine the last cards in your hand with cards within your "shown" pile eg. a 2 in hand and 2 from "shown"
Once you run out of cards in your hand and "shown" pile you can play from your "hidden" pile
You will play exactly one card from your "hidden" pile on your turn
You play the card entirely blind, if the card was not playable then you pick up the central pile and end your turn

## Variants
Stacking - When rearranging cards before play begins, players may stack cards of the same rank on top of each other on the upcard piles and replenish the hand from stock; this may be done more than once if more cards can be stacked