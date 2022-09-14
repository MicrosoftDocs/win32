---
title: Generating Texture Coordinates
description: Rather than explicitly supplying texture coordinates, you can have OpenGL generate them as a function of other vertex data using glTexGen\ .
ms.assetid: 5c9ce163-6107-46a3-8c8d-fc87d2f8cf9a
keywords:
- OpenGL processing pipeline,texture coordinates
- texture coordinates OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Generating Texture Coordinates

Rather than explicitly supplying texture coordinates, you can have OpenGL generate them as a function of other vertex data using [glTexGen\*](gltexgen-functions.md). After the texture coordinates have been specified or generated, they are transformed by the texture matrix. This matrix is controlled with the same functions that are used for matrix transformations (see [Matrix Transformations](matrix-transformations.md)).

 

 




