---
title: What Are WinEvents
description: Server applications and the operating system use WinEvents to notify clients when a change occurs in the system or in the user interface.
ms.assetid: 43723706-a173-4ddc-b135-824a7a8e8b40
ms.topic: article
ms.date: 05/31/2018
---

# What Are WinEvents?

Server applications and the operating system use WinEvents to notify clients when a change occurs in the system or in the user interface.

WinEvent support is a feature of the Windows operating system that provides:

-   A simple way for clients to register for event notifications.
-   A mechanism for injecting client code into servers.
-   Routing of events from servers to interested clients.
-   Automatic event generation for most **HWND**-based controls.

Event generation for **HWND**-based controls is especially important for server developers. The Microsoft Active Accessibility run-time provides [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) proxies for all standard UI elements. Similarly, the system automatically generates the appropriate WinEvents whenever it creates, destroys, moves, resizes, or performs any other action on an **HWND**-based control.

Some WinEvents, including general **HWND** events, are automatically supported by the system. Other types of WinEvents, such as state changes or selection events specific to a particular control, are supported by Microsoft Active Accessibility servers.

When an event occurs that affects the UI, servers can broadcast an event notification to all interested clients by calling the [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) function. The function call includes information that identifies the type of event that occurred, and the UI element to which the event applies. Clients can use this information to retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for the UI element and collect more information.

For example, to notify clients that a control's name has changed, a server calls [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) and passes [**EVENT\_OBJECT\_NAMECHANGE**](event-constants.md) in the event parameter. The system responds by determining which clients have registered to receive that particular event and calls their registered callback function. If no clients have registered for the event, the server's call to **NotifyWinEvent** is comparable to a "no operation" and the performance impact is negligible.

Servers call [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) to announce the event to the system after the event has occurred. They must never notify the system of an event before the event occurs.

To be notified of events, clients register callback hook functions by using [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook). Clients set a single hook function for all possible events or multiple hook functions for discrete ranges of events. For more information, see [Registering a Hook Function](registering-a-hook-function.md).

When Microsoft Active Accessibility is notified of an event, it calls any hook functions that were registered for that event, passing along the parameters from [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent).

 

 




