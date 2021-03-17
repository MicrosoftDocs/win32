---
title: Touch Hit Testing functions
description: The topics in this section provide the reference specifications for Touch Hit Testing functions.
ms.assetid: C7275A12-4F76-485D-896F-3CCB8CE92F8E
keywords:
- user interaction
- input
- pointer
- touch
ms.topic: article
ms.date: 02/07/2020
---

# Touch Hit Testing functions

The topics in this section provide the reference specifications for [Touch Hit Testing functions](functions.md).

## In this section

| Topic | Description |
| --- | --- |
| [**EvaluateProximityToPolygon**](/windows/win32/api/winuser/nf-winuser-evaluateproximitytopolygon)<br/> | Returns the score of a polygon as the probable touch target (compared to all other polygons that intersect the touch contact area) and an adjusted touch point within the polygon. <br/> |
| [**EvaluateProximityToRect**](/windows/win32/api/winuser/nf-winuser-evaluateproximitytorect)<br/> | Returns the score of a rectangle as the probable touch target, compared to all other rectangles that intersect the touch contact area, and an adjusted touch point within the rectangle. <br/> |
| [**PackTouchHitTestingProximityEvaluation**](/windows/win32/api/winuser/nf-winuser-packtouchhittestingproximityevaluation)<br/> | Returns the proximity evaluation score and the adjusted touch-point coordinates as a packed value for the [WM_TOUCHHITTESTING message](../inputmsg/wm-touchhittesting.md) callback. <br/> |
| [**RegisterTouchHitTestingWindow**](/windows/win32/api/winuser/nf-winuser-registertouchhittestingwindow)<br/> | Registers a window to process the [WM_TOUCHHITTESTING](../inputmsg/wm-touchhittesting.md) notification<br/> |

## Related topics

[Touch Hit Testing Reference](touchhittest-reference.md)
