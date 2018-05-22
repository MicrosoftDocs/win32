---
Description: 'The dimensions of a cosmetic pen are specified in device units.'
ms.assetid: 'd4386681-3523-4872-b048-2a5cfbf7d039'
title: Cosmetic Pens
---

# Cosmetic Pens

The dimensions of a cosmetic pen are specified in device units. Therefore, lines drawn with a cosmetic pen always have a fixed width. Lines drawn with a cosmetic pen are generally drawn 3 to 10 times faster than lines drawn with a geometric pen. Cosmetic pens have three attributes: width, style, and color. For more information about these attributes, see [Pen Attributes](pen-attributes.md).

To create a cosmetic pen, use the [**CreatePen**](createpen.md), [**CreatePenIndirect**](createpenindirect.md), or [**ExtCreatePen**](extcreatepen.md) function. To retrieve one of the three stock cosmetic pens managed by the system, use the [**GetStockObject**](getstockobject.md) function.

After you create a pen (or obtain a handle to one of the stock pens), select the pen into the application's device context (DC) using the [**SelectObject**](selectobject.md) function. From this point on, the application uses this pen for any line-drawing operations in its client area.

 

 



