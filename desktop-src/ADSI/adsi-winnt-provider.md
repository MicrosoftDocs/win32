---
title: ADSI WinNT Provider
description: The Microsoft ADSI provider implements a set of ADSI objects to support various ADSI interfaces.
ms.assetid: 6341be08-2e53-4708-a403-09c86fcc31a8
ms.tgt_platform: multiple
keywords:
- adsi winnt provider ADSI
- WinNT service provider ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADSI WinNT Provider

The Microsoft ADSI provider implements a set of ADSI objects to support various ADSI interfaces. The namespace name for the Windows provider is "WinNT" and this provider is commonly referred to as the WinNT provider. To access the WinNT provider, bind to any of the [ADSI objects of WinNT](adsi-objects-of-winnt.md), using the [WinNT AdsPath](winnt-adspath.md).

The WinNT provider is included in the ADSI system component for Windows and Windows Server.

> [!Note]  
> The default WinNT provider cannot be assumed to be completely thread-safe. Writers of multithreaded applications should handle multithreading to properly coordinate any access between threads through the proper use of synchronization objects such as semaphores, mutexes, critical sections, and so on.

 

 

 




