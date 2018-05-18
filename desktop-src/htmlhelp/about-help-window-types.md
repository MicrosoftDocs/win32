---
title: About Help Window Types
description: About Help Window Types
ms.assetid: 'DCDB5594-1742-4fd4-84F0-8B4F01AFD99F'
---

# About Help Window Types

Pop-up windows are based on an [**HH\_POPUP**](hh-popup-structure.md) structure and include the following default properties:

-   The pop-up window is positioned relative to the mouse. The calling program can override this with a specific position.
-   The width and height of the pop-up window are determined by the amount of text. The help author or the program can specify an exact width or height.
-   If there is insufficient screen real estate to display the text, the text is clipped. A pop-up window never includes a scroll bar.
-   The pop-up window is dismissed when the user clicks inside or outside the window, presses Esc, or when the pop-up window loses focus.

## Related topics

<dl> <dt>

[About Window Types](window-types.md)
</dt> </dl>

 

 




