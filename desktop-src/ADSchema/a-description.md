---
title: Description attribute (AD Schema)
description: Contains the description to display for an object. This value is restricted as single-valued for backward compatibility in some cases but is allowed to be multi-valued in others. See Remarks.
ms.assetid: 97dad871-5db0-4d1e-b931-1b053559f9c2
ms.tgt_platform: multiple
keywords:
- Description attribute AD Schema
- description attribute AD Schema
topic_type:
- apiref
api_name:
- Description
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Description attribute (AD Schema)

Contains the description to display for an object. This value is restricted as single-valued for backward compatibility in some cases but is allowed to be multi-valued in others. See Remarks.



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | Description                                 |
| Ldap-Display-Name | description                                 |
| Size              | \-                                          |
| Update Privilege  | Domain administrator or account owner.      |
| Update Frequency  | Whenever the description needs to change.   |
| Attribute-Id      | 2.5.4.13                                    |
| System-Id-Guid    | bf967950-0de6-11d0-a285-00aa003049e2        |
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



| Entry | Value |
|------------------------|------------------------------------------------------------------------------|
| Link-Id                | \-                                                                           |
| MAPI-Id                | 0x806F                                                                       |
| System-Only            | False                                                                        |
| Is-Single-Valued       | False                                                                        |
| Is Indexed             | False                                                                        |
| In Global Catalog      | True                                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                 |
| Range-Lower            | 0                                                                            |
| Range-Upper            | 1024                                                                         |
| Search-Flags           | 0x00000000                                                                   |
| System-Flags           | 0x00000010                                                                   |
| Classes used in        | [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                         |
| MAPI-Id                | 0x806F                                                                                                                                     |
| System-Only            | False                                                                                                                                      |
| Is-Single-Valued       | False                                                                                                                                      |
| Is Indexed             | False                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                               |
| Range-Lower            | 0                                                                                                                                          |
| Range-Upper            | 1024                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                 |
| Classes used in        | [**groupOfUniqueNames**](c-groupofuniquenames.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | 0x806F                          |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 0                               |
| Range-Upper            | 1024                            |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x806F                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Range-Upper            | 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Classes used in        | [**groupOfUniqueNames**](c-groupofuniquenames.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**ipService**](c-ipservice.md)<br/> [**ipProtocol**](c-ipprotocol.md)<br/> [**oncRpc**](c-oncrpc.md)<br/> [**ipHost**](c-iphost.md)<br/> [**ipNetwork**](c-ipnetwork.md)<br/> [**nisNetgroup**](c-nisnetgroup.md)<br/> [**nisMap**](c-nismap.md)<br/> [**nisObject**](c-nisobject.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x806F                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Range-Upper            | 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Classes used in        | [**groupOfUniqueNames**](c-groupofuniquenames.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**ipService**](c-ipservice.md)<br/> [**ipProtocol**](c-ipprotocol.md)<br/> [**oncRpc**](c-oncrpc.md)<br/> [**ipHost**](c-iphost.md)<br/> [**ipNetwork**](c-ipnetwork.md)<br/> [**nisNetgroup**](c-nisnetgroup.md)<br/> [**nisMap**](c-nismap.md)<br/> [**nisObject**](c-nisobject.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x806F                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Range-Upper            | 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Classes used in        | [**groupOfUniqueNames**](c-groupofuniquenames.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**ipService**](c-ipservice.md)<br/> [**ipProtocol**](c-ipprotocol.md)<br/> [**oncRpc**](c-oncrpc.md)<br/> [**ipHost**](c-iphost.md)<br/> [**ipNetwork**](c-ipnetwork.md)<br/> [**nisNetgroup**](c-nisnetgroup.md)<br/> [**nisMap**](c-nismap.md)<br/> [**nisObject**](c-nisobject.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x806F                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Range-Upper            | 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Classes used in        | [**groupOfUniqueNames**](c-groupofuniquenames.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Top**](c-top.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**ipService**](c-ipservice.md)<br/> [**ipProtocol**](c-ipprotocol.md)<br/> [**oncRpc**](c-oncrpc.md)<br/> [**ipHost**](c-iphost.md)<br/> [**ipNetwork**](c-ipnetwork.md)<br/> [**nisNetgroup**](c-nisnetgroup.md)<br/> [**nisMap**](c-nismap.md)<br/> [**nisObject**](c-nisobject.md)<br/> |



## Remarks

The description attribute is implemented as a multi-valued attribute in the schema for the cases where that is allowed. For an object that is not a SAM managed class, the description is multi-valued. For an attribute that is a SAM managed class, the description attribute is single-valued. SAM managed classes are for things like security principals so, if you have, for example, a container, or a class of your own, the schema will let you use multiple values. This behavior of the description attribute is for backward compatibility with earlier operating systems because the attribute existed in the SAM APIs before AD existed.

 

 





