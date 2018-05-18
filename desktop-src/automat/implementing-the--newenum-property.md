---
title: Implementing the \_NewEnum Property
description: The \_NewEnum property identifies an object as supporting iteration through the IEnumVARIANT interface.
ms.assetid: 'f45fd5b8-b0d7-4a71-ba6b-ab34da0cc6dd'
---

# Implementing the \_NewEnum Property

The **\_NewEnum** property identifies an object as supporting iteration through the [**IEnumVARIANT**](ienumvariant.md) interface. This property has the following requirements:

-   Must be named **\_NewEnum** and must not be localized.

-   Must return a pointer to the enumerator object's **IUnknown** interface.

-   Must include DISPID = DISPID\_NEWENUM (-4).

 

 




