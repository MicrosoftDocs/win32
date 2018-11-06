---
title: ADSI LDAP Provider
description: The ADSI LDAP Provider implements a set of ADSI objects that support various ADSI interfaces. To access the LDAP provider, bind to any of the ADSI LDAP objects, using the LDAP ADsPath.
ms.assetid: 3c13ea2f-fe40-4fd4-8540-422f277e07c1
ms.tgt_platform: multiple
keywords:
- ADSI LDAP Provider
ms.topic: article
ms.date: 05/31/2018
---

# ADSI LDAP Provider

The ADSI LDAP Provider implements a set of ADSI objects that support various ADSI interfaces. To access the LDAP provider, bind to any of the ADSI LDAP objects, using the LDAP ADsPath.

You must have Adsldp.dll, Adsldpc.dll, Adsmsext.dll, and Activeds.dll installed on your client computer to work with the provider.

> [!Note]  
> The default ADSI LDAP provider cannot be assumed to be completely thread-safe. Writers of multithreaded applications should properly coordinate access between threads through the proper use of synchronization objects such as semaphores, mutexes, critical sections, and so on.

 

 

 




