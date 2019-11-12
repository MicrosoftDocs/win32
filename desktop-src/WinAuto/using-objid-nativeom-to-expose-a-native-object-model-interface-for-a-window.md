---
title: Use OBJID\_NATIVEOM to expose a native interface for a window
description: This technique allows clients to get a custom object for a window. Servers can use this to expose a pointer to a custom document object for a window.
ms.assetid: 91713fe5-f03f-464e-88ee-9d8d66d5b19d
ms.topic: article
ms.date: 05/31/2018
---

# Use OBJID\_NATIVEOM to expose a native interface for a window

This technique allows clients to get a custom object for a window. Servers can use this to expose a pointer to a custom document object for a window.

**To expose a native object model interface for a window (servers)**

1.  Handle the [**WM\_GETOBJECT**](wm-getobject.md) message in the window procedure. When the *lParam* value is [**OBJID\_NATIVEOM**](object-identifiers.md), return an interface pointer to the custom object using [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject).
2.  Release your interface pointer after calling [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject), if appropriate. For more information, see **LresultFromObject**.

Clients can obtain a pointer to this custom object.

**To obtain a pointer for a custom object for a window (clients)**

-   Call [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) and pass [**OBJID\_NATIVEOM**](object-identifiers.md) as the second parameter.

Note the following issues for this technique:

-   This technique is similar to returning an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer except for the object ID used and the fact that [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) returns a custom object instead of **IAccessible**.
-   Server developers may need to publish information that allows clients to uniquely identify the **HWND** so that they can find it before calling [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) on its window handle.
-   Do not implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface on the custom object that is returned. If you do, OLEACC will treat it is as a standard **IAccessible** and may prevent the custom interfaces from being used.
-   In order to be used across processes, the interfaces on the returned object may need to be registered with Component Object Model (COM).

This technique is supported by several Microsoft Office components. For more information, see [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow).

 

 




