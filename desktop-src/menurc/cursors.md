---
title: Cursors
description: This section discusses cursors which are small pictures whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\resources\cursors.htm'
keywords:
- resources,cursors
- cursors,about
ms.topic: article
ms.date: 05/31/2018
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
| [**ClipCursor**](/windows/desktop/api/Winuser/nf-winuser-clipcursor)                     | Confines the cursor to a rectangular area on the screen. If a subsequent cursor position (set by the [**SetCursorPos**](/windows/desktop/api/Winuser/nf-winuser-setcursorpos) function or the mouse) lies outside the rectangle, the system automatically adjusts the position to keep the cursor inside the rectangular area. <br/> |
| [**CopyCursor**](/windows/desktop/api/Winuser/nf-winuser-copycursor)                     | Copies the specified cursor. <br/>                                                                                                                                                                                                                                                               |
| [**CreateCursor**](/windows/desktop/api/Winuser/nf-winuser-createcursor)                 | Creates a cursor having the specified size, bit patterns, and hot spot. <br/>                                                                                                                                                                                                                    |
| [**DestroyCursor**](/windows/desktop/api/Winuser/nf-winuser-destroycursor)               | Destroys a cursor and frees any memory the cursor occupied. Do not use this function to destroy a shared cursor.<br/>                                                                                                                                                                            |
| [**GetClipCursor**](/windows/desktop/api/Winuser/nf-winuser-getclipcursor)               | Retrieves the screen coordinates of the rectangular area to which the cursor is confined. <br/>                                                                                                                                                                                                  |
| [**GetCursor**](/windows/desktop/api/Winuser/nf-winuser-getcursor)                       | Retrieves a handle to the current cursor. <br/>                                                                                                                                                                                                                                                  |
| [**GetCursorInfo**](/windows/desktop/api/Winuser/nf-winuser-getcursorinfo)               | Retrieves information about the global cursor.<br/>                                                                                                                                                                                                                                              |
| [**GetCursorPos**](/windows/desktop/api/Winuser/nf-winuser-getcursorpos)                 | Retrieves the cursor's position, in screen coordinates.<br/>                                                                                                                                                                                                                                     |
| [**GetPhysicalCursorPos**](/windows/desktop/api/Winuser/nf-winuser-getphysicalcursorpos) | Retrieves the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                               |
| [**LoadCursor**](/windows/desktop/api/Winuser/nf-winuser-loadcursora)                     | Loads the specified cursor resource from the executable (.EXE) file associated with an application instance.<br/>                                                                                                                                                                                |
| [**LoadCursorFromFile**](/windows/desktop/api/Winuser/nf-winuser-loadcursorfromfilea)     | Creates a cursor based on data contained in a file. <br/>                                                                                                                                                                                                                                        |
| [**SetCursor**](/windows/desktop/api/Winuser/nf-winuser-setcursor)                       | Sets the cursor shape. <br/>                                                                                                                                                                                                                                                                     |
| [**SetCursorPos**](/windows/desktop/api/Winuser/nf-winuser-setcursorpos)                 | Moves the cursor to the specified screen coordinates. If the new coordinates are not within the screen rectangle set by the most recent [**ClipCursor**](/windows/desktop/api/Winuser/nf-winuser-clipcursor) function call, the system automatically adjusts the coordinates so that the cursor stays within the rectangle. <br/>    |
| [**SetPhysicalCursorPos**](/windows/desktop/api/Winuser/nf-winuser-setphysicalcursorpos) | Sets the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                                    |
| [**SetSystemCursor**](/windows/desktop/api/Winuser/nf-winuser-setsystemcursor)           | Enables an application to customize the system cursors. It replaces the contents of the system cursor specified by the *id* parameter with the contents of the cursor specified by the *hcur* parameter and then destroys *hcur*. <br/>                                                          |
| [**ShowCursor**](/windows/desktop/api/Winuser/nf-winuser-showcursor)                     | Displays or hides the cursor. <br/>                                                                                                                                                                                                                                                              |



 

### Cursor Notifications



| Name                                  | Description                                                                                                          |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**WM\_SETCURSOR**](wm-setcursor.md) | Sent to a window if the mouse causes the cursor to move within a window and mouse input is not captured. <br/> |



 

### Cursor Structures



| Name                             | Description                                    |
|----------------------------------|------------------------------------------------|
| [**CURSORINFO**](/windows/win32/api/winuser/ns-winuser-cursorinfo) | Contains global cursor information.<br/> |



 

 

 





