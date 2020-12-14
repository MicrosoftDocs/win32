---
title: ms-DS-User-Password-Not-Required attribute
description: Indicates whether a password is required for the account that this attribute references.
ms.assetid: 86779c6f-d05c-409a-afe4-99ebf7c0593e
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Password-Not-Required attribute AD Schema
- ms-DS-UserPasswordNotRequired attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Password-Not-Required
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-User-Password-Not-Required attribute

Indicates whether a password is required for the account that this attribute references. True if a password is not required; otherwise, False.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-User-Password-Not-Required     |
| Ldap-Display-Name | ms-DS-UserPasswordNotRequired        |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1854              |
| System-Id-Guid    | 8f066172-a25e-4f53-8dcd-0a67d5fb883d |
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

In ADAM, this attribute replaces the [**ADS\_UF\_PASSWD\_NOTREQD**](/windows/desktop/api/iads/ne-iads-ads_user_flag_enum) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

