---
title: ms-DNS-NSEC3-User-Salt attribute
description: An attribute that defines a user-specified NSEC3 salt string to use when signing the DNS zone. If empty, random salt will be used.
ms.assetid: b9829732-8a79-4f07-8644-9fe4ba05ba8f
ms.tgt_platform: multiple
keywords:
- ms-DNS-NSEC3-User-Salt attribute AD Schema
- msDNS-NSEC3UserSalt attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DNS-NSEC3-User-Salt
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DNS-NSEC3-User-Salt attribute

An attribute that defines a user-specified NSEC3 salt string to use when signing the DNS zone. If empty, random salt will be used.



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | ms-DNS-NSEC3-User-Salt                      |
| Ldap-Display-Name | msDNS-NSEC3UserSalt                         |
| Size              | \-                                          |
| Update Privilege  | \-                                          |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.2.840.113556.1.4.2148                     |
| System-Id-Guid    | aff16770-9622-4fbc-a128-3088777605b9        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | \-                                       |
| MAPI-Id                | \-                                       |
| System-Only            | False                                    |
| Is-Single-Valued       | True                                     |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 0                                        |
| Range-Upper            | 510                                      |
| Search-Flags           | 0x00000008                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**Dns-Zone**](c-dnszone.md)<br/> |



 

 





