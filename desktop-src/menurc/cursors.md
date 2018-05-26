---
title: Cursors
description: This section discusses cursors which are small pictures whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball.
ms.assetid: 0ca8e51c-1159-47e9-ba3f-5ced0667cadb
keywords:
- resources,cursors
- cursors,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**ClipCursor**](/windows/win32/Winuser/nf-winuser-clipcursor?branch=master)                     | Confines the cursor to a rectangular area on the screen. If a subsequent cursor position (set by the [**SetCursorPos**](/windows/win32/Winuser/nf-winuser-setcursorpos?branch=master) function or the mouse) lies outside the rectangle, the system automatically adjusts the position to keep the cursor inside the rectangular area. <br/> |
| [**CopyCursor**](/windows/win32/Winuser/nf-winuser-copycursor?branch=master)                     | Copies the specified cursor. <br/>                                                                                                                                                                                                                                                               |
| [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master)                 | Creates a cursor having the specified size, bit patterns, and hot spot. <br/>                                                                                                                                                                                                                    |
| [**DestroyCursor**](/windows/win32/Winuser/nf-winuser-destroycursor?branch=master)               | Destroys a cursor and frees any memory the cursor occupied. Do not use this function to destroy a shared cursor.<br/>                                                                                                                                                                            |
| [**GetClipCursor**](/windows/win32/Winuser/nf-winuser-getclipcursor?branch=master)               | Retrieves the screen coordinates of the rectangular area to which the cursor is confined. <br/>                                                                                                                                                                                                  |
| [**GetCursor**](/windows/win32/Winuser/nf-winuser-getcursor?branch=master)                       | Retrieves a handle to the current cursor. <br/>                                                                                                                                                                                                                                                  |
| [**GetCursorInfo**](/windows/win32/Winuser/nf-winuser-getcursorinfo?branch=master)               | Retrieves information about the global cursor.<br/>                                                                                                                                                                                                                                              |
| [**GetCursorPos**](/windows/win32/Winuser/nf-winuser-getcursorpos?branch=master)                 | Retrieves the cursor's position, in screen coordinates.<br/>                                                                                                                                                                                                                                     |
| [**GetPhysicalCursorPos**](/windows/win32/Winuser/nf-winuser-getphysicalcursorpos?branch=master) | Retrieves the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                               |
| [**LoadCursor**](/windows/win32/Winuser/nf-winuser-loadcursora?branch=master)                     | Loads the specified cursor resource from the executable (.EXE) file associated with an application instance.<br/>                                                                                                                                                                                |
| [**LoadCursorFromFile**](/windows/win32/Winuser/nf-winuser-loadcursorfromfilea?branch=master)     | Creates a cursor based on data contained in a file. <br/>                                                                                                                                                                                                                                        |
| [**SetCursor**](/windows/win32/Winuser/nf-winuser-setcursor?branch=master)                       | Sets the cursor shape. <br/>                                                                                                                                                                                                                                                                     |
| [**SetCursorPos**](/windows/win32/Winuser/nf-winuser-setcursorpos?branch=master)                 | Moves the cursor to the specified screen coordinates. If the new coordinates are not within the screen rectangle set by the most recent [**ClipCursor**](/windows/win32/Winuser/nf-winuser-clipcursor?branch=master) function call, the system automatically adjusts the coordinates so that the cursor stays within the rectangle. <br/>    |
| [**SetPhysicalCursorPos**](/windows/win32/Winuser/nf-winuser-setphysicalcursorpos?branch=master) | Sets the position of the cursor in physical coordinates.<br/>                                                                                                                                                                                                                                    |
| [**SetSystemCursor**](/windows/win32/Winuser/nf-winuser-setsystemcursor?branch=master)           | Enables an application to customize the system cursors. It replaces the contents of the system cursor specified by the *id* parameter with the contents of the cursor specified by the *hcur* parameter and then destroys *hcur*. <br/>                                                          |
| [**ShowCursor**](/windows/win32/Winuser/nf-winuser-showcursor?branch=master)                     | Displays or hides the cursor. <br/>                                                                                                                                                                                                                                                              |



 

### Cursor Notifications



| Name                                  | Description                                                                                                          |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**WM\_SETCURSOR**](wm-setcursor.md) | Sent to a window if the mouse causes the cursor to move within a window and mouse input is not captured. <br/> |



 

### Cursor Structures



| Name                             | Description                                    |
|----------------------------------|------------------------------------------------|
| [**CURSORINFO**](/windows/win32/Winuser/ns-winuser-tagcursorinfo?branch=master) | Contains global cursor information.<br/> |



 

 

 





