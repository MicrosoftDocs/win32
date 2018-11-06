---
title: Registering a Hook Function
description: Client applications receive WinEvents in a WinEventProc callback function. The actions performed by the callback function are defined by the application, but the syntax must be as specified in the prototype.
ms.assetid: 7e999335-6a41-4d22-82ef-1a8dd6cb656e
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Hook Function

Client applications receive WinEvents in a [*WinEventProc*](/windows/desktop/api/Winuser/nc-winuser-wineventproc) callback function. The actions performed by the callback function are defined by the application, but the syntax must be as specified in the prototype.

Before it can receive events, the function must be registered by calling [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook). The client can call **SetWinEventHook** more than once to register different hook functions, or to set additional events for a previously registered hook function.

When calling [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook) the client specifies which events to receive and how to receive them. The client can choose to:

-   Receive all events or a specific set of events.
-   Receive events from all threads or from a specific thread.
-   Receive events from all processes or from a specific process.
-   Handle events in process or out of process.

When an event is generated that matches the specified criteria, the system calls the client's [*WinEventProc*](/windows/desktop/api/Winuser/nc-winuser-wineventproc) callback function (or "hook procedure"). The parameters that the hook function receives tell the client about the window, object, and possible child element that generated the event. A client uses these parameters in an object retrieval call, such as [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent).

 

 




