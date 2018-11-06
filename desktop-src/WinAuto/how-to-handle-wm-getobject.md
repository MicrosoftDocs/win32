---
title: How to Handle WM_GETOBJECT
description: When it receives a WM\_GETOBJECT message that contains OBJID\_CLIENT, the server must return a pointer to the object that implements IAccessible.
ms.assetid: 455398b7-f748-4ab0-8953-3f74439e44f1
ms.topic: article
ms.date: 05/31/2018
---

# How to Handle WM\_GETOBJECT

When it receives a [**WM\_GETOBJECT**](wm-getobject.md) message that contains [**OBJID\_CLIENT**](object-identifiers.md), the server must return a pointer to the object that implements [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible). This pointer is an LRESULT that is obtained by calling [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject). Microsoft Active Accessibility, in conjunction with the Component Object Model (COM) library, performs the appropriate marshaling and passes the **IAccessible** interface pointer from the server to the client.

Servers must correctly handle reference counting on the accessible object. Remember that when you create a COM object, the reference count is 1. [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) then further increments the reference count several times. All the references created by **LresultFromObject** are automatically released when the object is no longer needed, but the server is responsible for releasing the initial reference, and unless it does so, the object will never be destroyed. The examples in the following sections show how to release references to accessible objects.

Servers typically handle [**WM\_GETOBJECT**](wm-getobject.md) in one of the following ways:

-   [Create New Accessible Objects](create-new-accessible-objects.md)
-   [Reuse Existing Pointers to Objects](reuse-existing-pointers-to-objects.md)
-   [Create New Interfaces to the Same Object](create-new-interfaces-to-the-same-object.md)

> [!Note]  
> In this section as in the rest of the documentation, when a pointer to an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface is discussed, this pointer may actually be a pointer to a proxy object that wraps the **IAccessible** interface. For more information about proxy objects, see [Creating Proxy Objects](creating-proxy-objects.md).

 

For an overview of [**WM\_GETOBJECT**](wm-getobject.md), see [How WM\_GETOBJECT Works](how-wm-getobject-works.md).

 

 




