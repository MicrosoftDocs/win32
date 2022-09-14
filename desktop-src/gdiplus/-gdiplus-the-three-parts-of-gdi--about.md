---
description: 'The services of Windows GDI+ fall into the following three broad categories:'
ms.assetid: d5bef8e4-7a4c-4ac4-938a-7034ad3d743f
title: The Three Parts of GDI+
ms.topic: article
ms.date: 05/31/2018
---

# The Three Parts of GDI+

The services of Windows GDI+ fall into the following three broad categories:

-   [2-D vector graphics](#2-d-vector-graphics)
-   [Imaging](#imaging)
-   [Typography](#typography)

## 2-D vector graphics

Vector graphics involves drawing primitives (such as lines, curves, and figures) that are specified by sets of points on a coordinate system. For example, a straight line can be specified by its two endpoints, and a rectangle can be specified by a point giving the location of its upper-left corner and a pair of numbers giving its width and height. A simple path can be specified by an array of points to be connected by straight lines. A Bézier spline is a sophisticated curve specified by four control points.

GDI+ provides classes that store information about the primitives themselves, classes that store information about how the primitives are to be drawn, and classes that actually do the drawing. For example, the **Rect** class stores the location and size of a rectangle; the **Pen** class stores information about line color, line width, and line style; and the **Graphics** class has methods for drawing lines, rectangles, paths, and other figures. There are also several **Brush** classes that store information about how closed figures and paths are to be filled with colors or patterns.

## Imaging

Certain kinds of pictures are difficult or impossible to display with the techniques of vector graphics. For example, the pictures on toolbar buttons and the pictures that appear as icons would be difficult to specify as collections of lines and curves. A high-resolution digital photograph of a crowded baseball stadium would be even more difficult to create with vector techniques. Images of this type are stored as bitmaps, arrays of numbers that represent the colors of individual dots on the screen. Data structures that store information about bitmaps tend to be more complex than those required for vector graphics, so there are several classes in GDI+ devoted to this purpose. An example of such a class is **CachedBitmap**, which is used to store a bitmap in memory for fast access and display.

## Typography

Typography is concerned with the display of text in a variety of fonts, sizes, and styles. GDI+ provides an impressive amount of support for this complex task. One of the new features in GDI+ is subpixel antialiasing, which gives text rendered on an LCD screen a smoother appearance.

 

 



