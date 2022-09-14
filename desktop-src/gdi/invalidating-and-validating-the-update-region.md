---
description: An application invalidates a portion of a window and sets the update region by using the InvalidateRect or InvalidateRgn function.
ms.assetid: ec8abb77-47bc-4198-9daf-f2ccb0864ccc
title: Invalidating and Validating the Update Region
ms.topic: article
ms.date: 05/31/2018
---

# Invalidating and Validating the Update Region

An application invalidates a portion of a window and sets the update region by using the [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect) or [**InvalidateRgn**](/windows/desktop/api/Winuser/nf-winuser-invalidatergn) function. These functions add the specified rectangle or region (in client coordinates) to the update region, combining the rectangle or region with anything the system or the application may have previously added to the update region.

The [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect) and [**InvalidateRgn**](/windows/desktop/api/Winuser/nf-winuser-invalidatergn) functions do not generate [**WM\_PAINT**](wm-paint.md) messages. Instead, the system accumulates the changes made by these functions and its own changes while a window processes other messages in its message queue. By accumulating changes, a window processes all changes at once instead of updating bits and pieces one step at a time.

The [**ValidateRect**](/windows/desktop/api/Winuser/nf-winuser-validaterect) and [**ValidateRgn**](/windows/desktop/api/Winuser/nf-winuser-validatergn) functions validate a portion of the window by removing a specified rectangle or region from the update region. These functions are typically used when the window has updated a specific part of the screen in the update region before receiving the [**WM\_PAINT**](wm-paint.md) message.

 

 



