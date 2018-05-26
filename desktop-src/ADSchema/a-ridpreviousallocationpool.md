---
title: RID-Previous-Allocation-Pool attribute
description: Contains the pool of relative identifiers (RIDs) that a domain controller allocates from.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d2f60259-388b-4dea-a1f7-9e650b1a66db
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- RID-Previous-Allocation-Pool attribute AD Schema
- rIDPreviousAllocationPool attribute AD Schema
topic_type:
- apiref
api_name:
- RID-Previous-Allocation-Pool
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RID-Previous-Allocation-Pool attribute

The **RID-Previous-Allocation-Pool** attribute contains the pool of relative identifiers (RIDs) that a domain controller allocates from. This attribute is an eight-byte value that contains a pair of four-byte integers that represent the start and end values of the RID pool. The start value is in the lower four bytes and the end value is in the upper four bytes.



|                   |                                      |
|-------------------|--------------------------------------|
| CN                | RID-Previous-Allocation-Pool         |
| Ldap-Display-Name | rIDPreviousAllocationPool            |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.372               |
| System-Id-Guid    | 6617188a-8f3c-11d0-afda-00c04fd930c9 |
| Syntax            | [**Interval**](s-interval.md)       |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



## Windows Server 2003



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



## Windows Server 2003 R2



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



## Windows Server 2008



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



## Windows Server 2008 R2



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



## Windows Server 2012



|                        |                                        |
|------------------------|----------------------------------------|
| Link-Id                | \-                                     |
| MAPI-Id                | \-                                     |
| System-Only            | True                                   |
| Is-Single-Valued       | True                                   |
| Is Indexed             | False                                  |
| In Global Catalog      | False                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                           |
| Range-Lower            | \-                                     |
| Range-Upper            | \-                                     |
| Search-Flags           | 0x00000000                             |
| System-Flags           | 0x00000011                             |
| Classes used in        | [**RID-Set**](c-ridset.md)<br/> |



 

 





