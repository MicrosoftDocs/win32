---
title: ms-DS-User-Encrypted-Text-Password-Allowed attribute
description: Indicates whether Active Directory will store the password in the reversible encryption format.
ms.assetid: 67067cf6-60e3-4626-bf8c-a0a1264a899e
ms.tgt_platform: multiple
keywords:
- ms-DS-User-Encrypted-Text-Password-Allowed attribute AD Schema
- ms-DS-UserEncryptedTextPasswordAllowed attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-User-Encrypted-Text-Password-Allowed
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-User-Encrypted-Text-Password-Allowed attribute

Indicates whether Active Directory will store the password in the reversible encryption format. True if the password is stored in the reversible encryption format; otherwise, False.

> [!Note]  
> This attribute is not used by [Active Directory Lightweight Directory Services](/previous-versions/windows/desktop/adam/active-directory-lightweight-directory-services) and is only included for completeness/parity with userAccountControl. AD LDS does not store passwords with reversible encryption, regardless of this attribute's value on any given object or the computer security policy pertaining to reversible encryption on the computer itself.

 



| Entry | Value |
|-------------------|--------------------------------------------|
| CN                | ms-DS-User-Encrypted-Text-Password-Allowed |
| Ldap-Display-Name | ms-DS-UserEncryptedTextPasswordAllowed     |
| Size              | \-                                         |
| Update Privilege  | \-                                         |
| Update Frequency  | \-                                         |
| Attribute-Id      | 1.2.840.113556.1.4.1856                    |
| System-Id-Guid    | 5a87c7f2-93c5-454c-a8c5-8cb09613292e       |
| Syntax            | [**Boolean**](s-boolean.md)               |



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

In ADAM, this attribute replaces the [**ADS\_UF\_ENCRYPTED\_TEXT\_PASSWORD\_ALLOWED**](/windows/desktop/api/iads/ne-iads-ads_user_flag_enum) flag of the [**userAccountControl**](a-useraccountcontrol.md) attribute.

 

