---
title: "Rubik's Cube (3x3) Algorithms"
date: "2026-02-06"
categories: [
  miscellaneous
]
tags: [
  rubik's cube, rubiks cube, cubing, 3x3 cube, cube algorithms, beginner's method, cheat sheet
]
---

# Overview
I learned to solve the Rubik's Cube a while ago using the "beginners method". When learning I had to learn the algorithms needed for the different stages, but after a while it became muscle memory and I forgot the algorithms. This was all well and good until I took a long break and came back, only to realise that my muscles had forgotten some of the steps. 

When I went back to find the algorithms for the "beginners method" I found that there are actually quite a few different ones. There are variations in annotation style, as well as completely different ways to hold and manipulate the cube. They all achieve the same result but I didn't want to learn a new style just yet so I went in search of the method I used

# Helpful Sites
The site that is most useful for me to use for these notes is [alg.cubing.net](https://alg.cubing.net/). It allows you to setup the cube in any way you wish and create an animation for different algorithms. You can either play the animation, or move through it one move at a time

# Cube Notation
All mentions of clockwise are if you were looking at them head-on, an example would be that a clockwise `B` move looks anti-clockwise if you are doing it while looking at the `F` face, but would look clockwise if looking at the `B` face head-on

A hypthen `'` signifies doing the move in reverse, or anti-clockwise. An example would be `R'` which would move the `R` face towards you. It is usually called "dash" or "prime" eg. "R-dash" or "R-prime"

A number signifies doing the move multiple times in a row, eg. `U2` would be the same as `U U`

- `L` turns the left layer clockwise, which is towards you
- `R` turns the right layer clockwise, which is away from you
- `U` turns the top layer clockwise
- `D` turns the down (bottom) layer clockwise
- `F` turns the front layer clockwise
- `B` turns the back layer clockwise

- `x` rotates the entire cube following the path of an `R` move
- `y` rotates the entire cube following the path of an `U` move
- `z` rotates the entire cube following the path of an `F` move

- `l` turns the left two layers clockwise
- `r` turns the right two layers clockwise
- `u` turns the top two layers clockwise
- `d` turns the down (bottom) two layers clockwise
- `f` turns the front two layers clockwise
- `b` turns the back two layers clockwise

- `M` turns the middle layer between `L` and `R`
- `E` turns the middle layer between `U` and `D`
- `S` turns the middle layer between `F` and `B`

You can see all the moves [here](https://alg.cubing.net/?alg=L_R_U_D_F_B%0AB-_F-_D-_U-_R-_L-%0A%0Ax_y_z%0Az-_y-_x-%0A%0Al_r_u_d_f_b%0Ab-_f-_d-_u-_r-_l-%0A%0AM_E_S%0AS-_E-_M-%0A%0AU2_R2_F2%0AF2_R2_U2&title=Cube%20Notation)

# First Layer - Making the Daisy
During the solve you want the white face on `D` and the yellow face on `U`. The daisy is when you have a yellow centre with white edge pieces, the orientation of them doesn't matter much and you shouldn't need any specific algorithms, it should be intuitive.

You can see a basic example of making the daisy [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R&alg=R_F-_L_B-_L). The example isn't an algorithm to remember, just shows general intuitive moves and what you're aiming for at the end

# First Layer - Moving the Daisy
Once you have all the white edge pieces of the daisy you can start moving them down to the white face on `D`. The easiest way is to line up an edge piece so that its non-white colour is touching its matching centre on the `F` face. Then use the algorithm `F2` to move it down to the white face. Do this same orientation and spin with each of the edge pieces until you have them all in the right place

You can see a basic example of moving the daisy [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R_R_F-_L_B-_L&alg=U2_F2_y_U2_F2_y2_F2_y-_U2_F2_x2_y_y_y_y). Again it's not really "algorithm" based, it's more done by eye

# First Layer - Solving the White Corners
If you have all the white edge pieces in the right place you can search for white corners around the cube. If you have a white corner on `D` that is in the wrong place, orient it so that it is in the bottom right corner of the `F` face and use the algorithm `R U R'`. You can also orient it so that it is in the bottom left corner of the `F` face and use the algorithm `L' U' L`. The two algorithms are also used to bring the correct corners into the right places.

If you want to bring a correct corner down on the right hand side you want to orient so that the centre colour matches the part of the corner on `F` and the white part of the piece is on `R`, the colour on `U` does not matter. If you use `R U R'` it should bring the corner into the correct place on `D`

If you want to bring a correct corner down on the left hand side you want to orient so that the centre colour matches the part of the corner on `F` and the white part of the piece is on `L`, the colour on `U` does not matter. If you use `L' U' L` it should bring the corner into the correct place on `D`

Sometimes you will have corners where the white sticker is on `U`, I usually just fix this with `R U2 R'` or `L' U2 L` to move the white corner but it should be mostly intuitive

An example of using `R U R'` to solve a corner can be seen [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R_R_F-_L_B-_L_U2_F2_y_U2_F2_y2_F2_y-_U2_F2_y_U-&alg=R_U_R-)

An example of using `L' U' L` to solve a corner can be seen [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R_R_F-_L_B-_L_U2_F2_y_U2_F2_y2_F2_y-_U2_F2_U2&alg=L-_U-_L&view=playback)

An example of using `R U R'` to reorient a corner that has white on `U` can be seen [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R_R_F-_L_B-_L_U2_F2_y_U2_F2_y2_F2_y-_U2_F2_y-&view=playback&alg=R_U2_R-)

An example of chaining algorithms to solve a corner that has white on `U` can be seen [here](https://alg.cubing.net/?setup=x2_R2_F_L_F2_R2_B_R_R_F-_L_B-_L_U2_F2_y_U2_F2_y2_F2_y-_U2_F2_y-&view=playback&alg=R_U2_R-_U-_R_U_R-). The combined algorithm is `R U2 R' U' R U R'`

# Middle Layer - Solving the Middle Layer
When solving the middle layer you are looking for middle pieces that have two non-yellow stickers, where one of the stickers is on the `U` face and touches the yellow centre. Once you find a valid piece, orient it so that one of the stickers touches its matching centre on the `F` face. You now need to note the colour of the sticker on the `U` face. If that sticker matches the centre of the `R` face use `U R U R' U' F' U' F`. If that sticker matches the centre of the `L` face use `U' L' U' L U F U F'`
- `U R U R' U' F' U' F` if top colour matches right face centre
  - This moves the piece clockwise, with one sticker on `F` and one sticker on `R`
- `U' L' U' L U F U F'` if top colour matches left face centre
  - This moves the piece ant-clockwise, with one sticker on `F` and one sticker on `L`

If you have not solved the middle layer and all middle pieces that touch `U` have a yellow sticker, then you may need to apply the algorithms above to "dislodge" a middle piece that is in the wrong place

You can see an example of the algorithms being used [here](https://alg.cubing.net/?setup=z2_F_U_R_U-_R-_F-_F_U_R_U-_R-_F-_U_R_U_R-_U-_F-_U-_F_y2__y_U_U-_L-_U-_L_U_F_U_F-_y_U_R_U_R-_U-_F-_U-_F&title=Solving%20the%20Middle%20Layer&alg=d2_U_R_U_R-_U-_F-_U-_F_y-_U-_L-_U-_L_U_F_U_F-_U2_U-_L-_U-_L_U_F_U_F-)


# Last Layer - Making the Yellow Cross
You are completely ignoring the yellow corner pieces for now and are looking for one of the situations below
- a solid line
  - align it vertically across `U` from `F` to `B`
- an L 
  - align it as a backwards L in the top left corner of `U` going from `L` to `B` via yellow centre
- a single dot in the centre
  - it doesn't matter how you align

You will apply the same algorithm to the "dot" the "line" and the "L", and may need to repeat multiple times - adjusting the alignment as you go, to get the yellow cross. The algorithm is `F U R U' R' F'`

You can see an example of the algorithm being used on the "L" in this [example](https://alg.cubing.net/?setup=z2_F_U_R_U-_R-_F-_F_U_R_U-_R-_F-&title=making%20the%20cross&alg=F_U_R_U-_R-_F-)

A text diagram of the yellow cross
```text
- Y -
Y Y Y
- Y -
```

# Last Layer - Making the Yellow Fishy
Once you have a yellow cross you are next trying to make a yellow fishy. Not everyone calls it that but I like it. It's essentially the yellow cross with a single yellow corner and looks slightly like a fish shape. The algorithm to get the yellow fishy is `R U R' U R U2 R'`, and you need to apply it when there is anything other than exactly 1 yellow corner. The orientation you need is a corner piece with yellow on `L` and the attached colour on `F`. If you end up with any number other than exactly 1 yellow corner you will need to reorient and apply the algorithm again. You can view an example [here](https://alg.cubing.net/?setup=x2_R_U2_R-_U-_R_U_R-_U-_R_U-_R-&alg=R_U_R-_U_R_U2_R-&title=CROSS%20TO%20FISHY)

A text diagram of the yellow fishy
```text
- Y -
Y Y Y
Y Y -
```

# Last Layer - Yellow Fishy to Full Yellow
With a yellow cross, and exactly one yellow corner, on the top face. Align the yellow corner in the bottom left of `U` so it is adjacent to `F` and `L`, this is the yellow fishy. When aligned, the algorithm is the same as for making the yellow fishy from the yellow cross which is `R U R' U R U2 R'` and you can see it in use in this [example](https://alg.cubing.net/?setup=z2&alg=R_U_R-_U_R_U2_R-&type=alg&title=Completing%20the%20top%20face%20with%20one%20corner&view=playback). You may need to apply the algorithm multiple times, making sure to align the fishy correctly each time

# Last Layer - Making Top Corner Pairs
If all your corners are paired you can skip this step. If you have one pair of corners align it so they are matching their centre colour and place them on the `L` side of the cube, if you have no corner pairs then alignment doesn't matter. The algorithm used here is `L' U R U' L U2 R' U R U2 R'`, and you may need to repeat it, making sure you align your new corner pairs correctly. You can see an example [here](https://alg.cubing.net/?setup=z2_y2_L-_U_R_U-_L_U2_R-_U_R_U2_R-_y2_L-_U_R_U-_L_U2_R-_U_R_U2_R-&title=3x3x3%20Corner%20Swap%20with%20no%20pairs&alg=L-_U_R_U-_L_U2_R-_U_R_U2_R-)

# Last Layer - Cycle Top Middle Pieces
Once you have all the correct corner pairs you will likely have either 1 or 0 fully correct faces on the cube (`L`, `F`, `R` or `B`). The algorithm is `F2 U' R' L F2 R L' U' F2`. This algorithm cycles the middle pieces, so if you have no correct face orientation doesn't matter, but if you have 1 then you want to keep it on `B` before performing the algorithm. The example for when you have one completed face is [here](https://alg.cubing.net/?setup=z2_y2&type=alg&alg=F2_U-_R-_L_F2_R_L-_U-_F2&title=top%20layer%20middle%20-%20%0Amoving%20piece%20in%20from%20the%20Left)

Technically, `F2 U' R' L F2 R L' U' F2` actually cycles one way and `F2 U R' L F2 R L' U F2` cycles the other but I'd say just learn one and use it multiple times

# Algorithms
- `R U R'` and `L' U' L`
  - Also known as right trigger and left trigger, `<` and `>`
- `U R U R' U' F' U' F` and `U' L' U' L U F U F'`
  - `U > U' F' U' F` and `U' < U F U F'`
- `F U R U' R' F'`
  - `F U > F'`
- `R U R' U R U2 R'`
  - `> U R U2 R'`
- `L' U R U' L U2 R' U R U2 R'`
- `F2 U' R' L F2 R L' U' F2` and `F2 U R' L F2 R L' U F2`

# Miscellaneous
- https://www.speedsolving.com/wiki/index.php?title=Layer_by_layer
- https://www.speedsolving.com/wiki/index.php?title=Category:3x3x3_beginner_methods_and_substeps
- https://www.speedsolving.com/wiki/index.php/OLL
- A full solve that I made using all of the methods I know can be found [here](https://alg.cubing.net/?title=Full%20Solve&setup=x2_y_m2_f2_R_L-_m_d_R_U2_F2_L_F_z-&alg=F-_y-_F2_y-_F2_U2_R-%0A%2F%2F_Making_the_daisy_on_the_yellow_face%0A%0Ay_F2_y_U-_y_F2_y_F2_y_U-_y_F2%0A%2F%2F_Moving_the_daisy_to_the_white_face%0A%0Ay2_L-_U2_L_U_L-_U-_L_U-_y_R_U_R-_y-_R_U2_R-_U-_R_U_R-_y-_L-_U-_L%0A%2F%2F_Solving_the_white_corners%0A%0Ay2_U_U-_L-_U-_L_U_F_U_F-_y2_U_R_U_R-_U-_F-_U-_F_y-_U-_U_R_U_R-_U-_F-_U-_F_U2_U-_L-_U-_L_U_F_U_F-%0A%2F%2F_Solving_the_middle_layer%0A%0Ay2_F_U_R_U-_R-_F-%0A%2F%2F_Making_the_yellow_cross%0A%0Ay_R_U_R-_U_R_U2_R-_y2_R_U_R-_U_R_U2_R-_y-%0A%2F%2F_Making_the_yellow_fishy%0A%0AR_U_R-_U_R_U2_R-%0A%2F%2F_Yellow_fishy_to_full_yellow%0A%0AU2_y-_L-_U_R_U-_L_U2_R-_U_R_U2_R-%0A%2F%2F_Making_top_corner_pairs%0A%0Ay-_F2_U-_R-_L_F2_R_L-_U-_F2%0A%2F%2F_Cycle_top_middle_pieces), there's quite a few cube orientation changes as I was looking around the cube for the pieces I needed. It is not meant to teach anyone how to solve a cube but shows off all the steps as a reminder to myself