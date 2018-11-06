---
title: Stencil Test
description: The stencil test conditionally discards a fragment based on the outcome of a comparison between the value in the stencil buffer and a reference value.
ms.assetid: 967be1e5-a9a2-45cc-aae7-c33cc257ade1
keywords:
- OpenGL processing pipeline,stencil test
- stencil test OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Stencil Test

The stencil test conditionally discards a fragment based on the outcome of a comparison between the value in the stencil buffer and a reference value. The [**glStencilFunc**](glstencilfunc.md) function specifies the comparison function and the reference value. Whether the fragment passes or fails the stencil test, the value in the stencil buffer is modified according to the instructions specified with [**glStencilOp**](glstencilop.md).

 

 




