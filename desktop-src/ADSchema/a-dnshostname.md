---
title: DNS-Host-Name attribute
description: Name of computer as registered in DNS.
ms.assetid: ba655adb-cb70-47f2-820f-c5b0749d3e70
ms.tgt_platform: multiple
keywords:
- DNS-Host-Name attribute AD Schema
- dNSHostName attribute AD Schema
topic_type:
- apiref
api_name:
- DNS-Host-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# DNS-Host-Name attribute

Name of computer as registered in DNS.



| Entry | Value |
|-------------------|-----------------------------------------------------------------------------|
| CN                | DNS-Host-Name                                                               |
| Ldap-Display-Name | dNSHostName                                                                 |
| Size              | Each segment can be 63 characters. The entire length can be 255 characters. |
| Update Privilege  | Domain administrator                                                        |
| Update Frequency  | When the computer is named.                                                 |
| Attribute-Id      | 1.2.840.113556.1.4.619                                                      |
| System-Id-Guid    | 72e39547-7b18-11d1-adef-00c04fd8d5cd                                        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                 |



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
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------------|
| Link-Id                | \-                                    |
| MAPI-Id                | \-                                    |
| System-Only            | False                                 |
| Is-Single-Valued       | True                                  |
| Is Indexed             | False                                 |
| In Global Catalog      | True                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                          |
| Range-Lower            | 0                                     |
| Range-Upper            | 2048                                  |
| Search-Flags           | 0x00000000                            |
| System-Flags           | 0x00000010                            |
| Classes used in        | [**Server**](c-server.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                         |
| MAPI-Id                | \-                                                                                                                                                                                                                         |
| System-Only            | False                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                       |
| Is Indexed             | False                                                                                                                                                                                                                      |
| In Global Catalog      | True                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                          |
| Range-Upper            | 2048                                                                                                                                                                                                                       |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                 |
| System-Flags           | 0x00000010                                                                                                                                                                                                                 |
| Classes used in        | [**Certification-Authority**](c-certificationauthority.md)<br/> [**Computer**](c-computer.md)<br/> [**PKI-Enrollment-Service**](c-pkienrollmentservice.md)<br/> [**Server**](c-server.md)<br/> |



 

 





