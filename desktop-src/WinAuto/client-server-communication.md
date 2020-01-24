---
title: Client/Server Communication
description: The WinEvents mechanism provides a way for servers to communicate easily with Microsoft Active Accessibility clients.
ms.assetid: 992fe603-dcfe-4afd-88db-6d258a7a5f64
ms.topic: article
ms.date: 05/31/2018
---

# Client/Server Communication

The [WinEvents](winevents-overview.md) mechanism provides a way for servers to communicate easily with Microsoft Active Accessibility clients. Clients often collect information by reacting to WinEvents (for example, following focus), but they are free to request information from a server at any time.

To request information for an accessible object that generates a WinEvent, a client must process the event and establish a connection with the relevant accessible object. To do this, the client performs the following six steps:

-   A server calls [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) to generate a WinEvent notification for each change to its user interface elements.
-   The WinEvent management code in USER determines if any client applications have registered a WinEvent [*hook function*](/windows/desktop/api/Winuser/nc-winuser-wineventproc) using [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook) and calls the registered callback function.
-   In its callback function, the client requests access to the object that generated the event by calling [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent) or other accessible object retrieval functions. For more information, see [Retrieving an IAccessible Object](retrieving-an-iaccessible-object.md).
-   This Microsoft Active Accessibility API sends the server application a [**WM\_GETOBJECT**](wm-getobject.md) message to retrieve the accessible object.
-   In response to [**WM\_GETOBJECT**](wm-getobject.md), the server application either returns zero or returns a value that acts as a one-time reference to the object that generated the event.
-   If the server returns zero, Microsoft Active Accessibility creates a proxy object and gives its address to the client. Otherwise, Microsoft Active Accessibility uses this reference to retrieve the address of an object interface such as [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) or [**IDispatch**](idispatch-interface.md), and gives that address to the client.

Once the client has an interface address, it can call the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods of the accessible object to retrieve information.

## In this section

-   [WinEvents and Active Accessibility](winevents-overview.md)
-   [How WM\_GETOBJECT Works](how-wm-getobject-works.md)
-   [Retrieving an IAccessible Object](retrieving-an-iaccessible-object.md)

 

 




