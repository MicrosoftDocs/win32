---
title: ms-DS-User-Account-Disabled attribute
description: Indicates whether an account is disabled or enabled.
ms.assetid: 5d6ced7b-ca0f-4afa-b394-e61e80454f3d
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Account-Disabled attribute AD Schema
- msDS-UserAccountDisabled attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Account-Disabled
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-User-Account-Disabled attribute

Indicates whether an account is disabled or enabled. True if the account disabled; otherwise, False.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-User-Account-Disabled          |
| Ldap-Display-Name | msDS-UserAccountDisabled             |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1853              |
| System-Id-Guid    | 7c708658-7372-4211-b22b-13a45ffd1d61 |
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

In ADAM, this attribute replaces the [**ADS\_UF\_ACCOUNTDISABLE**](/windows/desktop/api/iads/ne-iads-ads_user_flag_enum) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

