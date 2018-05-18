---
title: Cursors
description: This section discusses cursors which are small pictures whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball.
ms.assetid: '0ca8e51c-1159-47e9-ba3f-5ced0667cadb'
keywords: ["resources,cursors", "cursors,about"]
---

# Cursors

A cursor is a small picture whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball. In the remainder of this overview, the term mouse refers to any pointing device.

When the user moves the mouse, the system moves the cursor accordingly. The cursor functions enable applications to create, load, display, animate, move, confine, and destroy cursors.

### In This Section



| Name                                     | Description                                                   |
|------------------------------------------|---------------------------------------------------------------|
| [About Cursors](about-cursors.md)       | Discusses the standard cursors.<br/>                    |
| [Using Cursors](using-cursors.md)       | Discusses how to perform tasks related to cursors.<br/> |
| [Cursor Reference](cursor-reference.md) | Contains the API reference.<br/>                        |



 

### Cursor Functions



| Name                                                 | Description                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClipCursor**](clipcursor.md)                     | Confines the cursor to a rectangular area on the screen. If a subsequent cursor position (set by the [**SetCursorPos**](setcursorpos.md) function or the mouse) lies outside the rectangle, the system automatically adjusts the position to keep the cursor inside the rectangular area. <br/> |
| [**CopyCursor**](copycursor.md)                     | Copies the specified cursor. <br/>                                                                                                                                                                                                                                                               |
| [**CreateCursor**](createcursor.md)                 | Creates a cursor having the specified size, bit patterns, and hot spot. <br/>                                                                                                                                                                                                                    |
| [**DestroyCursor**](destroycursor.md)               | Destroys a cursor and frees any memory the cursor occupied. Do not use this function to destroy a shared cursor.<br/>                                                                                                                                                                            |
| [**GetClipCursor**](getclipcursor.md)               | Retrieves the screen coordinates of the rectangular area to which the cursor is confined. <br/>                                                                                                                                                                                                  |
| [**GetCursor**](getcursor.md)                       | Retrieves a handle to the current cursor. <br/>                                                                                                                                                                                                                                                  |
| [**GetCursorInfo**](getcursorinfo.md)               | Retrieves information about the global cursor.<br/>                                                                                                                                                                                                                                              |
| [**GetCursorPos**](getcursorpos.md)                 | Retrieves the cursor's position, in screen coordinates.<br/>                                                                                                                                                                                                                                     |
| [**GetPhysicalCursorPos**](getphysicalcursorpos.md) | Retrieves the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                               |
| [**LoadCursor**](loadcursor.md)                     | Loads the specified cursor resource from the executable (.EXE) file associated with an application instance.<br/>                                                                                                                                                                                |
| [**LoadCursorFromFile**](loadcursorfromfile.md)     | Creates a cursor based on data contained in a file. <br/>                                                                                                                                                                                                                                        |
| [**SetCursor**](setcursor.md)                       | Sets the cursor shape. <br/>                                                                                                                                                                                                                                                                     |
| [**SetCursorPos**](setcursorpos.md)                 | Moves the cursor to the specified screen coordinates. If the new coordinates are not within the screen rectangle set by the most recent [**ClipCursor**](clipcursor.md) function call, the system automatically adjusts the coordinates so that the cursor stays within the rectangle. <br/>    |
| [**SetPhysicalCursorPos**](setphysicalcursorpos.md) | Sets the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                                    |
| [**SetSystemCursor**](setsystemcursor.md)           | Enables an application to customize the system cursors. It replaces the contents of the system cursor specified by the *id* parameter with the contents of the cursor specified by the *hcur* parameter and then destroys *hcur*. <br/>                                                          |
| [**ShowCursor**](showcursor.md)                     | Displays or hides the cursor. <br/>                                                                                                                                                                                                                                                              |



 

### Cursor Notifications



| Name                                  | Description                                                                                                          |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**WM\_SETCURSOR**](wm-setcursor.md) | Sent to a window if the mouse causes the cursor to move within a window and mouse input is not captured. <br/> |



 

### Cursor Structures



| Name                             | Description                                    |
|----------------------------------|------------------------------------------------|
| [**CURSORINFO**](cursorinfo.md) | Contains global cursor information.<br/> |



 

 

 





