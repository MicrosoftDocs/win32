---
title: NT-Security-Descriptor attribute
description: The Windows NT security descriptor for the schema object. A security descriptor is a data structure that contains security information about an object, such as the ownership and permissions of the object.
ms.assetid: 3a17b584-97ea-441c-846e-3031aea171b2
ms.tgt_platform: multiple
keywords:
- NT-Security-Descriptor attribute AD Schema
- nTSecurityDescriptor attribute AD Schema
topic_type:
- apiref
api_name:
- NT-Security-Descriptor
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# NT-Security-Descriptor attribute

The Windows NT security descriptor for the schema object. A security descriptor is a data structure that contains security information about an object, such as the ownership and permissions of the object.

For information about the format this value, see [Security Descriptor String Format (Windows)](https://msdn.microsoft.com/library(d=robot)/aa379570(d=robot,l=en-us,v=vs.85).aspx).



| Entry | Value |
|-------------------|-----------------------------------------------------|
| CN                | NT-Security-Descriptor                              |
| Ldap-Display-Name | nTSecurityDescriptor                                |
| Size              | \-                                                  |
| Update Privilege  | \-                                                  |
| Update Frequency  | \-                                                  |
| Attribute-Id      | 1.2.840.113556.1.2.281                              |
| System-Id-Guid    | bf9679e3-0de6-11d0-a285-00aa003049e2                |
| Syntax            | [**String(NT-Sec-Desc)**](s-string-nt-sec-desc.md) |



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
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x00000012                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x0000001A                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                           |
| MAPI-Id                | 0x8013                                                                                       |
| System-Only            | False                                                                                        |
| Is-Single-Valued       | True                                                                                         |
| Is Indexed             | False                                                                                        |
| In Global Catalog      | True                                                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                 |
| Range-Lower            | 0                                                                                            |
| Range-Upper            | 132096                                                                                       |
| Search-Flags           | 0x00000008                                                                                   |
| System-Flags           | 0x0000001A                                                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x0000001A                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x0000001A                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x0000001A                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                 |
| MAPI-Id                | 0x8013                                                                                                                                             |
| System-Only            | False                                                                                                                                              |
| Is-Single-Valued       | True                                                                                                                                               |
| Is Indexed             | False                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                       |
| Range-Lower            | 0                                                                                                                                                  |
| Range-Upper            | 132096                                                                                                                                             |
| Search-Flags           | 0x00000008                                                                                                                                         |
| System-Flags           | 0x0000001A                                                                                                                                         |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |



 

 





