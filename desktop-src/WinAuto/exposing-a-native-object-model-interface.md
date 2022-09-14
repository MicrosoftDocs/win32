---
title: Exposing a Native Object Model Interface
description: If a UI element supports a native object model other than Microsoft Active Accessibility or UI Automation, it can expose the custom interface by responding to WM\_GETOBJECT messages that include the OBJID\_NATIVEOM object identifier.
ms.assetid: 430abeaf-e5ca-48c4-aa35-8d52a8cee2f1
ms.topic: article
ms.date: 05/31/2018
---

# Exposing a Native Object Model Interface

If a UI element supports a native object model other than Microsoft Active Accessibility or UI Automation, it can expose the custom interface by responding to [**WM\_GETOBJECT**](wm-getobject.md) messages that include the [**OBJID\_NATIVEOM**](object-identifiers.md) object identifier. To respond, the UI element should return the value retrieved by a call to the [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) function.

A client can retrieve an interface from a UI element that supports a native object model by calling the [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) function and specifying [**OBJID\_NATIVEOM**](object-identifiers.md) as the second parameter.

 

 




