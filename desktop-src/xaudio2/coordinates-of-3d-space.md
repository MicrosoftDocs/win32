---
description: 'The position, velocity, and orientation of sound sources and listeners in 3D space are represented by Cartesian coordinates, which are values on three axes: the x-axis, the y-axis, and the z-axis.'
ms.assetid: b6315e21-0758-e4c8-195f-4b83c7b61784
title: Coordinates of 3D Space
ms.topic: article
ms.date: 05/31/2018
---

# Coordinates of 3D Space

The position, velocity, and orientation of sound sources and listeners in 3D space are represented by Cartesian coordinates, which are values on three axes: the x-axis, the y-axis, and the z-axis.

The axes are relative to a viewpoint established by the application. Values on the x-axis increase from left to right, on the y-axis from down to up, and on the z-axis from near to far.

The **X3DAUDIO\_VECTOR** structure contains values describing position, velocity, or orientation on the three axes.

Conventionally, vectors are expressed as three values enclosed in parentheses and separated by commas, in the order (x, y, z).

For position, the values are in user-defined world units.

For velocity, the vector describes the rate of movement along each axis in world units per second.

For orientation, the values are in arbitrary units, and they are relative to one another. For example, if the base view of the 3D world is facing north toward the horizon, and the orientation of the listener is (-1, 0, 1), then the listener is facing northwest. Because the values within a vector are not in absolute units, the vector equally could be expressed as (-5, 0, 5) or (-0.25, 0, 0.25).

3D vectors work much like 2D vectors, but with an additional axis in the up-down direction. You can see how vectors work in 2D space by drawing them on a sheet of graph paper. Let the values increase from the bottom to the top of the paper, and from left to right. A line drawn from (0, 0) to (1, 1) has the same orientation, or direction, as one drawn from (0, 0) to (5, 5). However, the second line indicates a greater distance, or velocity.

## Related topics

<dl> <dt>

[Common Audio Concepts](common-audio-concepts.md)
</dt> <dt>

[X3DAudio Overview](x3daudio-overview.md)
</dt> </dl>

 

 



