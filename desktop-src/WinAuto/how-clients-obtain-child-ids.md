---
title: How Clients Obtain Child IDs
description: How Clients Obtain Child IDs
ms.assetid: 8e5786fe-5123-4262-b0b8-5c9aff4787bb
ms.topic: article
ms.date: 05/31/2018
---

# How Clients Obtain Child IDs

Client developers can get an object's child ID in the following ways:

-   Call [**AccessibleChildren**](/windows/desktop/api/Oleacc/nf-oleacc-accessiblechildren). This function retrieves an array of [**VARIANT**](variant-structure.md) structures.
-   Query the object to see if it supports the [**IEnumVARIANT**](https://msdn.microsoft.com/library/windows/desktop/ms221053) interface. If it is present, use [**IEnumVARIANT::Next**](https://msdn.microsoft.com/library/windows/desktop/ms221369) obtain child IDs.
-   Collect the child IDs by calling the parent object's [**IAccessible::accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate) method.

> [!Note]  
> It is the responsibility of the client to free the memory used for the [**VARIANT**](variant-structure.md) structures. Clients also must call [**IUnknown::Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on any [**IDispatch**](idispatch-interface.md) interface that is returned.

 

 

 




