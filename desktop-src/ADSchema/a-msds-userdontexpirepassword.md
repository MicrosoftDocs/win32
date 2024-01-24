---
title: ms-DS-User-Dont-Expire-Password attribute
description: Indicates whether the password for the account this attribute references will expire.
ms.assetid: bafbcb4a-ee45-4f88-8fb2-93840efd1289
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Dont-Expire-Password attribute AD Schema
- msDS-UserDontExpirePassword attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Dont-Expire-Password
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-User-Dont-Expire-Password attribute

Indicates whether the password for the account this attribute references will expire. True if the password will not expire; otherwise, False.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-User-Dont-Expire-Password      |
| Ldap-Display-Name | msDS-UserDontExpirePassword          |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1855              |
| System-Id-Guid    | 8788193a-2925-43d9-a221-bb7fff397675 |
| Syntax            | [**Boolean**](s-boolean.md)         |



## Implementations

-   [**ADAM**](#adam)

## ADAM



| Entry | Value |
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
| System-Flags           | 0x00000010                                                        |
| Classes used in        | [**ms-DS-Bindable-Object**](c-msds-bindableobject.md)<br/> |



## Remarks

In ADAM, this attribute replaces the [**ADS\_UF\_DONT\_EXPIRE\_PASSWD**](/windows/desktop/api/iads/ne-iads-ads_user_flag_enum) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

