---
Description: The accumulated bounding rectangle is the smallest rectangle enclosing the portion of a window or client area affected by recent drawing operations.
ms.assetid: 8ae13486-a9e2-4841-ada3-c70d30450ac8
title: Accumulated Bounding Rectangle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accumulated Bounding Rectangle

The *accumulated bounding rectangle* is the smallest rectangle enclosing the portion of a window or client area affected by recent drawing operations. An application can use this rectangle to conveniently determine the extent of changes caused by drawing operations. It is sometimes used in conjunction with [**LockWindowUpdate**](/windows/win32/Winuser/nf-winuser-lockwindowupdate?branch=master) to determine which portion of the client area must be redrawn after the update lock is cleared.

An application uses the [**SetBoundsRect**](/windows/win32/Wingdi/nf-wingdi-setboundsrect?branch=master) function (specifying DCB\_ENABLE) to begin accumulating the bounding rectangle. The system subsequently accumulates points for the bounding rectangle as the application uses the specified display device context. The application can retrieve the current bounding rectangle at any time by using the [**GetBoundsRect**](/windows/win32/Wingdi/nf-wingdi-getboundsrect?branch=master) function. The application stops the accumulation by calling **SetBoundsRect** again, specifying the DCB\_DISABLE value.

 

 



