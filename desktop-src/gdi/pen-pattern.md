---
description: The pattern attribute specifies the pattern of a geometric pen.
ms.assetid: 5a330416-3b83-4f0f-825c-80e47903966e
title: Pen Pattern
ms.topic: article
ms.date: 05/31/2018
---

# Pen Pattern

The pattern attribute specifies the pattern of a geometric pen.

The following illustration shows lines drawn with different geometric pens. Each pen was created using a different pattern attribute.

![illustration showing four lines, each filled with a different pen](images/cspen-02.png)

The first line in the previous illustration is drawn using one of the six available hatch patterns; for more information about hatch patterns, see [Pen Hatch](pen-hatch.md). The next line is drawn using the hollow pattern, identical to the null pattern. The third line is drawn using a custom pattern created from an 8-by-8-pixel bitmap. (For more information about bitmaps and their creation, see [Bitmaps](bitmaps.md).) The last line is drawn using a solid pattern. Creating a brush and passing its handle to the [**ExtCreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-extcreatepen) function creates a pattern.

 

 



