---
title: Managing Object Identifiers
description: The WinSNMP API provides several WinSNMP utility functions that simplify the manipulation of object identifiers for WinSNMP applications.
ms.assetid: 6ca5f5bc-aa49-4826-97a7-2ea4a882dc2d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Object Identifiers

The WinSNMP API provides several [WinSNMP utility functions](winsnmp-functions.md#winsnmp-utility-functions) that simplify the manipulation of object identifiers for WinSNMP applications.

The [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master) function converts the internal binary representation of an object identifier to its dotted numeric string format. When you call [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master), specify a string buffer of MAXOBJIDSTRSIZE length (1408 bytes) to ensure that the output buffer is large enough to hold the converted string. To convert an object identifier from the dotted numeric string format to its internal binary representation, call the [**SnmpStrToOid**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtooid?branch=master) function.

To copy an SNMP object identifier call the [**SnmpOidCopy**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcopy?branch=master) function. This function allocates any necessary memory for the new object identifier.

A WinSNMP application must call the [**SnmpFreeDescriptor**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreedescriptor?branch=master) function to free resources allocated for the **ptr** member of the [**smiOID**](/windows/win32/Winsnmp/ns-winsnmp-smioid?branch=master) structure specified by both the [**SnmpStrToOid**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtooid?branch=master) and the [**SnmpOidCopy**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcopy?branch=master) functions.

The [**SnmpOidCompare**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcompare?branch=master) function compares two SNMP object identifiers. The WinSNMP application can specify the number of subidentifiers to compare. Call **SnmpOidCompare** to determine whether two object identifiers have common prefixes.

For additional information about managing the memory allocated for object identifiers, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




