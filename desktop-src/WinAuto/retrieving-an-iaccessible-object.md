---
title: Retrieving an IAccessible Object
description: Microsoft Active Accessibility provides functions such as AccessibleObjectFromWindow and AccessibleObjectFromPoint that allow clients to retrieve accessible objects.
ms.assetid: 971cbead-128b-465a-8e77-2a20217f8d0f
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an IAccessible Object

Microsoft Active Accessibility provides functions such as [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) and [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint) that allow clients to retrieve accessible objects. These functions return either an [**IDispatch**](idispatch-interface.md) or [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer through which clients get information about the accessible object.

When a client calls [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) or any of the other **AccessibleObjectFrom***X* functions that retrieve an interface to an object, Microsoft Active Accessibility sends the [**WM\_GETOBJECT**](wm-getobject.md) window message to the applicable window procedure within the appropriate application. To provide information to clients, servers must respond to the **WM\_GETOBJECT** message.

To collect specific information about a UI element, clients must first retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface for the element. To retrieve an element's **IAccessible** object, clients can use one of the following functions:

-   [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
-   [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow)
-   [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent)

**To retrieve an IAccessible Interface Pointer**

1.  Client calls one of the **AccessibleObjectFrom***X* functions.
2.  Oleacc.dll sends a [**WM\_GETOBJECT**](wm-getobject.md) message to server.
3.  The server determines which UI element corresponds to the request.
4.  The server either returns zero to request an Oleacc.dll proxy,

    Or

    Returns an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object (native implementation). To do this, it:

    -   Constructs an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for the element.
    -   Calls [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) to marshal the object's pointer.
    -   Returns the LRESULT to Oleacc.dll.

5.  Oleacc.dll examines the return value from [**WM\_GETOBJECT**](wm-getobject.md).

    If it is zero, Oleacc.dll constructs a proxy object and returns it to the client.

    Or

    If it is nonzero, Oleacc.dll calls [**ObjectFromLresult**](/windows/desktop/api/Oleacc/nf-oleacc-objectfromlresult) to unmarshal the native [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object pointer and returns it to the client.

 

 




