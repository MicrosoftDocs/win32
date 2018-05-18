---
title: Managing Object Identifiers
description: The WinSNMP API provides several WinSNMP utility functions that simplify the manipulation of object identifiers for WinSNMP applications.
ms.assetid: '6ca5f5bc-aa49-4826-97a7-2ea4a882dc2d'
---

# Managing Object Identifiers

The WinSNMP API provides several [WinSNMP utility functions](winsnmp-functions.md#winsnmp-utility-functions) that simplify the manipulation of object identifiers for WinSNMP applications.

The [**SnmpOidToStr**](snmpoidtostr.md) function converts the internal binary representation of an object identifier to its dotted numeric string format. When you call [**SnmpOidToStr**](snmpoidtostr.md), specify a string buffer of MAXOBJIDSTRSIZE length (1408 bytes) to ensure that the output buffer is large enough to hold the converted string. To convert an object identifier from the dotted numeric string format to its internal binary representation, call the [**SnmpStrToOid**](snmpstrtooid.md) function.

To copy an SNMP object identifier call the [**SnmpOidCopy**](snmpoidcopy.md) function. This function allocates any necessary memory for the new object identifier.

A WinSNMP application must call the [**SnmpFreeDescriptor**](snmpfreedescriptor.md) function to free resources allocated for the **ptr** member of the [**smiOID**](smioid-str.md) structure specified by both the [**SnmpStrToOid**](snmpstrtooid.md) and the [**SnmpOidCopy**](snmpoidcopy.md) functions.

The [**SnmpOidCompare**](snmpoidcompare.md) function compares two SNMP object identifiers. The WinSNMP application can specify the number of subidentifiers to compare. Call **SnmpOidCompare** to determine whether two object identifiers have common prefixes.

For additional information about managing the memory allocated for object identifiers, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




