---
title: Resource Handle Objects
description: The structure of a resource object is restricted to the Microsoft WinSNMP implementation. A WinSNMP application can access a resource object with a handle.
ms.assetid: c70a03b1-afac-4f1a-81e7-7f31430f5655
ms.topic: article
ms.date: 05/31/2018
---

# Resource Handle Objects

The structure of a resource object is restricted to the Microsoft WinSNMP implementation. A WinSNMP application can access a resource object with a handle.

The implementation can allocate one of the following types of resource handles for a WinSNMP application.

| Handle type        | Description                       |
|--------------------|-----------------------------------|
| **HSNMP\_SESSION** | Handle to a WinSNMP session       |
| **HSNMP\_ENTITY**  | Handle to an SNMP entity          |
| **HSNMP\_CONTEXT** | Handle to a WinSNMP context       |
| **HSNMP\_PDU**     | Handle to a protocol data unit    |
| **HSNMP\_VBL**     | Handle to a variable binding list |



 

A WinSNMP application can request that the implementation create or delete resource handles, but the implementation performs the operation. For additional information about freeing individual resources, see the [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor), [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl), [**SnmpFreePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreepdu), [**SnmpFreeEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreeentity), and [**SnmpFreeContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreecontext) functions.

 

 




