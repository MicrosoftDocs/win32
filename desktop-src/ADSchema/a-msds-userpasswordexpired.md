---
title: ms-DS-User-Password-Expired attribute
description: Indicates whether the password for the account that this attribute references has expired.
ms.assetid: cab4a2e8-b440-45d2-8da8-9f020ffee08c
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Password-Expired attribute AD Schema
- msDS-UserPasswordExpired attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Password-Expired
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-User-Password-Expired attribute

Indicates whether the password for the account that this attribute references has expired. True if the password has expired; otherwise, False.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-User-Password-Expired          |
| Ldap-Display-Name | msDS-UserPasswordExpired             |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1858              |
| System-Id-Guid    | 565c7ab5-e13e-47f6-abb5-de741806f125 |
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
| System-Flags           | 0x00000014                                                        |
| Classes used in        | [**ms-DS-Bindable-Object**](c-msds-bindableobject.md)<br/> |



## Remarks

In ADAM, this attribute replaces the [**ADS\_UF\_PASSWORD\_EXPIRED**](/windows/desktop/api/iads/ne-iads-ads_user_flag_enum) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

