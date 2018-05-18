---
title: Implementing the IEnumVARIANT Interface
description: Automation defines the IEnumVARIANT interface to provide a standard way for ActiveX clients to iterate over collection objects.
ms.assetid: '7f20c07d-05f6-447a-8bed-72100cd96a97'
---

# Implementing the IEnumVARIANT Interface

Automation defines the [**IEnumVARIANT**](ienumvariant.md) interface to provide a standard way for ActiveX clients to iterate over collection objects. Every collection object must expose a read-only property named **\_NewEnum** to let ActiveX clients know that the object supports iteration. The **\_NewEnum** property returns an enumerator object that supports [**IEnumVARIANT**](ienumvariant.md).

The [**IEnumVARIANT**](ienumvariant.md) interface provides a way to iterate through the items contained by a collection object. This interface is supported by an enumerator object that is returned by the **\_NewEnum** property of the collection object, as in the following figure.

![](images/oa02-02.png)

The [**IEnumVARIANT**](ienumvariant.md) interface defines these member functions:

-   [**Next**](ienumvariant-next.md) — Retrieves one or more elements in a collection, starting with the current element.

-   [**Skip**](ienumvariant-skip.md) — Skips over one or more elements in a collection.

-   [**Reset**](ienumvariant-reset.md) — Resets the current element to the first element in the collection.

-   [**Clone**](ienumvariant-clone.md) — Copies the current state of the enumeration so you can return to the current element after using [**Skip**](ienumvariant-skip.md) or [**Reset**](ienumvariant-reset.md).

 

 




