---
title: Domain-Component attribute
description: The naming attribute for Domain and DNS objects. Usually displayed as dc DomainName.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1d674af1-ed2f-4266-9704-8c6ed5a9bdd8
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- Domain-Component attribute AD Schema
- dc attribute AD Schema
topic_type:
- apiref
api_name:
- Domain-Component
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Domain-Component attribute

The naming attribute for Domain and DNS objects. Usually displayed as dc=DomainName.



|                   |                                             |
|-------------------|---------------------------------------------|
| CN                | Domain-Component                            |
| Ldap-Display-Name | dc                                          |
| Size              | \-                                          |
| Update Privilege  | Domain administrator                        |
| Update Frequency  | When the domain is created.                 |
| Attribute-Id      | 0.9.2342.19200300.100.1.25                  |
| System-Id-Guid    | 19195a55-6da0-11d0-afd3-00c04fd930c9        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



## Windows Server 2003



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



## ADAM



|                        |                                       |
|------------------------|---------------------------------------|
| Link-Id                | \-                                    |
| MAPI-Id                | \-                                    |
| System-Only            | False                                 |
| Is-Single-Valued       | True                                  |
| Is Indexed             | False                                 |
| In Global Catalog      | True                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                          |
| Range-Lower            | 1                                     |
| Range-Upper            | 255                                   |
| Search-Flags           | 0x00000000                            |
| System-Flags           | 0x00000012                            |
| Classes used in        | [**Domain**](c-domain.md)<br/> |



## Windows Server 2003 R2



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



## Windows Server 2008



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



## Windows Server 2008 R2



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



## Windows Server 2012



|                        |                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                      |
| MAPI-Id                | \-                                                                                                                      |
| System-Only            | False                                                                                                                   |
| Is-Single-Valued       | True                                                                                                                    |
| Is Indexed             | False                                                                                                                   |
| In Global Catalog      | True                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                            |
| Range-Lower            | 1                                                                                                                       |
| Range-Upper            | 255                                                                                                                     |
| Search-Flags           | 0x00000000                                                                                                              |
| System-Flags           | 0x00000012                                                                                                              |
| Classes used in        | [**Dns-Node**](c-dnsnode.md)<br/> [**Dns-Zone**](c-dnszone.md)<br/> [**Domain**](c-domain.md)<br/> |



 

 





