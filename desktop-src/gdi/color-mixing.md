---
description: Color mixing lets an application create new colors by combining the pen or brush color with colors in the existing image.
ms.assetid: 4a5dff8c-f75f-41d2-8367-33d97d4fd010
title: Color Mixing
ms.topic: article
ms.date: 05/31/2018
---

# Color Mixing

Color mixing lets an application create new colors by combining the pen or brush color with colors in the existing image. The application can choose either to draw the pen or brush color as is (effectively drawing over any existing image) or to mix the color with the colors already present.

The foreground mix mode, sometimes called the binary raster operation, determines how these colors are mixed. An application can merge colors, preserving all components of both colors; mask colors, removing or moderating components that are not common; or exclusively mask colors, removing or moderating components that are common. There are several variations on these basic mixing operations.

Color mixing is subject to color approximation. If the result of color mixing is a color that the device cannot generate, the system approximates the result, using a color it can generate. If an application mixes dithered colors, the individual colors used to create the dithered color are mixed, and the results are subject to color approximation.

An application sets the foreground mix mode by using the [**SetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-setrop2) function and retrieves the current mode by using the [**GetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-getrop2) function.

Although there is a background mix mode, that mode does not control the mixing of colors. Instead, it specifies whether a background color is used when drawing styled lines, hatched brushes, and text.

 

 



