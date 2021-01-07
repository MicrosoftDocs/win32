---
description: When using a Windows Image Acquisition (WIA) interface in more than one thread within a single process, an application must provide marshalling for that interface.
ms.assetid: b125b36e-1428-4aa6-b367-eac78291c88e
title: Using Multiple Threads in a WIA Application
ms.topic: article
ms.date: 05/31/2018
---

# Using Multiple Threads in a WIA Application

When using a Windows Image Acquisition (WIA) interface in more than one thread within a single process, an application must provide marshalling for that interface. If one thread creates an interface pointer, you cannot use that pointer in a different thread without marshalling.

For example, if one thread in an application obtains a pointer to the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) interface, a separate thread cannot use that interface pointer without marshalling.

A common technique used to accomplish this marshalling is to use the global interface table. The global interface table is a table maintained across all threads within a single process. All threads running within the process can retrieve interfaces that are registered to the global interface table. This technique avoids the need to create streams for passing interfaces between threads.

For information on how to use the global interface table, see [IGlobalInterfaceTable](/windows/win32/api/objidl/nn-objidl-iglobalinterfacetable).

Even if you do not intend to use multiple threads in a WIA application, you must assume that all data transfer or device event callback functions run in separate threads.

 

 
