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
It's hard to know how best to write the rules when teaching them to new players and it is possible this guide is only understandable when you already know the gist of the game, or have played before. Hopefully it makes at least some sense to beginners!

The rules and descriptions below apply to my own personal flavour of the game "shiphead", also known by other names such as "shithead" or just "shed". You can read about the history of the game in the `Wikipedia` article [here](https://en.wikipedia.org/wiki/Shithead_%28card_game%29). The rules are slightly different, but the general premise and gameplay are mostly the same.

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

Before we get into special rules, the general principle is that you want to play card with an equal or higher value than the card on the centre pile. For example, if there is a 5 in the centre you could play a 5, or a card higher than 5. You can play any number of cards of a single valid rank, so you could play three 5s or four 6s for instance. Multiple cards of the same rank are not "harder to beat", and you don't need to match or beat the quantity of cards played, only the rank.

You must always play the cards from your hand first. This means that if there are cards in your hand you cannot play from your face-up cards or face-down cards. If you have no cards in your hand, and there are no cards in the deck to refill your hand, then you can play from your face-up cards. If there are no cards in your hand, and there are no cards in the deck, and you have no face-up cards, then you can play from your face-down cards.

## Special Rules
- **2** -> plays on almost every card, every card can play on it, and it effectively resets the pile
- **7** -> plays on almost every card, is considered invisible, and the value of the pile is the same as the first non-7 card from the top of the pile, also known as "invisible sevens"
- **8** -> plays as the value 8, requires the next player wait if they can't also play an eight, also known as "eight or wait"
- **9** -> plays as the value 9, requires the next player to play a card that is a lower value than a 9, also known as "nine or lower"
- **10** -> plays on almost every card, burns the pile, removing the cards from the game, and the player takes another turn
- **four-in-a-row** -> four cards of the same value in a row burns the pile, removing the cards from the game, the player that played the fourth takes another turn

## Card Reference Guide
The `[ ]` and `< >` denote different states for cards on top of the pile
- `[ ]` denotes that the "normal" state applies
    - `[8]` is a "normal" `8` that has just been played, and requires the player to follow the "eight-or-wait" rule
    - `[9]` is a "normal" `9` that has just been played, and requires the player to follow the "nine-or-lower" rule
- `< >` suggests an "alternate" state for the card
    - `<8>` has already been "waited" and the "eight-or-wait" rule no longer applies to it
    - `<9>` has had a `7` played on top and the "nine-or-lower" rule no longer applies to it

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
    [10]  => Burns the pile, should never be on the pile
    [J]   => 2, 7, 10, J, Q, K, A
    [Q]   => 2, 7, 10, Q, K, A
    [K]   => 2, 7, 10, K, A
    [A]   => 2, 7, 10, A
```

```text
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

## Frequently Asked Questions
- Do suits matter?
    - No
- What happens if there is a 7 on top of an otherwise empty table?
    - Treat it as if there were no cards, any card can be played
- Can I play multiple cards at once from my face-up cards?
    - Yes, you can play any number of the same valid rank, same as if playing from hand
- Can I combine cards from my hand with my face-up cards and play them at the same time?
    - No, not even if the last card in your hand is a 5, and you have a 5 in your face-up cards, you cannot play both 5s on the same turn
- Can I play multiple face-down cards at the same time?
    - No
- I was playing with my face-up cards as I had no cards in hand, but I just picked up cards, can I play face-up cards?
    - No, you must play cards from your hand before you can go back to playing from your face-up cards
- I was playing with my face-down cards as I had no cards in hand, and no face-up cards, but I just picked up cards, can I play face-down cards?
    - No, you must play cards from your hand before you can go back to playing from your face-down cards
- I played a face-down card and it was not playable on the pile, what do I do?
    - Pick up the pile, and the face-down card that you played, and put them in your hand
- There is an 8 on the pile and I have only face-down cards, do I "wait"?
    - No, you are required to play a face-down card and pickup the pile if it is not an 8
- Does a four-in-a-row only count if all four are played in one go?
    - No, a four-in-a-row can be contributed to by any number of players, and doesn't need to be one single play of a four-of-a-kind
- How does 7 work with a four-in-a-row?
    - 7s do not stop a four-in-a-row, this means that a pile of [3, 4, 7, 7, 4, 4, 7, 4] would burn as the same as four 4s directly next to each other

## Recap
- On your turn you can decide to play any number of a single rank of card that is playable, see [card reference guide](#card-reference-guide)
- If you cannot play, and there is not a special rule in play such as "eight-or-wait", then you must pick up the pile and end your turn
- If you played cards from your hand and there are cards left in the deck, then you must draw back to 5 cards
- Once you have finished your turn, the game moves onto the next player
- If, on your turn, you complete a "four-in-a-row", where there are four of a single card rank in a row on top of the pile, the pile is burned and you take another turn
- If, on your turn, you play a 10, the pile is burned and you take another turn
- If, at the start of your turn, there is an 7 on top of the pile you must follow the rule "invisible-sevens"
- If, at the start of your turn, there is an 8 on top of the pile you must follow the rule "eight-or-wait"
    - If the 8 has already been "waited" then the "eight-or-wait" rule no longer applies
- If, at the start of your turn, there is an 9 on top of the pile you must follow the rule "nine-or-lower"
    - If the 9 has had a 7 played on top of it then the "nine-or-lower" rule no longer applies
- Once you run out of cards in hand you play from your face-up pile
- Once you run out of cards in hand and face-up pile you play from your face-down pile
    - You play exactly one card from your face-down pile on your turn entirely blind, even on an 8, if the card was not playable then you pick up the pile and end your turn
- If you pick up cards they go to hand, and you will need to empty your hand to use face-up or face-down cards

## Variants
Below is a list of rules that are not currently in the game but could be added if you are looking to mix things up
- **Stacking** - Before starting the game, when picking face-up cards, players may stack cards of the same rank on top of each other and draw from the deck, continuing to stack from drawn cards