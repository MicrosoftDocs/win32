---
title: SAM-Account-Type attribute
description: This attribute contains information about every account type object.
ms.assetid: 00479b89-1d96-4ace-bbd8-053ca9e548b0
ms.tgt_platform: multiple
keywords:
- SAM-Account-Type attribute AD Schema
- sAMAccountType attribute AD Schema
topic_type:
- apiref
api_name:
- SAM-Account-Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SAM-Account-Type attribute

This attribute contains information about every account type object. You can enumerate a list of account types or you can use the Display Information API to create a list. Because computers, normal user accounts, and trust accounts can also be enumerated as user objects, the values for these accounts must be a contiguous range.

The possible values for this attribute are the following:

-   SAM\_DOMAIN\_OBJECT 0x0
-   SAM\_GROUP\_OBJECT 0x10000000
-   SAM\_NON\_SECURITY\_GROUP\_OBJECT 0x10000001
-   SAM\_ALIAS\_OBJECT 0x20000000
-   SAM\_NON\_SECURITY\_ALIAS\_OBJECT 0x20000001
-   SAM\_USER\_OBJECT 0x30000000
-   SAM\_NORMAL\_USER\_ACCOUNT 0x30000000
-   SAM\_MACHINE\_ACCOUNT 0x30000001
-   SAM\_TRUST\_ACCOUNT 0x30000002
-   SAM\_APP\_BASIC\_GROUP 0x40000000
-   SAM\_APP\_QUERY\_GROUP 0x40000001
-   SAM\_ACCOUNT\_TYPE\_MAX 0x7fffffff



| Entry | Value |
|-------------------|-----------------------------------------------------------------|
| CN                | SAM-Account-Type                                                |
| Ldap-Display-Name | sAMAccountType                                                  |
| Size              | \-                                                              |
| Update Privilege  | This value is set by the system.                                |
| Update Frequency  | This is set by the operating system when the object is created. |
| Attribute-Id      | 1.2.840.113556.1.4.302                                          |
| System-Id-Guid    | 6e7b626c-64f2-11d0-afd2-00c04fd930c9                            |
| Syntax            | [**Enumeration**](s-enumeration.md)                            |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



 

 





