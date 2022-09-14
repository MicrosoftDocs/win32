---
title: Using the IAccessible Interface
description: The IAccessible interface is a collection of methods that expose the most common attributes and behaviors of a wide range of UI elements.
ms.assetid: 82f6e934-58ea-47f2-98a3-2ab1c20f24c3
ms.topic: article
ms.date: 05/31/2018
---

# Using the IAccessible Interface

The [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface is a collection of methods that expose the most common attributes and behaviors of a wide range of UI elements. A UI element is a control, such as a menu or push button, that is part of the user interface. An accessible object is a UI element that has a meaningful **IAccessible** interface.

Some of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties are not applicable to every kind of user interface element. Also, the implementation of **IAccessible** varies from application to application.

Although the parameters and return values for the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods are fully specified, how a client should use a property or how a server should implement a property is sometimes subject to interpretation.

This section provides suggestions, guidelines, and examples for helping client applications obtain information about UI elements and for helping server applications provide appropriate information.

## In this section

-   [Content of Descriptive Properties](content-of-descriptive-properties.md)
-   [Selection and Focus Properties and Methods](selection-and-focus-properties-and-methods.md)
-   [Object Navigation Properties and Methods](object-navigation-properties-and-methods.md)

 

 




