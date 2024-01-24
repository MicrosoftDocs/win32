---
description: This section discusses window procedures. Each window has an associated window procedure that processes all messages sent or posted to all windows of the class.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\windowprocedures.htm'
title: Window Procedures
ms.topic: article
ms.date: 05/31/2018
---

# Window Procedures

Every window has an associated window procedure — a function that processes all messages sent or posted to all windows of the class. All aspects of a window's appearance and behavior depend on the window procedure's response to these messages.

### In This Section



| Name                                                         | Description                                                                                                                                                                                                    |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Window Procedures](about-window-procedures.md)       | Discusses window procedures. Each window is a member of a particular window class. The window class determines the default window procedure that an individual window uses to process its messages.<br/> |
| [Using Window Procedures](using-window-procedures.md)       | Covers how to perform the following tasks associated with window procedures.<br/>                                                                                                                        |
| [Window Procedure Reference](window-procedure-reference.md) | Contains the API reference.<br/>                                                                                                                                                                         |



 

### Functions



| Name                                     | Description                                                                                                                                                                                                                                                                                                   |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallWindowProc**](/windows/win32/api/winuser/nf-winuser-callwindowproca) | Passes message information to the specified window procedure. <br/>                                                                                                                                                                                                                                     |
| [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)   | Calls the default window procedure to provide default processing for any window messages that an application does not process. This function ensures that every message is processed. [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) is called with the same parameters received by the window procedure. <br/> |
| [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc)           | An application-defined function that processes messages sent to a window. The **WNDPROC** type defines a pointer to this callback function. [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) is a placeholder for the application-defined function name. <br/>                                                            |



 

 

 
