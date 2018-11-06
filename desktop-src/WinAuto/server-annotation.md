---
title: Server Annotation
description: This section provides information about using server annotation.
ms.assetid: d8de90af-f5ed-42ef-bd74-e383360e8128
ms.topic: article
ms.date: 05/31/2018
---

# Server Annotation

This section provides information about using server annotation.

## Summary

You define a class that implements [**IAccPropServer**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropserver), create an instance of it, and tell the system that you want it to override specific properties on specific UI elements. When a client requests one of the properties from one of the UI elements, your object is called and given an opportunity to provide a value. If your object returns a value, that value is passed back to the client. If your object does not return a value, the default value for that UI element is returned to the client.

## When to Use This Technique

Use this technique when you want to override the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties for an object. This technique is much simpler than previous **IAccessible** techniques. For more information, see [Alternatives to Dynamic Annotation](alternatives-to-dynamic-annotation.md).

You cannot use server annotation to alter the exposed object structure. To change the structure of an object, you must implement a full [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer.

For more information on server annotation, see the following topics:

-   [Using Server Annotation](using-server-annotation.md)
-   [Server Annotation Sample](server-annotation-sample.md)

 

 




