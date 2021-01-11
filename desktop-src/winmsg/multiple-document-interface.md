---
description: This section discusses the Multiple Document Interface which is a specification that defines a user interface for applications that enable the user to work with more than one document at the same time.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\multipledocumentinterface.htm'
title: Multiple Document Interface
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Document Interface

\[Many new and intermediate users find it difficult to learn to use MDI applications. Therefore, you should consider other models for your user interface. However, you can use MDI for applications which do not easily fit into an existing model.\]

The multiple-document interface (MDI) is a specification that defines a user interface for applications that enable the user to work with more than one document at the same time.

### In This Section



| Topic                                                                              | Description                                                                               |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [About the Multiple Document Interface](about-the-multiple-document-interface.md) | Describes the Multiple Document Interface.<br/>                                     |
| [Using the Multiple Document Interface](using-the-multiple-document-interface.md) | Explains how to perform tasks associated with the Multiple Document Interface.<br/> |
| [MDI Reference](multiple-document-interface-reference.md)                         | Contains the API reference.<br/>                                                    |



 

### MDI Functions



| Name                                                 | Description                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateMDIWindow**](/windows/win32/api/winuser/nf-winuser-createmdiwindowa)           | Creates a MDI child window. <br/>                                                                                                                                                                                                                                                                                                                                    |
| [**DefFrameProc**](/windows/win32/api/winuser/nf-winuser-defframeproca)                 | Provides default processing for any window messages that the window procedure of a MDI frame window does not process. All window messages that are not explicitly processed by the window procedure must be passed to the [**DefFrameProc**](/windows/win32/api/winuser/nf-winuser-defframeproca) function, not the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. <br/>                              |
| [**DefMDIChildProc**](/windows/win32/api/winuser/nf-winuser-defmdichildproca)           | Provides default processing for any window message that the window procedure of a MDI child window does not process. A window message not processed by the window procedure must be passed to the [**DefMDIChildProc**](/windows/win32/api/winuser/nf-winuser-defmdichildproca) function, not to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. <br/>                                             |
| [**TranslateMDISysAccel**](/windows/win32/api/winuser/nf-winuser-translatemdisysaccel) | Processes accelerator keystrokes for window menu commands of the MDI child windows associated with the specified MDI client window. The function translates [**WM\_KEYUP**](/windows/desktop/inputdev/wm-keyup) and [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) messages to [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand) messages and sends them to the appropriate MDI child windows. <br/> |



 

### MDI Messages



| Name                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_MDIACTIVATE**](wm-mdiactivate.md)       | Sent to a MDI client window to instruct the client window to activate a different MDI child window. <br/>                                                                                                                                                                                                                                                                                                                               |
| [**WM\_MDICASCADE**](wm-mdicascade.md)         | Sent to a MDI client window to arrange all its child windows in a cascade format. <br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**WM\_MDICREATE**](wm-mdicreate.md)           | Sent to a MDI client window to create an MDI child window. <br/>                                                                                                                                                                                                                                                                                                                                                                        |
| [**WM\_MDIDESTROY**](wm-mdidestroy.md)         | Sent to a MDI client window to close an MDI child window. <br/>                                                                                                                                                                                                                                                                                                                                                                         |
| [**WM\_MDIGETACTIVE**](wm-mdigetactive.md)     | Sent to a MDI client window to retrieve the handle to the active MDI child window. <br/>                                                                                                                                                                                                                                                                                                                                                |
| [**WM\_MDIICONARRANGE**](wm-mdiiconarrange.md) | Sent to a MDI client window to arrange all minimized MDI child windows. It does not affect child windows that are not minimized. <br/>                                                                                                                                                                                                                                                                                                  |
| [**WM\_MDIMAXIMIZE**](wm-mdimaximize.md)       | Sent to a MDI client window to maximize an MDI child window. The system resizes the child window to make its client area fill the client window. The system places the child window's window menu icon in the rightmost position of the frame window's menu bar, and places the child window's restore icon in the leftmost position. The system also appends the title bar text of the child window to that of the frame window. <br/> |
| [**WM\_MDINEXT**](wm-mdinext.md)               | Sent to a MDI client window to activate the next or previous child window. <br/>                                                                                                                                                                                                                                                                                                                                                        |
| [**WM\_MDIREFRESHMENU**](wm-mdirefreshmenu.md) | Sent to a MDI client window to refresh the window menu of the MDI frame window. <br/>                                                                                                                                                                                                                                                                                                                                                   |
| [**WM\_MDIRESTORE**](wm-mdirestore.md)         | Sent to a MDI client window to restore an MDI child window from maximized or minimized size. <br/>                                                                                                                                                                                                                                                                                                                                      |
| [**WM\_MDISETMENU**](wm-mdisetmenu.md)         | Sent to a MDI client window to replace the entire menu of an MDI frame window, to replace the window menu of the frame window, or both. <br/>                                                                                                                                                                                                                                                                                           |
| [**WM\_MDITILE**](wm-mditile.md)               | Sent to a MDI client window to arrange all of its MDI child windows in a tile format. <br/>                                                                                                                                                                                                                                                                                                                                             |



 

### MDI Structures



| Name                                       | Description                                                                                               |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) | Contains information about the class, title, owner, location, and size of a MDI child window. <br/> |



 

 

