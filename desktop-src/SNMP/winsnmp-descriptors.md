---
title: WinSNMP Descriptors
description: In the WinSNMP programming environment a descriptor is one of the following two structures.
ms.assetid: 'a329963b-cdb9-40d2-9a82-6f0d9f4ac73a'
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Descriptors

In the WinSNMP programming environment a *descriptor* is one of the following two structures:

-   An [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) structure which describes an octet string variable
-   An [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) structure which describes an SNMP object identifier variable

A WinSNMP descriptor is a structure that has two members: a length member, **len**, and a pointer member, **ptr**. The **ptr** member points to the octet string or object identifier of interest. The **ptr** member can be either the **smiLPBYTE** or **smiLPUINT32** data type.

An [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) descriptor or an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) descriptor can be the **value** member of an **smiVALUE** structure. The [**smiVALUE**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivalue) structure describes the value associated with a variable name in a variable binding entry.

The Microsoft WinSNMP implementation allocates and deallocates memory for all output **smiOCTETS** and **smiOID** structures. Therefore, the application must call the [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor) function to free the memory for the **ptr** member of these structures.

String members in descriptors do not require a **NULL** terminating byte. For additional information about managing the memory allocated for descriptors, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




