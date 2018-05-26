---
title: Object Navigation Properties and Methods
description: Clients navigate from one object to another using methods such as IAccessible accNavigate and IAccessible accHitTest.
ms.assetid: c6bcd044-bf70-4eec-92ae-66f9bd836c33
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Object Navigation Properties and Methods

Clients *navigate* from one object to another using methods such as [**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master) and [**IAccessible::accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master). These methods allow clients to retrieve either a child ID or the address of another object's [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface. Navigation allows clients to explore how objects are related to each other. Note that navigating to another object does not change the selection or focus.

The [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface provides properties and methods that support the following kinds of navigation:

-   [Hierarchical Navigation](hierarchical-navigation.md)
-   [Spatial and Logical Navigation](spatial-and-logical-navigation.md)
-   [Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)

 

 




