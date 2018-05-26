---
title: Retrieving an IAccessible Object
description: Microsoft Active Accessibility provides functions such as AccessibleObjectFromWindow and AccessibleObjectFromPoint that allow clients to retrieve accessible objects.
ms.assetid: 971cbead-128b-465a-8e77-2a20217f8d0f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving an IAccessible Object

Microsoft Active Accessibility provides functions such as [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) and [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master) that allow clients to retrieve accessible objects. These functions return either an [**IDispatch**](idispatch-interface.md) or [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer through which clients get information about the accessible object.

When a client calls [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) or any of the other **AccessibleObjectFrom***X* functions that retrieve an interface to an object, Microsoft Active Accessibility sends the [**WM\_GETOBJECT**](wm-getobject.md) window message to the applicable window procedure within the appropriate application. To provide information to clients, servers must respond to the **WM\_GETOBJECT** message.

To collect specific information about a UI element, clients must first retrieve an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface for the element. To retrieve an element's **IAccessible** object, clients can use one of the following functions:

-   [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master)
-   [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master)
-   [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master)

**To retrieve an IAccessible Interface Pointer**

1.  Client calls one of the **AccessibleObjectFrom***X* functions.
2.  Oleacc.dll sends a [**WM\_GETOBJECT**](wm-getobject.md) message to server.
3.  The server determines which UI element corresponds to the request.
4.  The server either returns zero to request an Oleacc.dll proxy,

    Or

    Returns an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) object (native implementation). To do this, it:

    -   Constructs an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) object for the element.
    -   Calls [**LresultFromObject**](/windows/win32/Oleacc/nf-oleacc-lresultfromobject?branch=master) to marshal the object's pointer.
    -   Returns the LRESULT to Oleacc.dll.

5.  Oleacc.dll examines the return value from [**WM\_GETOBJECT**](wm-getobject.md).

    If it is zero, Oleacc.dll constructs a proxy object and returns it to the client.

    Or

    If it is nonzero, Oleacc.dll calls [**ObjectFromLresult**](/windows/win32/Oleacc/nf-oleacc-objectfromlresult?branch=master) to unmarshal the native [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) object pointer and returns it to the client.

 

 




