---
title: How Active Accessibility Exposes User Interface Elements
description: Microsoft Active Accessibility creates a proxy object for each user interface element that it exposes.
ms.assetid: 64aa8fac-cea7-4466-ae34-2760956c296b
ms.topic: article
ms.date: 05/31/2018
---

# How Active Accessibility Exposes User Interface Elements

Microsoft Active Accessibility creates a *proxy* object for each user interface element that it exposes. A proxy object acts as an intermediary between the client utility and the UI element. The purpose of the proxy object is to monitor the life span of the UI element and to implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods on behalf of the UI element. Server developers who create custom controls or other custom UI elements should also create proxy objects. For more information, see [Creating Proxy Objects](creating-proxy-objects.md).

When Microsoft Active Accessibility creates an object to expose a predefined or common control, it actually creates at least two objects: one for the control and one for the window that surrounds the control. In most cases, these parent windows have the [Role property](role-property.md) of [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) and have the same [Name property](name-property.md) and window class name as the control. The information about the control that clients convey to end users is contained in the object that Microsoft Active Accessibility creates to expose the control, not the parent object that exposes the window that surrounds the control.

For more information, see the following topics.

-   [Screening Out Unnecessary Objects](screening-out-unnecessary-objects.md)
-   [Providing the Name Property](providing-the-name-property.md)
-   [Ensuring that UI Elements are Correctly Named](ensure-that-ui-elements-are-named-correctly.md)
-   [Unsupported User Interface Elements](unsupported-user-interface-elements.md)

 

 




