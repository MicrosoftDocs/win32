---
title: Retrieving an IAccessible Object
description: Microsoft Active Accessibility provides functions such as AccessibleObjectFromWindow and AccessibleObjectFromPoint that allow clients to retrieve accessible objects.
ms.assetid: '971cbead-128b-465a-8e77-2a20217f8d0f'
---

# Retrieving an IAccessible Object

Microsoft Active Accessibility provides functions such as [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md) and [**AccessibleObjectFromPoint**](accessibleobjectfrompoint.md) that allow clients to retrieve accessible objects. These functions return either an [**IDispatch**](idispatch-interface.md) or [**IAccessible**](iaccessible.md) interface pointer through which clients get information about the accessible object.

When a client calls [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md) or any of the other **AccessibleObjectFrom***X* functions that retrieve an interface to an object, Microsoft Active Accessibility sends the [**WM\_GETOBJECT**](wm-getobject.md) window message to the applicable window procedure within the appropriate application. To provide information to clients, servers must respond to the **WM\_GETOBJECT** message.

To collect specific information about a UI element, clients must first retrieve an [**IAccessible**](iaccessible.md) interface for the element. To retrieve an element's **IAccessible** object, clients can use one of the following functions:

-   [**AccessibleObjectFromPoint**](accessibleobjectfrompoint.md)
-   [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md)
-   [**AccessibleObjectFromEvent**](accessibleobjectfromevent.md)

**To retrieve an IAccessible Interface Pointer**

1.  Client calls one of the **AccessibleObjectFrom***X* functions.
2.  Oleacc.dll sends a [**WM\_GETOBJECT**](wm-getobject.md) message to server.
3.  The server determines which UI element corresponds to the request.
4.  The server either returns zero to request an Oleacc.dll proxy,

    Or

    Returns an [**IAccessible**](iaccessible.md) object (native implementation). To do this, it:

    -   Constructs an [**IAccessible**](iaccessible.md) object for the element.
    -   Calls [**LresultFromObject**](lresultfromobject.md) to marshal the object's pointer.
    -   Returns the LRESULT to Oleacc.dll.

5.  Oleacc.dll examines the return value from [**WM\_GETOBJECT**](wm-getobject.md).

    If it is zero, Oleacc.dll constructs a proxy object and returns it to the client.

    Or

    If it is nonzero, Oleacc.dll calls [**ObjectFromLresult**](objectfromlresult.md) to unmarshal the native [**IAccessible**](iaccessible.md) object pointer and returns it to the client.

 

 




