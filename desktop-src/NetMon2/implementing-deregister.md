---
description: Network Monitor passes all the frames of a capture to the parsers, and then starts calling the Deregister function for all the protocols it identifies. Each parser DLL must implement a Deregister function for each protocol that the parser DLL supports.
ms.assetid: 936d5b00-b0ee-4a29-9396-1e2a7a91a2dd
title: Implementing Deregister
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Deregister

Network Monitor passes all the frames of a capture to the parsers, and then starts calling the [**Deregister**](deregister.md) function for all the protocols it identifies. Each parser DLL must implement a **Deregister** function for each protocol that the parser DLL supports.

Each implementation of the [**Deregister**](deregister.md) function must call the [**DestroyProtocolDatabase**](destroypropertydatabase.md) function to release the resources that are used to create the database.

The following procedure identifies the one step necessary to implement [**Deregister**](deregister.md).

**To implement Deregister for one protocol**

-   Call [**DestroyProtocolDatabase**](destroypropertydatabase.md) to release the database resources.

The following is a basic implementation of [**Deregister**](deregister.md). Note that the code example shows the release of resources that are used to create a property database.

``` syntax
#include <windows.h>

VOID WINAPI MyProtocolDeregister (HPROTOCOL hProtocol)
{
  DestroyPropertyDatabase (hProtocol);
}
```

 

 



