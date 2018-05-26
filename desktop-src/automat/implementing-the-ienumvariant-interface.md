---
title: Implementing the IEnumVARIANT Interface
description: Automation defines the IEnumVARIANT interface to provide a standard way for ActiveX clients to iterate over collection objects.
ms.assetid: 7f20c07d-05f6-447a-8bed-72100cd96a97
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing the IEnumVARIANT Interface

Automation defines the [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master) interface to provide a standard way for ActiveX clients to iterate over collection objects. Every collection object must expose a read-only property named **\_NewEnum** to let ActiveX clients know that the object supports iteration. The **\_NewEnum** property returns an enumerator object that supports [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master).

The [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master) interface provides a way to iterate through the items contained by a collection object. This interface is supported by an enumerator object that is returned by the **\_NewEnum** property of the collection object, as in the following figure.

![](images/oa02-02.png)

The [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master) interface defines these member functions:

-   [**Next**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-next?branch=master) — Retrieves one or more elements in a collection, starting with the current element.

-   [**Skip**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-skip?branch=master) — Skips over one or more elements in a collection.

-   [**Reset**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-reset?branch=master) — Resets the current element to the first element in the collection.

-   [**Clone**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-clone?branch=master) — Copies the current state of the enumeration so you can return to the current element after using [**Skip**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-skip?branch=master) or [**Reset**](/windows/previous-versions/oaidl/nf-oaidl-ienumvariant-reset?branch=master).

 

 




