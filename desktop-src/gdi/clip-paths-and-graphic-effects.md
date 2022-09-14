---
description: An application can use clipping and paths to create special graphic effects. The following illustration shows a string of text drawn with a large Arial font.
ms.assetid: fda0d627-406c-44f9-9061-7aea3e2d7f66
title: Clip Paths and Graphic Effects
ms.topic: article
ms.date: 05/31/2018
---

# Clip Paths and Graphic Effects

An application can use clipping and paths to create special graphic effects. The following illustration shows a string of text drawn with a large Arial font.

![illustration showing black text on a white background](images/cspth-02.png)

The next illustration shows the result of selecting the text as a clip path and drawing radial lines for a circle whose center is located above and left of the string.

![illustration showing the same text, but filled with lines instead of solid black](images/cspth-03.png)

> [!Note]  
> Before graphics device interface (GDI) adds text created with a bitmapped font to a path, it converts the font to an outline or vector font.

 

An application creates a clip path by generating a path bracket and then calling the [**SelectClipPath**](/windows/desktop/api/Wingdi/nf-wingdi-selectclippath) function. After a clip path is selected into a DC, output only appears within the borders of the path.

In addition to creating special graphics effects, clip paths are also useful in applications that save images as enhanced metafiles. By using a clip path, an application is able to ensure device independence because the units used to specify a path are logical units.

 

 



