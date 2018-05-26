---
title: Implementing Dual Interfaces
description: It is recommended that you implement dual interfaces because of the advantages in doing so.
ms.assetid: a8e877bc-6e28-4413-9070-ef979f39d1a4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing Dual Interfaces

Although Automation allows you to implement an [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface, a [VTBL](glossary.md) interface, or a [dual](dual.md) interface (which encompasses both), it is strongly recommended that you implement *dual* interfaces for all exposed ActiveX objects. Dual interfaces have significant advantages over **IDispatch**-only or VTBL-only interfaces.

-   Binding can take place at compile time through the VTBL interface, or at run time through [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master).

-   ActiveX clients that can use the VTBL interface may benefit from improved performance.

-   Existing ActiveX clients that use the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface will continue to work.

-   The VTBL interface is easier to call from C++.

-   *Dual* interfaces are required for compatibility with Visual Basic object support features.

 

 




