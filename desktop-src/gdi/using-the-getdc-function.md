---
description: You use the GetDC function to carry out drawing that must occur instantly rather than when a WM\_PAINT message is processing.
ms.assetid: 75525e26-72f5-4a58-a663-0bbdc2034759
title: Using the GetDC Function
ms.topic: article
ms.date: 05/31/2018
---

# Using the GetDC Function

You use the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function to carry out drawing that must occur instantly rather than when a [**WM\_PAINT**](wm-paint.md) message is processing. Such drawing is usually in response to an action by the user, such as making a selection or drawing with the mouse. In such cases, the user should receive instant feedback and must not be forced to stop selecting or drawing in order for the application to display the result. The following sections show how to use GetDC to draw in a window:

-   [Drawing with the Mouse](drawing-with-the-mouse.md)
-   [Drawing at Timed Intervals](drawing-at-timed-intervals.md)

 

 



