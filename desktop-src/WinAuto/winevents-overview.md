---
title: WinEvents and Active Accessibility Overview
description: Microsoft Active Accessibility servers raise WinEvents to notify clients when an accessible object changes.
ms.assetid: 'a2d486ee-84ef-4c44-a832-dbc0dae81542'
ms.topic: article
ms.date: 05/31/2018
---

# WinEvents and Active Accessibility

Microsoft Active Accessibility servers raise *WinEvents* to notify clients when an accessible object changes. There are numerous conditions in which a server notifies a client of a change. Each [event constant](event-constants.md) defined by Microsoft Active Accessibility describes a condition about which a client is notified. For example, WinEvents can signal:

- When an object is created or destroyed.
- When an object receives or loses focus.
- When the state or location of an object changes.
- When any property of an object changes.

Client applications do not receive event notifications automatically; they must specify which events they want to receive by calling the [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook) function. With **SetWinEventHook**, a client registers to receive one or more events and sets a hook function to handle the specified events. Clients can use the same hook function to handle multiple types of events, or it can use multipe hook functions. Clients call the **SetWinEventHook** once for each hook function it needs to register.

Hook functions are located within the client's code body, in a DLL mapped into the client's process, or in a DLL mapped into the server's process. Each of these methods has advantages and disadvantages. For more information, see [In-Context and Out-of-Context Hook Functions](in-context-and-out-of-context-hook-functions.md).

To notify clients of an event occurrence, servers call [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent). The system checks whether any client applications have set hook functions for the event and calls the appropriate hook functions as necessary.

When the client's hook function is called, it receives a number of parameters that describe the event and the object that generated the event. To gain access to the object that generated the event, the client hook function calls [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent).

> [!NOTE]
> If no clients have registered to receive WinEvents, the performance impact on a server for calling [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) is negligible.
>
> Servers call [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) for changes only in their own accessible objects; they do not call **NotifyWinEvent** for changes in system-provided user interface elements.

## Event-Driven Communication

Clients must register a WinEvent hook before they can receive WinEvent notifications. To avoid unnecessary callbacks and improve performance, clients are advised to register only for the events they need to receive.

Inside the hook procedure, the client can call [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent) to retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for the element to which the event applies. With this object, the client can begin calling **IAccessible** methods to retrieve information or interact with the UI element.

## Related topics

[WinEvents](winevents-infrastructure.md)
