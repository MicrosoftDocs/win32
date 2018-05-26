---
title: WinSNMP Descriptors
description: In the WinSNMP programming environment a descriptor is one of the following two structures.
ms.assetid: 3e4cbbc5-18bc-4731-971c-6e533d904f56
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinSNMP Descriptors

In the WinSNMP programming environment a *descriptor* is one of the following two structures:

-   An [**smiOCTETS**](/windows/win32/Winsnmp/ns-winsnmp-smioctets?branch=master) structure which describes an octet string variable
-   An [**smiOID**](/windows/win32/Winsnmp/ns-winsnmp-smioid?branch=master) structure which describes an SNMP object identifier variable

A WinSNMP descriptor is a structure that has two members: a length member, **len**, and a pointer member, **ptr**. The **ptr** member points to the octet string or object identifier of interest. The **ptr** member can be either the **smiLPBYTE** or **smiLPUINT32** data type.

An [**smiOCTETS**](/windows/win32/Winsnmp/ns-winsnmp-smioctets?branch=master) descriptor or an [**smiOID**](/windows/win32/Winsnmp/ns-winsnmp-smioid?branch=master) descriptor can be the **value** member of an **smiVALUE** structure. The [**smiVALUE**](/windows/win32/Winsnmp/ns-winsnmp-smivalue?branch=master) structure describes the value associated with a variable name in a variable binding entry.

The Microsoft WinSNMP implementation allocates and deallocates memory for all output **smiOCTETS** and **smiOID** structures. Therefore, the application must call the [**SnmpFreeDescriptor**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreedescriptor?branch=master) function to free the memory for the **ptr** member of these structures.

String members in descriptors do not require a **NULL** terminating byte. For additional information about managing the memory allocated for descriptors, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




