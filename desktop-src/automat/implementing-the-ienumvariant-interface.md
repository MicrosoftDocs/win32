---
title: Implementing the IEnumVARIANT Interface
description: Automation defines the IEnumVARIANT interface to provide a standard way for ActiveX clients to iterate over collection objects.
ms.assetid: 7f20c07d-05f6-447a-8bed-72100cd96a97
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the IEnumVARIANT Interface

Automation defines the [**IEnumVARIANT**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant) interface to provide a standard way for ActiveX clients to iterate over collection objects. Every collection object must expose a read-only property named **\_NewEnum** to let ActiveX clients know that the object supports iteration. The **\_NewEnum** property returns an enumerator object that supports [**IEnumVARIANT**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant).

The [**IEnumVARIANT**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant) interface provides a way to iterate through the items contained by a collection object. This interface is supported by an enumerator object that is returned by the **\_NewEnum** property of the collection object, as in the following figure.

![](images/oa02-02.png)

The [**IEnumVARIANT**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant) interface defines these member functions:

-   [**Next**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-next) — Retrieves one or more elements in a collection, starting with the current element.

-   [**Skip**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-skip) — Skips over one or more elements in a collection.

-   [**Reset**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-reset) — Resets the current element to the first element in the collection.

-   [**Clone**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-clone) — Copies the current state of the enumeration so you can return to the current element after using [**Skip**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-skip) or [**Reset**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-reset).

 

 




