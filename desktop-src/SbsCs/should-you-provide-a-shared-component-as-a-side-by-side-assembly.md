---
description: Providers of shared components should consider making their component available as a side-by-side assembly if one or more of the following cases are true.
ms.assetid: 543451cd-0608-4302-a85b-ddce79a5cfd6
title: Should you provide a shared component as a side-by-side assembly?
ms.topic: article
ms.date: 05/31/2018
---

# Should you provide a shared component as a side-by-side assembly?

Providers of shared components should consider making their component available as a side-by-side assembly if one or more of the following are true:

-   The component exposes a rich application programming interface that is used by many applications. For example, a component such as MSHTML, which enables C and C++ applications to access the Dynamic HTML (DHTML) Object Model.
-   The component is already being shared by multiple applications. For example, a component such as COMCTL32, which provides applications access to the common controls.
-   The component is a new component.
-   The component is a user-mode component and not a device driver.

Not every component is a suitable candidate for a side-by-side assembly. A component is not a suitable candidate for a side-by-side assembly if any of the following are true:

-   The component handles communication between applications. For example, parts of OLE32 would not make a good side-by-side assembly because you would not want to have two different versions of the parts that coordinate communication between applications run on your system.
-   The component manages a physical or virtual device for the system. For example a device driver for a print spooler.

In some cases it may be possible for the developer of the component to redesign an existing component in order to make it suitable for publication as a side-by-side assembly. For more information see [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md).

 

 



