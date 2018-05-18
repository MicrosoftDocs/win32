---
Description: 'This section discusses window procedures. Each window has an associated window procedure that processes all messages sent or posted to all windows of the class.'
ms.assetid: '3a8e8f4e-910d-4863-a4a7-dd37c2dfa402'
title: Window Procedures
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
| [**CallWindowProc**](callwindowproc.md) | Passes message information to the specified window procedure. <br/>                                                                                                                                                                                                                                     |
| [**DefWindowProc**](defwindowproc.md)   | Calls the default window procedure to provide default processing for any window messages that an application does not process. This function ensures that every message is processed. [**DefWindowProc**](defwindowproc.md) is called with the same parameters received by the window procedure. <br/> |
| [*WindowProc*](windowproc.md)           | An application-defined function that processes messages sent to a window. The **WNDPROC** type defines a pointer to this callback function. [*WindowProc*](windowproc.md) is a placeholder for the application-defined function name. <br/>                                                            |



 

 

 




