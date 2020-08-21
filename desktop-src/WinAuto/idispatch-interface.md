---
title: IDispatch Interface and Accessibility
description: The IDispatch interface was initially designed to support Automation.
ms.assetid: 5a95f002-4fd5-43d3-9b50-7b3f7790300a
ms.topic: article
ms.date: 05/31/2018
---

# IDispatch Interface and Accessibility

The [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface was initially designed to support Automation. It provides a late-binding mechanism to access and retrieve information about an object's methods and properties. Previously, server developers had to implement both the **IDispatch** and [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interfaces for their accessible objects; that is, they had to provide a [dual interface](dual-interfaces--iaccessible-and-idispatch.md). With Microsoft Active Accessibility 2.0, servers can return **E\_NOTIMPL** from **IDispatch** methods and Microsoft Active Accessibility will implement the **IAccessible** interface for them.

In addition to the methods inherited from [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown), server developers must implement the following methods within the class definition of each object that is exposed:

-   [**GetTypeInfoCount**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfocount) returns the number of type descriptions for the object. For objects that support [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch), the type information count is always one.
-   [**GetTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfo) retrieves a description of the object's programmable interface.
-   [**GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames) maps the name of a method or property to a **DISPID**, which is later used to invoke the method or property.
-   [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) calls one of the object's methods, or gets or sets one of its properties.

 

 