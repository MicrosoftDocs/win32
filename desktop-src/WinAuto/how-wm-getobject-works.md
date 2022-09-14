---
title: How WM_GETOBJECT Works
description: Microsoft Active Accessibility sends the WM\_GETOBJECT message to the appropriate server application when a client calls one of the AccessibleObjectFromX functions.
ms.assetid: 53f7b3db-97e4-4ff2-9f7a-4555ec7956ea
ms.topic: article
ms.date: 05/31/2018
---

# How WM\_GETOBJECT Works

Microsoft Active Accessibility sends the [**WM\_GETOBJECT**](wm-getobject.md) message to the appropriate server application when a client calls one of the **AccessibleObjectFrom***X* functions. The following list describes the various scenarios that occur:

-   If the window or control that receives [**WM\_GETOBJECT**](wm-getobject.md) implements [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible), the window returns a reference to the **IAccessible** interface using [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject). Microsoft Active Accessibility, in conjunction with the Component Object Model (COM) library, performs the appropriate marshaling and passes the interface pointer from the server back to the client.
-   If the window that receives the message does not implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible), it should return zero.
-   If the window does not handle the [**WM\_GETOBJECT**](wm-getobject.md) message, the [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) function returns zero.

Even if the server returns zero, Microsoft Active Accessibility still provides the client with information about the object. For most system-provided objects such as list boxes and buttons, Microsoft Active Accessibility provides complete information; for other objects, the information is limited. For example, Microsoft Active Accessibility does not provide information for controls that do not have a window handle. Microsoft Active Accessibility returns a proxied [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer that the client uses to get information about the object.

For more information, see [The WM\_GETOBJECT Message](the-wm-getobject-message.md).

 

 