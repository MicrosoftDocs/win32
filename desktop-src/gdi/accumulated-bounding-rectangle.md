---
Description: 'The accumulated bounding rectangle is the smallest rectangle enclosing the portion of a window or client area affected by recent drawing operations.'
ms.assetid: '8ae13486-a9e2-4841-ada3-c70d30450ac8'
title: Accumulated Bounding Rectangle
---

# Accumulated Bounding Rectangle

The *accumulated bounding rectangle* is the smallest rectangle enclosing the portion of a window or client area affected by recent drawing operations. An application can use this rectangle to conveniently determine the extent of changes caused by drawing operations. It is sometimes used in conjunction with [**LockWindowUpdate**](lockwindowupdate.md) to determine which portion of the client area must be redrawn after the update lock is cleared.

An application uses the [**SetBoundsRect**](setboundsrect.md) function (specifying DCB\_ENABLE) to begin accumulating the bounding rectangle. The system subsequently accumulates points for the bounding rectangle as the application uses the specified display device context. The application can retrieve the current bounding rectangle at any time by using the [**GetBoundsRect**](getboundsrect.md) function. The application stops the accumulation by calling **SetBoundsRect** again, specifying the DCB\_DISABLE value.

 

 



