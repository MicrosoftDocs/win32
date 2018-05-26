---
title: IDispatch Interface and Accessibility
description: The IDispatch interface was initially designed to support Automation.
ms.assetid: 5a95f002-4fd5-43d3-9b50-7b3f7790300a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDispatch Interface and Accessibility

The [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608) interface was initially designed to support Automation. It provides a late-binding mechanism to access and retrieve information about an object's methods and properties. Previously, server developers had to implement both the **IDispatch** and [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interfaces for their accessible objects; that is, they had to provide a [dual interface](dual-interfaces--iaccessible-and-idispatch.md). With Microsoft Active Accessibility 2.0, servers can return **E\_NOTIMPL** from **IDispatch** methods and Microsoft Active Accessibility will implement the **IAccessible** interface for them.

In addition to the methods inherited from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509), server developers must implement the following methods within the class definition of each object that is exposed:

-   [**GetTypeInfoCount**](https://msdn.microsoft.com/library/windows/desktop/ms221674) returns the number of type descriptions for the object. For objects that support [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608), the type information count is always one.
-   [**GetTypeInfo**](https://msdn.microsoft.com/library/windows/desktop/ms221571) retrieves a description of the object's programmable interface.
-   [**GetIDsOfNames**](https://msdn.microsoft.com/library/windows/desktop/ms221306) maps the name of a method or property to a **DISPID**, which is later used to invoke the method or property.
-   [**Invoke**](https://msdn.microsoft.com/library/windows/desktop/ms221479) calls one of the object's methods, or gets or sets one of its properties.

 

 




