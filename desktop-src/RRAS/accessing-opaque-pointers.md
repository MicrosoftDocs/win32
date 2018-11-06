---
title: Accessing Opaque Pointers
description: Clients are able to access the information stored in destinations by using opaque pointers.
ms.assetid: 1f6af84f-c6c9-4091-8e6b-2c773541ca97
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Opaque Pointers

Clients are able to access the information stored in destinations by using opaque pointers. To use the storage, the client must first call [**RtmGetOpaqueInformationPointer**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetopaqueinformationpointer) to obtain the pointer. Whenever a change to the information is necessary, the client must first lock the destination by calling [**RtmLockDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlockdestination) with the *LockDest* parameter set to **TRUE**. Once the destination is locked, the client can make the necessary change. The destination can be unlocked using another call to **RtmLockDestination** with the *LockDest* parameter set to **FALSE**.

The [**RtmLockDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlockdestination) function also allows a client to use either a read lock or a write lock, using the *Exclusive* parameter. A client should use the write lock only when it is making changes to the information kept using the opaque pointer. Clients can use the read lock to view the opaque pointer information stored in a destination.

For sample code that shows how to use these functions, see [Access the Opaque Pointer in a Destination](access-the-opaque-pointer-in-a-destination.md).

 

 




