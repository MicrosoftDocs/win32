---
title: Exposing a Native Object Model Interface
description: If a UI element supports a native object model other than Microsoft Active Accessibility or UI Automation, it can expose the custom interface by responding to WM\_GETOBJECT messages that include the OBJID\_NATIVEOM object identifier.
ms.assetid: 430abeaf-e5ca-48c4-aa35-8d52a8cee2f1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Exposing a Native Object Model Interface

If a UI element supports a native object model other than Microsoft Active Accessibility or UI Automation, it can expose the custom interface by responding to [**WM\_GETOBJECT**](wm-getobject.md) messages that include the [**OBJID\_NATIVEOM**](object-identifiers.md#objid-nativeom) object identifier. To respond, the UI element should return the value retrieved by a call to the [**LresultFromObject**](/windows/win32/Oleacc/nf-oleacc-lresultfromobject?branch=master) function.

A client can retrieve an interface from a UI element that supports a native object model by calling the [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) function and specifying [**OBJID\_NATIVEOM**](object-identifiers.md#objid-nativeom) as the second parameter.

 

 




