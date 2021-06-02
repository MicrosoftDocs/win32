---
title: Repl-Interval attribute
description: The attribute of Site-Link objects that defines the interval, in minutes, between replication cycles between the sites in the Site-List.
ms.assetid: ef4cbf75-7283-4930-9f98-1ffd6eb05669
ms.tgt_platform: multiple
keywords:
- Repl-Interval attribute AD Schema
- replInterval attribute AD Schema
topic_type:
- apiref
api_name:
- Repl-Interval
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Repl-Interval attribute

The attribute of Site-Link objects that defines the interval, in minutes, between replication cycles between the sites in the Site-List. Must be a multiple of 15 minutes (the granularity of cross-site DS replication), a minimum of 15 minutes, and a maximum of 10,080 minutes (one week).



| Entry | Value |
|-------------------|------------------------------------------------|
| CN                | Repl-Interval                                  |
| Ldap-Display-Name | replInterval                                   |
| Size              | 4 bytes                                        |
| Update Privilege  | Enterprise administrator                       |
| Update Frequency  | When the replication interval needs to change. |
| Attribute-Id      | 1.2.840.113556.1.4.1336                        |
| System-Id-Guid    | 45ba9d1a-56fa-11d2-90d0-00c04fd91ab1           |
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
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                         |
| MAPI-Id                | \-                                                                                                         |
| System-Only            | False                                                                                                      |
| Is-Single-Valued       | True                                                                                                       |
| Is Indexed             | False                                                                                                      |
| In Global Catalog      | False                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                               |
| Range-Lower            | \-                                                                                                         |
| Range-Upper            | \-                                                                                                         |
| Search-Flags           | 0x00000000                                                                                                 |
| System-Flags           | 0x00000010                                                                                                 |
| Classes used in        | [**Inter-Site-Transport**](c-intersitetransport.md)<br/> [**Site-Link**](c-sitelink.md)<br/> |



 

 





