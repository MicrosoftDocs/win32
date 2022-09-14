---
title: Trust-Attributes attribute
description: This attribute stores the trust attributes for a trusted domain.
ms.assetid: c85b98a6-4d09-4eb2-821b-58ef558b3460
ms.tgt_platform: multiple
keywords:
- Trust-Attributes attribute AD Schema
- trustAttributes attribute AD Schema
topic_type:
- apiref
api_name:
- Trust-Attributes
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Trust-Attributes attribute

This attribute stores the trust attributes for a trusted domain. Possible attribute values are as follows:

-   TRUST\_ATTRIBUTE\_NON\_TRANSITIVE Disable transitivity.
-   TRUST\_ATTRIBUTE\_TREE\_PARENT Trust is set to the organization tree parent.
-   TRUST\_ATTRIBUTE\_TREE\_ROOT Trust set to another tree root in the forest.
-   TRUST\_ATTRIBUTE\_UPLEVEL\_ONLY Trusted link valid only for uplevel client.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Trust-Attributes                     |
| Ldap-Display-Name | trustAttributes                      |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.470               |
| System-Id-Guid    | 80a67e5a-9f22-11d0-afdd-00c04fd930c9 |
| Syntax            | [**Enumeration**](s-enumeration.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | True                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | True                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | True                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | True                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | True                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



 

 





