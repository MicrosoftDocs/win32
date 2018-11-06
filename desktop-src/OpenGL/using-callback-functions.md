---
title: Using Callback Functions
description: The GLU callback functions, gluBeginPolygon, gluTessVertex, gluNextContour, and gluEndPolygon, are similar to the OpenGL polygon functions.
ms.assetid: e8277ba9-e270-4d7d-a29f-143f2f0d0324
keywords:
- OpenGL Utility (GLU),callback functions
- GLU (OpenGL Utility),callback functions
- OpenGL Utility (GLU),tessellation
- GLU (OpenGL Utility),tessellation
ms.topic: article
ms.date: 05/31/2018
---

# Using Callback Functions

The GLU callback functions, [**gluBeginPolygon**](glubeginpolygon.md), [**gluTessVertex**](glutessvertex.md), [**gluNextContour**](glunextcontour.md), and [**gluEndPolygon**](gluendpolygon.md), are similar to the OpenGL polygon functions.

They typically save the data for the triangles, triangle meshes, and triangle fans in user-defined data structures or in OpenGL display lists. To render the polygons, other code traverses the data structures or calls the display lists. Although the callback functions could call OpenGL functions to display polygons directly, this is usually not done, as tessellation can be computationally resource-intensive. It's a good idea to save the data if there is any chance that you want to display it again. The GLU tessellation functions are guaranteed never to return any new vertices, so interpolation of vertices, texture coordinates, or colors is never required.

 

 




