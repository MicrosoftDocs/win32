---
title: ms-DS-User-Account-Auto-Locked attribute
description: Indicates whether the account that this attribute references has been locked out.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f9d9c98a-3c4f-4687-8133-4476aeec10e8
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Account-Auto-Locked attribute AD Schema
- ms-DS-UserAccountAutoLocked attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Account-Auto-Locked
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ms-DS-User-Account-Auto-Locked attribute

Indicates whether the account that this attribute references has been locked out. True if the account is locked out; otherwise, False.



|                   |                                      |
|-------------------|--------------------------------------|
| CN                | ms-DS-User-Account-Auto-Locked       |
| Ldap-Display-Name | ms-DS-UserAccountAutoLocked          |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1857              |
| System-Id-Guid    | f2dd7bab-1f3b-47cf-89fa-143b56ad0a3d |
| Syntax            | [**Boolean**](s-boolean.md)         |



## Implementations

-   [**ADAM**](#adam)

## ADAM



|                        |                                                                   |
|------------------------|-------------------------------------------------------------------|
| Link-Id                | \-                                                                |
| MAPI-Id                | \-                                                                |
| System-Only            | False                                                             |
| Is-Single-Valued       | True                                                              |
| Is Indexed             | False                                                             |
| In Global Catalog      | False                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                      |
| Range-Lower            | \-                                                                |
| Range-Upper            | \-                                                                |
| Search-Flags           | 0x00000000                                                        |
| System-Flags           | 0x00000014                                                        |
| Classes used in        | [**ms-DS-Bindable-Object**](c-msds-bindableobject.md)<br/> |



## Remarks

In ADAM, this attribute replaces the [**ADS\_UF\_LOCKOUT**](https://msdn.microsoft.com/library/aa772300) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

 





