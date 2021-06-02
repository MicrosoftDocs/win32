---
title: Instance-Type attribute
description: A bitfield that dictates how the object is instantiated on a particular server.
ms.assetid: ed77c302-3d80-4292-8e48-bfc6cb5079ee
ms.tgt_platform: multiple
keywords:
- Instance-Type attribute AD Schema
- instanceType attribute AD Schema
topic_type:
- apiref
api_name:
- Instance-Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Instance-Type attribute

A bitfield that dictates how the object is instantiated on a particular server. The value of this attribute can differ on different replicas even if the replicas are in sync.

This attribute can be zero or a combination of one or more of the following values.

| Value      | Description                                                                                        |
|------------|----------------------------------------------------------------------------------------------------|
| 0x00000001 | The head of naming context.                                                                        |
| 0x00000002 | This replica is not instantiated.                                                                  |
| 0x00000004 | The object is writable on this directory.                                                          |
| 0x00000008 | The naming context above this one on this directory is held.                                       |
| 0x00000010 | The naming context is in the process of being constructed for the first time by using replication. |
| 0x00000020 | The naming context is in the process of being removed from the local DSA.                          |



 



| Entry | Value |
|-------------------|------------------------------------------------|
| CN                | Instance-Type                                  |
| Ldap-Display-Name | instanceType                                   |
| Size              | 4 bytes.                                       |
| Update Privilege  | This value is set by the schema administrator. |
| Update Frequency  | When the object is created.                    |
| Attribute-Id      | 1.2.840.113556.1.2.1                           |
| System-Id-Guid    | bf96798c-0de6-11d0-a285-00aa003049e2           |
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
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x80BD                          |
| System-Only            | True                            |
| Is-Single-Valued       | True                            |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000008                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



 

 





