---
title: Object Identifiers (SNMP)
description: An SNMP object identifier uniquely names an object and identifies its location within a Management Information Base (MIB) tree structure.
ms.assetid: 'b4552185-ef37-4e04-9b19-a226165e0b32'
ms.topic: article
ms.date: 05/31/2018
---

# Object Identifiers (SNMP)

An SNMP object identifier uniquely names an object and identifies its location within a Management Information Base (MIB) tree structure. Object identifiers are application-independent Abstract Syntax Notation One (ASN.1) data types that consist of a sequence of non-negative integers, or subidentifiers. Object identifiers must have a minimum of two subidentifiers and they must not exceed 128 subidentifiers.

The WinSNMP programming environment uses the [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) structure to manage object identifiers. The format of the object identifier array in an **smiOID** structure is one subidentifier per array element.

The dotted numeric string representation of an object identifier separates its subidentifiers with periods; for example, "1.2.3.4.5.6".

For more information, see [The SNMP Management Information Base (MIB)](the-snmp-management-information-base-mib-.md) and the relevant RFCs.

 

 




