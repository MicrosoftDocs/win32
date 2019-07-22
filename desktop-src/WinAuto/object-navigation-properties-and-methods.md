---
title: Object Navigation Properties and Methods
description: Clients navigate from one object to another using methods such as IAccessible accNavigate and IAccessible accHitTest.
ms.assetid: c6bcd044-bf70-4eec-92ae-66f9bd836c33
ms.topic: reference
ms.date: 05/31/2018
---

# Object Navigation Properties and Methods

Clients *navigate* from one object to another using methods such as [**IAccessible::accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate) and [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest). These methods allow clients to retrieve either a child ID or the address of another object's [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. Navigation allows clients to explore how objects are related to each other. Note that navigating to another object does not change the selection or focus.

The [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface provides properties and methods that support the following kinds of navigation:

-   [Hierarchical Navigation](hierarchical-navigation.md)
-   [Spatial and Logical Navigation](spatial-and-logical-navigation.md)
-   [Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)

 

 




