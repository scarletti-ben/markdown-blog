---
title: "Rubik's Cube (3x3) Algorithms"
date: "2026-02-06"
categories: [
  miscellaneous
]
tags: [
  rubik's cube, rubiks cube, cubing, 3x3 cube, cube algorithms, beginner's method
]
---

# Overview
I learned to solve the Rubik's Cube a while ago using the "beginners method". When learning I had to learn the algorithms needed for the different stages, but after a while it became muscle memory and I forgot the algorithms. This was all well and good until I took a long break and came back, only to realise that my muscles had forgotten some of the steps. 

When I went back to find the algorithms for the "beginners method" I found that there are actually quite a few different ones. There are variations in annotation style, as well as completely different ways to hold and manipulate the cube. They all achieve the same result but I didn't want to learn a new style just yet so I went in search of the method I used

# Helpful Sites
The site that is most useful for me to use for these notes is [alg.cubing.net](https://alg.cubing.net/). It allows you to setup the cube in any way you wish and create an animation for different algorithms. You can either play the animation, or move through it one move at a time

# First Two Layers
I cannot be bothered to make notes on these right now as they haven't fallen out of my brain yet. Hopefully I will remember to make the notes before they do.

# Last Layer - Creating the Yellow Cross
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

# Last Layer - Creating the Yellow Fishy
Once you have a yellow cross you are next trying to make a yellow fishy. Not everyone calls it that but I like it. It's essentially the yellow cross with a single yellow corner and looks slightly like a fish shape. The algorithm to get the yellow fishy is `R U R' U R U2 R'`, and you need to apply it when there is anything other than exactly 1 yellow corner. The orientation you need is a corner piece with yellow on `L` and the attached colour on `F`. If you end up with any number other than exactly 1 yellow corner you will need to reorient and apply the algorithm again. You can view an example [here](https://alg.cubing.net/?setup=x2_R_U2_R-_U-_R_U_R-_U-_R_U-_R-&alg=R_U_R-_U_R_U2_R-&title=CROSS%20TO%20FISHY)

A text diagram of the yellow fishy
```text
- Y -
Y Y Y
Y Y -
```

# Last Layer - Yellow Fishy to Full Yellow
With a yellow cross, and exactly one yellow corner, on the top face. Align the yellow corner in the bottom left of `U` so it is adjacent to `F` and `L`, this is the yellow fishy. When aligned, the algorithm is the same as for creating the yellow fishy from the yellow cross which is `R U R' U R U2 R'` and you can see it in use in this [example](https://alg.cubing.net/?setup=z2&alg=R_U_R-_U_R_U2_R-&type=alg&title=Completing%20the%20top%20face%20with%20one%20corner&view=playback). You may need to apply the algorithm multiple times, making sure to align the fishy correctly each time

# Last Layer - Making Corner Pairs
If all your corners are paired you can skip this step. If you have one pair of corners align it so they are matching their centre colour and place them on the `L` side of the cube, if you have no corner pairs then alignment doesn't matter. The algorithm used here is `L' U R U' L U2 R' U R U2 R'`, and you may need to repeat it, making sure you align your new corner pairs correctly. You can see an example [here](https://alg.cubing.net/?setup=z2_y2_L-_U_R_U-_L_U2_R-_U_R_U2_R-_y2_L-_U_R_U-_L_U2_R-_U_R_U2_R-&title=3x3x3%20Corner%20Swap%20with%20no%20pairs&alg=L-_U_R_U-_L_U2_R-_U_R_U2_R-)

# Last Layer - Cycle Middle Pieces
Once you have all the correct corner pairs you will likely have either 1 or 0 fully correct faces on the cube (`L`, `F`, `R` or `B`). The algorithm is `F2 U' R' L F2 R L' U' F2`. This algorithm cycles the middle pieces, so if you have no correct face orientation doesn't matter, but if you have 1 then you want to keep it on `B` before performing the algorithm. The example for when you have one completed face is [here](https://alg.cubing.net/?setup=z2_y2&type=alg&alg=F2_U-_R-_L_F2_R_L-_U-_F2&title=top%20layer%20middle%20-%20%0Amoving%20piece%20in%20from%20the%20Left)

Technically, `F2 U' R' L F2 R L' U' F2` actually cycles one way and `F2 U R' L F2 R L' U F2` cycles the other but I'd say just learn one and use it multiple times

# Miscellaneous
- https://www.speedsolving.com/wiki/index.php?title=Layer_by_layer
- https://www.speedsolving.com/wiki/index.php?title=Category:3x3x3_beginner_methods_and_substeps
- https://www.speedsolving.com/wiki/index.php/OLL