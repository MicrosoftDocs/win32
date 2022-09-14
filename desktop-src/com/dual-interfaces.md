---
title: Dual Interfaces (COM)
description: Dual Interfaces
ms.assetid: 6e4dc529-8a25-4ae5-b868-28cb17e0db52
ms.topic: article
ms.date: 05/31/2018
---

# Dual Interfaces

OLE Automation enables an object to expose a set of methods in two ways: via the **IDispatch** interface, and through direct OLE VTable binding. **IDispatch** is used by most tools available today, and offers support for late binding to properties and methods.

VTable binding offers much higher performance because this method is called directly instead of through **IDispatch::Invoke**. **IDispatch** offers late bound support, where direct VTable binding offers a significant performance gain; both techniques are valuable and important in different scenarios. By labeling an interface as \[[**dual**](/windows/desktop/Midl/dual)\] in the type library, an OLE Automation interface can be used either via **IDispatch**, or it can be bound to directly. Containers can thus choose the most appropriate technique. Support for dual interfaces is strongly recommended for both controls and containers.

 

 