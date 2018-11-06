---
title: Allocating WinSNMP Memory Objects
description: Descriptors, resource handles and C-style strings are the three types of memory objects in the WinSNMP programming environment.
ms.assetid: 7f51f02b-7c9f-4aa0-b0cf-83551a312e83
ms.topic: article
ms.date: 05/31/2018
---

# Allocating WinSNMP Memory Objects

Descriptors, resource handles and C-style strings are the three types of memory objects in the WinSNMP programming environment.

The type of object determines whether the Microsoft WinSNMP implementation or the WinSNMP application allocates and deallocates the memory for the object. This reduces unnecessary allocation of temporary buffer space and unnecessary copying of buffers.

The following table summarizes the allocation and deallocation of resources for WinSNMP memory objects.



| Object type                                                                   | Description                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) or [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) descriptor | If the WinSNMP application allocates the memory, it must deallocate the memory with a call to an appropriate function. If the implementation allocates the memory, the application must call the [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor) function to deallocate the memory. |
| [**smiVALUE**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivalue) structure                                    | If the **value** member is an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) or an [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) descriptor, the application must proceed as indicated above for descriptors.                                                                                                     |
| Resource handle                                                               | The implementation allocates, manages, and frees the memory.                                                                                                                                                                                                                         |
| C-style string                                                                | The WinSNMP application must manage and free the memory it allocates.                                                                                                                                                                                                                |



 

For more information, see [Freeing WinSNMP Descriptors](freeing-winsnmp-descriptors.md).

 

 




