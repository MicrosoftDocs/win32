---
title: Using OBJID\_NATIVEOM to expose a native object model interface for a window
description: This technique allows clients to get a custom object for a window. Servers can use this to expose a pointer to a custom document object for a window.
ms.assetid: '91713fe5-f03f-464e-88ee-9d8d66d5b19d'
---

# Using OBJID\_NATIVEOM to expose a native object model interface for a window

This technique allows clients to get a custom object for a window. Servers can use this to expose a pointer to a custom document object for a window.

**To expose a native object model interface for a window (servers)**

1.  Handle the [**WM\_GETOBJECT**](wm-getobject.md) message in the window procedure. When the *lParam* value is [**OBJID\_NATIVEOM**](object-identifiers.md#objid-nativeom), return an interface pointer to the custom object using [**LresultFromObject**](lresultfromobject.md).
2.  Release your interface pointer after calling [**LresultFromObject**](lresultfromobject.md), if appropriate. For more information, see **LresultFromObject**.

Clients can obtain a pointer to this custom object.

**To obtain a pointer for a custom object for a window (clients)**

-   Call [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md) and pass [**OBJID\_NATIVEOM**](object-identifiers.md#objid-nativeom) as the second parameter.

Note the following issues for this technique:

-   This technique is similar to returning an [**IAccessible**](iaccessible.md) interface pointer except for the object ID used and the fact that [**LresultFromObject**](lresultfromobject.md) returns a custom object instead of **IAccessible**.
-   Server developers may need to publish information that allows clients to uniquely identify the **HWND** so that they can find it before calling [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md) on its window handle.
-   Do not implement the [**IAccessible**](iaccessible.md) interface on the custom object that is returned. If you do, OLEACC will treat it is as a standard **IAccessible** and may prevent the custom interfaces from being used.
-   In order to be used across processes, the interfaces on the returned object may need to be registered with Component Object Model (COM).

This technique is supported by several Microsoft Office components. For more information, see [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md).

 

 




