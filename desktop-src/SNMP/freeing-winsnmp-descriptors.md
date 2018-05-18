---
title: Freeing WinSNMP Descriptors
description: The WinSNMP programming environment assigns the deallocation of descriptor resources to the WinSNMP implementation or the WinSNMP application, depending on which component allocates the memory for the descriptor.
ms.assetid: '3e4cbbc5-18bc-4731-971c-6e533d904f56'
---

# Freeing WinSNMP Descriptors

The WinSNMP programming environment assigns the deallocation of descriptor resources to the WinSNMP implementation or the WinSNMP application, depending on which component allocates the memory for the descriptor.

To free the resources for an [**smiOID**](smioid-str.md) or an [**smiOCTETS**](smioctets-str.md) descriptor, the following rules apply:

-   For input parameters

    Because the WinSNMP application allocates the memory for input objects with variable lengths, the application must free that memory using an appropriate function. For example, if the application allocated the resources with a call to the [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574) function, it should use the [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579) function to deallocate the resources. If the application allocated the resources with a call to the [**HeapAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366597) function, it should call the [**HeapFree**](https://msdn.microsoft.com/library/windows/desktop/aa366701) function.

-   For output parameters

    A call to any of the following functions results in the implementation allocating memory for an [**smiOID**](smioid-str.md) or an [**smiOCTETS**](smioctets-str.md) descriptor: [**SnmpGetVb**](snmpgetvb.md), [**SnmpEncodeMsg**](snmpencodemsg.md), [**SnmpOidCopy**](snmpoidcopy.md), [**SnmpContextToStr**](snmpcontexttostr.md), and [**SnmpStrToOid**](snmpstrtooid.md).

    Because the implementation allocates the memory for these output objects, the application must call the [**SnmpFreeDescriptor**](snmpfreedescriptor.md) function to deallocate the resources. This function enables the implementation to free the memory allocated for the **ptr** member of these structures.

To free the resources for an [**smiVALUE**](smivalue-str.md) structure, a WinSNMP application must check the **syntax** member of an [**smiVALUE**](smivalue-str.md) structure to correctly evaluate the **value** member of the structure. If the **syntax** member indicates that the **value** member is an [**smiOCTETS**](smioctets-str.md) or an [**smiOID**](smioid-str.md) descriptor, and the implementation allocated the resources for the descriptor, the application must call [**SnmpFreeDescriptor**](snmpfreedescriptor.md). This enables the implementation to free the memory. If the application allocated the resources, it must free the memory using an appropriate function, as indicated earlier.

For more information, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




