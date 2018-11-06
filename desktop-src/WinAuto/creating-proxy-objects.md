---
title: Creating Proxy Objects
description: In addition to designing classes that implement IAccessible properties and methods, server developers may also need to design proxy objects that monitor the life span of accessible objects.
ms.assetid: d140206a-9918-438b-96bd-df141da2f04b
ms.topic: article
ms.date: 05/31/2018
---

# Creating Proxy Objects

In addition to designing classes that implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods, server developers may also need to design *proxy* objects that monitor the life span of accessible objects. If an accessible object in an application is available the entire time the application is running, then you do not need to create a proxy object. If it is possible to destroy the accessible object while the application is running, then you must create a proxy object.

## In this section

-   [What Are Proxy Objects?](what-are-proxy-objects.md)
-   [Why Proxy Objects Are Needed](why-proxy-objects-are-needed.md)
-   [Design Considerations for Proxy Objects](design-considerations-for-proxy-objects.md)

 

 




