---
title: Dynamic Annotation API
description: The Dynamic Annotation API is an extension to Microsoft Active Accessibility that allows developers to customize existing IAccessible support without having to use error-prone subclassing or wrapping techniques.
ms.assetid: 2daf0e76-b300-47e7-994b-d1d00d0dca4d
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Annotation API

The Dynamic Annotation API is an extension to Microsoft Active Accessibility that allows developers to customize existing [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) support without having to use error-prone subclassing or wrapping techniques. This mechanism also allows developers to pass hints or other useful information to the Oleacc.dll proxies.

Dynamic Annotation is typically used to correct or amend an inaccurate instance of an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object exposed by an existing Oleacc.dll proxy. For example, you can use it to override the [**Name**](name-property.md) and [**Role**](role-property.md) properties provided by the default proxy, and to supply [**Description**](description-property.md) and [**Help**](help-property.md) properties (which may not be provided by the default proxy).

With Windows 7, developers can use the Dynamic Annotation API to annotate Microsoft UI Automation properties as well as Microsoft Active Accessibility properties of the proxy objects that Oleacc.dll creates for standard Windows controls. The Oleacc.dll proxy objects serve both Microsoft Active Accessibility and UI Automation clients.

## In this section

-   [Background Information](background-information.md)
-   [Alternatives to Dynamic Annotation](alternatives-to-dynamic-annotation.md)
-   [Types of Dynamic Annotation](types-of-dynamic-annotation.md)
-   [Direct Annotation](direct-annotation.md)
-   [Value Map Annotation](value-map-annotation.md)
-   [Server Annotation](server-annotation.md)
-   [Issues and Limitations](issues-and-limitations.md)

 

 




