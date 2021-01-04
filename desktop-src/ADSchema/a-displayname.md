---
title: Display-Name attribute
description: The display name for an object.
ms.assetid: 0ecf5ede-0351-4d59-bdbf-44baf729f2e2
ms.tgt_platform: multiple
keywords:
- Display-Name attribute AD Schema
- displayName attribute AD Schema
topic_type:
- apiref
api_name:
- Display-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Display-Name attribute

The display name for an object. This is usually the combination of the users first name, middle initial, and last name.



| Entry | Value |
|-------------------|------------------------------------------------------------------------------|
| CN                | Display-Name                                                                 |
| Ldap-Display-Name | displayName                                                                  |
| Size              | \-                                                                           |
| Update Privilege  | Domain administrator or account owner.                                       |
| Update Frequency  | When the user's record is created and when the display name needs to change. |
| Attribute-Id      | 1.2.840.113556.1.2.13                                                        |
| System-Id-Guid    | bf967953-0de6-11d0-a285-00aa003049e2                                         |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                  |



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
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                               |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                               |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                            |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                             |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                             |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                     |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                              |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                       |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                       |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                         |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                    |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                                                                                  |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                           |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**inetOrgPerson**](c-inetorgperson.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | True                            |
| Is Indexed             | True                            |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 0                               |
| Range-Upper            | 256                             |
| Search-Flags           | 0x00000005                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                         |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                    |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                                                                                  |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                           |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**inetOrgPerson**](c-inetorgperson.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                         |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                    |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                                                                                  |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                           |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**inetOrgPerson**](c-inetorgperson.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                         |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                    |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                                                                                  |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                           |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**inetOrgPerson**](c-inetorgperson.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAPI-Id                | \-                                                                                                                                                                                                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                                                |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| Is Indexed             | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| In Global Catalog      | True                                                                                                                                                                                                                                                                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                                         |
| Range-Lower            | 0                                                                                                                                                                                                                                                                                                                                                                                                    |
| Range-Upper            | 256                                                                                                                                                                                                                                                                                                                                                                                                  |
| Search-Flags           | 0x00000005                                                                                                                                                                                                                                                                                                                                                                                           |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                                           |
| Classes used in        | [**Address-Book-Container**](c-addressbookcontainer.md)<br/> [**Address-Template**](c-addresstemplate.md)<br/> [**inetOrgPerson**](c-inetorgperson.md)<br/> [**PKI-Certificate-Template**](c-pkicertificatetemplate.md)<br/> [**Service-Class**](c-serviceclass.md)<br/> [**Service-Instance**](c-serviceinstance.md)<br/> [**Top**](c-top.md)<br/> |



 

 





