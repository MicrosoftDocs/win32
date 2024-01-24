---
title: ms-DS-Supported-Encryption-Types attribute
description: The encryption algorithms supported by user, computer or trust accounts.Note The KDC uses this information while generating a service ticket for this account.
ms.assetid: 6f9055a9-531e-4f4b-8703-aca5531a3bcb
ms.tgt_platform: multiple
keywords:
- ms-DS-Supported-Encryption-Types attribute AD Schema
- msDS-SupportedEncryptionTypes attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Supported-Encryption-Types
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Supported-Encryption-Types attribute

The encryption algorithms supported by user, computer or trust accounts.

> [!Note]  
> The KDC uses this information while generating a service ticket for this account. Services and Computers can automatically update this attribute on their respective accounts in Active Directory, and therefore need write access to this attribute.

 



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-Supported-Encryption-Types     |
| Ldap-Display-Name | msDS-SupportedEncryptionTypes        |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1963              |
| System-Id-Guid    | 20119867-1d04-4ab7-9371-cfc3d5df0afd |
| Syntax            | [**Enumeration**](s-enumeration.md) |



## Implementations

-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2008



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                     |
| MAPI-Id                | \-                                                                                     |
| System-Only            | False                                                                                  |
| Is-Single-Valued       | True                                                                                   |
| Is Indexed             | False                                                                                  |
| In Global Catalog      | False                                                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                           |
| Range-Lower            | \-                                                                                     |
| Range-Upper            | \-                                                                                     |
| Search-Flags           | 0x00000000                                                                             |
| System-Flags           | 0x00000010                                                                             |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                     |
| MAPI-Id                | \-                                                                                     |
| System-Only            | False                                                                                  |
| Is-Single-Valued       | True                                                                                   |
| Is Indexed             | False                                                                                  |
| In Global Catalog      | False                                                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                           |
| Range-Lower            | \-                                                                                     |
| Range-Upper            | \-                                                                                     |
| Search-Flags           | 0x00000000                                                                             |
| System-Flags           | 0x00000010                                                                             |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                     |
| MAPI-Id                | \-                                                                                     |
| System-Only            | False                                                                                  |
| Is-Single-Valued       | True                                                                                   |
| Is Indexed             | False                                                                                  |
| In Global Catalog      | False                                                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                           |
| Range-Lower            | \-                                                                                     |
| Range-Upper            | \-                                                                                     |
| Search-Flags           | 0x00000000                                                                             |
| System-Flags           | 0x00000010                                                                             |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> [**User**](c-user.md)<br/> |



 

 





