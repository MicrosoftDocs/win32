---
title: Working with Variable Binding Lists
description: A variable binding is the pairing of an SNMP object instance name with an associated value. A variable binding list is a series of variable binding entries. In WinSNMP, a protocol data unit (PDU) includes a variable binding list.
ms.assetid: e6353ae7-1d32-4de4-8518-49864fcbfc57
keywords:
- Working with Variable Binding Lists SNMP
- Variable Binding Lists SNMP , SNMP
ms.topic: article
ms.date: 05/31/2018
---

# Working with Variable Binding Lists

A *variable binding* is the pairing of an SNMP object instance name with an associated value. A *variable binding list* is a series of variable binding entries. In WinSNMP, a protocol data unit (PDU) includes a variable binding list.

The details of the variable binding list structure are restricted to the Microsoft WinSNMP implementation. A WinSNMP application can access a variable binding list with a handle of type **HSNMP\_VBL**. For more information, see [Resource Handle Objects](resource-handle-objects.md).

The WinSNMP application can construct and manipulate variable binding lists, and include them in PDUs. To perform these operations, the application uses the WinSNMP [variable binding functions](winsnmp-functions.md). For more information about working with WinSNMP and variable binding lists, see the topics listed in the following table.



| Topic                                                                    | Description                                      |
|--------------------------------------------------------------------------|--------------------------------------------------|
| [Creating a Variable Binding List](creating-a-variable-binding-list.md) | Describes how to create a variable binding list. |
| [Managing a Variable Binding List](managing-a-variable-binding-list.md) | Describes how to manage a variable binding list. |



 

For more information about variable bindings and variable binding lists, see [RFC1905](https://www.ietf.org/rfc/rfc1905.txt), "Protocol Operations for Version 2 of the Simple Network Management Protocol (SNMPv2)," and the WinSNMP [Variable Binding Functions](winsnmp-functions.md).

 

 




