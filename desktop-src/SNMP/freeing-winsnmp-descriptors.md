---
title: Freeing WinSNMP Descriptors
description: The WinSNMP programming environment assigns the deallocation of descriptor resources to the WinSNMP implementation or the WinSNMP application, depending on which component allocates the memory for the descriptor.
ms.assetid: 3e4cbbc5-18bc-4731-971c-6e533d904f56
ms.topic: article
ms.date: 05/31/2018
---

# Freeing WinSNMP Descriptors

The WinSNMP programming environment assigns the deallocation of descriptor resources to the WinSNMP implementation or the WinSNMP application, depending on which component allocates the memory for the descriptor.

To free the resources for an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) or an [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) descriptor, the following rules apply:

-   For input parameters

    Because the WinSNMP application allocates the memory for input objects with variable lengths, the application must free that memory using an appropriate function. For example, if the application allocated the resources with a call to the [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc) function, it should use the [**GlobalFree**](/windows/desktop/api/winbase/nf-winbase-globalfree) function to deallocate the resources. If the application allocated the resources with a call to the [**HeapAlloc**](/windows/desktop/api/heapapi/nf-heapapi-heapalloc) function, it should call the [**HeapFree**](/windows/desktop/api/heapapi/nf-heapapi-heapfree) function.

-   For output parameters

    A call to any of the following functions results in the implementation allocating memory for an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) or an [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) descriptor: [**SnmpGetVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetvb), [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg), [**SnmpOidCopy**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidcopy), [**SnmpContextToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcontexttostr), and [**SnmpStrToOid**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtooid).

    Because the implementation allocates the memory for these output objects, the application must call the [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor) function to deallocate the resources. This function enables the implementation to free the memory allocated for the **ptr** member of these structures.

To free the resources for an [**smiVALUE**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivalue) structure, a WinSNMP application must check the **syntax** member of an [**smiVALUE**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivalue) structure to correctly evaluate the **value** member of the structure. If the **syntax** member indicates that the **value** member is an [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) or an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) descriptor, and the implementation allocated the resources for the descriptor, the application must call [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor). This enables the implementation to free the memory. If the application allocated the resources, it must free the memory using an appropriate function, as indicated earlier.

For more information, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 