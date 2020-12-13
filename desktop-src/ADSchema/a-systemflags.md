---
title: System-Flags attribute
description: An integer value that contains flags that define additional properties of the class.
ms.assetid: ce24322c-fb01-462a-aefe-cb422851f782
ms.tgt_platform: multiple
keywords:
- System-Flags attribute AD Schema
- systemFlags attribute AD Schema
topic_type:
- apiref
api_name:
- System-Flags
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# System-Flags attribute

An integer value that contains flags that define additional properties of the class. See Remarks.



| Entry | Value |
|-------------------|------------------------------------------------|
| CN                | System-Flags                                   |
| Ldap-Display-Name | systemFlags                                    |
| Size              | \-                                             |
| Update Privilege  | This value is set by the schema administrator. |
| Update Frequency  | Whenever the state of the object changes.      |
| Attribute-Id      | 1.2.840.113556.1.4.375                         |
| System-Id-Guid    | e0fa1e62-9b45-11d0-afdd-00c04fd930c9           |
| Syntax            | [**Enumeration**](s-enumeration.md)           |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Remarks

This attribute can be zero or a combination of one or more of the following values.



| Value                   | Description                                                                                                                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 (0x00000001)          | When applied to an attribute, the attribute will not be replicated.When applied to a [**Cross-Ref**](c-crossref.md) object, the naming context is in NTDS.<br/>                                                                                                                          |
| 2 (0x00000002)          | When applied to an attribute, the attribute will be replicated to the global catalog.When applied to a [**Cross-Ref**](c-crossref.md) object, the naming context is a domain.<br/>                                                                                                       |
| 4 (0x00000004)          | When applied to an attribute, the attribute is constructed.                                                                                                                                                                                                                                     |
| 16 (0x00000010)         | When set, indicates the object is a category 1 object. A category 1 object is a class or attribute that is included in the base schema included with the system.                                                                                                                                |
| 33554432 (0x02000000)   | The object is not moved to the Deleted Objects container when it is deleted. It will be deleted immediately.                                                                                                                                                                                    |
| 67108864 (0x04000000)   | The object cannot be moved.                                                                                                                                                                                                                                                                     |
| 134217728 (0x08000000)  | The object cannot be renamed.                                                                                                                                                                                                                                                                   |
| 268435456 (0x10000000)  | For objects in the configuration partition, if this flag is set, the object can be moved with restrictions; otherwise, the object cannot be moved. By default, this flag is not set on new objects created under the configuration partition. This flag can only be set during object creation. |
| 536870912 (0x20000000)  | For objects in the configuration partition, if this flag is set, the object can be moved; otherwise, the object cannot be moved. By default, this flag is not set on new objects created under the configuration partition. This flag can only be set during object creation.                   |
| 1073741824 (0x40000000) | For objects in the configuration partition, if this flag is set, the object can be renamed; otherwise, the object cannot be renamed. By default, this flag is not set on new objects created under the configuration partition. This flag can only be set during object creation.               |
| 2147483648 (0x80000000) | The object cannot be deleted.                                                                                                                                                                                                                                                                   |



 

 

 





