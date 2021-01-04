---
title: UNC-Name attribute
description: The universal naming convention name for shared volumes and printers.
ms.assetid: 967fd0dc-10af-4482-bc2c-1d1dc13dee39
ms.tgt_platform: multiple
keywords:
- UNC-Name attribute AD Schema
- uNCName attribute AD Schema
topic_type:
- apiref
api_name:
- UNC-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# UNC-Name attribute

The universal naming convention name for shared volumes and printers.



| Entry | Value |
|-------------------|-----------------------------------------------|
| CN                | UNC-Name                                      |
| Ldap-Display-Name | uNCName                                       |
| Size              | \-                                            |
| Update Privilege  | Domain administrator                          |
| Update Frequency  | When new volumes or print queues are created. |
| Attribute-Id      | 1.2.840.113556.1.4.137                        |
| System-Id-Guid    | bf967a64-0de6-11d0-a285-00aa003049e2          |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)   |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                   |
| System-Only            | False                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                         |
| Range-Lower            | \-                                                                                                                                                   |
| Range-Upper            | \-                                                                                                                                                   |
| Search-Flags           | 0x00000001                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                           |
| Classes used in        | [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                        |
| MAPI-Id                | \-                                                                                                                                                                                        |
| System-Only            | False                                                                                                                                                                                     |
| Is-Single-Valued       | True                                                                                                                                                                                      |
| Is Indexed             | True                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                              |
| Range-Lower            | \-                                                                                                                                                                                        |
| Range-Upper            | \-                                                                                                                                                                                        |
| Search-Flags           | 0x00000001                                                                                                                                                                                |
| System-Flags           | 0x00000010                                                                                                                                                                                |
| Classes used in        | [**FT-Dfs**](c-ftdfs.md)<br/> [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                         |
| Range-Lower            | \-                                                                                                                                                                                                                                                                   |
| Range-Upper            | \-                                                                                                                                                                                                                                                                   |
| Search-Flags           | 0x00000001                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                           |
| Classes used in        | [**FT-Dfs**](c-ftdfs.md)<br/> [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**ms-Print-ConnectionPolicy**](c-msprint-connectionpolicy.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                         |
| Range-Lower            | \-                                                                                                                                                                                                                                                                   |
| Range-Upper            | \-                                                                                                                                                                                                                                                                   |
| Search-Flags           | 0x00000001                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                           |
| Classes used in        | [**FT-Dfs**](c-ftdfs.md)<br/> [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**ms-Print-ConnectionPolicy**](c-msprint-connectionpolicy.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                         |
| Range-Lower            | \-                                                                                                                                                                                                                                                                   |
| Range-Upper            | \-                                                                                                                                                                                                                                                                   |
| Search-Flags           | 0x00000001                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                           |
| Classes used in        | [**FT-Dfs**](c-ftdfs.md)<br/> [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**ms-Print-ConnectionPolicy**](c-msprint-connectionpolicy.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                         |
| Range-Lower            | \-                                                                                                                                                                                                                                                                   |
| Range-Upper            | \-                                                                                                                                                                                                                                                                   |
| Search-Flags           | 0x00000001                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                           |
| Classes used in        | [**FT-Dfs**](c-ftdfs.md)<br/> [**Index-Server-Catalog**](c-indexservercatalog.md)<br/> [**ms-Print-ConnectionPolicy**](c-msprint-connectionpolicy.md)<br/> [**Print-Queue**](c-printqueue.md)<br/> [**Volume**](c-volume.md)<br/> |



 

 





