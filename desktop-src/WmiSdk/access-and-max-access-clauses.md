---
description: Each MIB object definition contains either an ACCESS (SNMPv1) or MAX-ACCESS (SNMPv2C) clause that defines the access rights to the object.
ms.assetid: c3b8d65b-c1ca-4131-baf4-1aab54451180
ms.tgt_platform: multiple
title: ACCESS and MAX-ACCESS Clauses
ms.topic: article
ms.date: 05/31/2018
---

# ACCESS and MAX-ACCESS Clauses

Each MIB object definition contains either an ACCESS (SNMPv1) or MAX-ACCESS (SNMPv2C) clause that defines the access rights to the object.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The following table lists the mapping of the SNMPv1 ACCESS clause.



| MIB ACCESS clause | CIM qualifier       |
|-------------------|---------------------|
| read-only         | **Read**            |
| read-write        | **Read**, **Write** |
| write-only        | **Write**           |
| not-accessible    | **Not\_Accessible** |



 

The following table lists the mapping of the SNMPv2C MAX-ACCESS clause.



| MIB-ACCESS clause     | CIM qualifier       |
|-----------------------|---------------------|
| read-only             | **Read**            |
| read-write            | **Read**, **Write** |
| read-create           | **Read**            |
| accessible-for-notify | **Not\_Accessible** |
| not-accessible        | **Not\_Accessible** |



 

When a MIB object maps to not-accessible and is not a keyed property of the class, there is no mapping of the MIB object itself.

 

 



