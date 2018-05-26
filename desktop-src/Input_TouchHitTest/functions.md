---
title: Functions
description: The topics in this section provide the reference specifications for Touch Hit Testing functions.
ms.assetid: C7275A12-4F76-485D-896F-3CCB8CE92F8E
keywords:
- user interaction
- input
- pointer
- touch
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

The topics in this section provide the reference specifications for [Touch Hit Testing](https://msdn.microsoft.com/library/windows/desktop/hh437255) functions.

## In this section



| Topic                                                                                               | Description                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EvaluateProximityToPolygon**](/windows/win32/winuser/nf-winuser-evaluateproximitytopolygon?branch=master)<br/>                         | Returns the score of a polygon as the probable touch target (compared to all other polygons that intersect the touch contact area) and an adjusted touch point within the polygon. <br/>       |
| [**EvaluateProximityToRect**](/windows/win32/winuser/nf-winuser-evaluateproximitytorect?branch=master)<br/>                               | Returns the score of a rectangle as the probable touch target, compared to all other rectangles that intersect the touch contact area, and an adjusted touch point within the rectangle. <br/> |
| [**PackTouchHitTestingProximityEvaluation**](/windows/win32/winuser/nf-winuser-packtouchhittestingproximityevaluation?branch=master)<br/> | Returns the proximity evaluation score and the adjusted touch-point coordinates as a packed value for the [**WM\_TOUCHHITTESTING**](https://msdn.microsoft.com/library/windows/desktop/hh454931) callback. <br/>               |
| [**RegisterTouchHitTestingWindow**](/windows/win32/winuser/nf-winuser-registertouchhittestingwindow?branch=master)<br/>                   | Registers a window to process the [**WM\_TOUCHHITTESTING**](https://msdn.microsoft.com/library/windows/desktop/hh454931) notification<br/>                                                                                     |



 

## Related topics

<dl> <dt>

[Touch Hit Testing Reference](reference.md)
</dt> </dl>

 

 





