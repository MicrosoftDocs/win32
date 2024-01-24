---
title: X509-Cert attribute
description: Contains the DER-encoded X.509v3 certificates issued to the user. Note that this property contains the public key certificates issued to this user by Microsoft Certificate Service.
ms.assetid: bdd6b9a4-c402-462c-be2c-8e7e582a899a
ms.tgt_platform: multiple
keywords:
- X509-Cert attribute AD Schema
- userCertificate attribute AD Schema
topic_type:
- apiref
api_name:
- X509-Cert
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# X509-Cert attribute

Contains the DER-encoded X.509v3 certificates issued to the user. Note that this property contains the public key certificates issued to this user by Microsoft Certificate Service.



| Entry | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------------|
| CN                | X509-Cert                                                                                                               |
| Ldap-Display-Name | userCertificate                                                                                                         |
| Size              | This attribute will require about 4 KB for each Key Recovery Agent certificate issued by the CA using the KRA instance. |
| Update Privilege  | Domain administrator                                                                                                    |
| Update Frequency  | Each time a certificate is issued.                                                                                      |
| Attribute-Id      | 2.5.4.36                                                                                                                |
| System-Id-Guid    | bf967a7f-0de6-11d0-a285-00aa003049e2                                                                                    |
| Syntax            | [**Object(Replica-Link)**](s-object-replica-link.md)                                                                   |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|----------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                     |
| MAPI-Id                | 0x8C6A                                                                                 |
| System-Only            | False                                                                                  |
| Is-Single-Valued       | False                                                                                  |
| Is Indexed             | False                                                                                  |
| In Global Catalog      | True                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                           |
| Range-Lower            | \-                                                                                     |
| Range-Upper            | \-                                                                                     |
| Search-Flags           | 0x00000000                                                                             |
| System-Flags           | 0x00000010                                                                             |
| Classes used in        | [**Mail-Recipient**](c-mailrecipient.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x8C6A                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                       |
| Range-Lower            | \-                                                                                                                                                                                                                                 |
| Range-Upper            | \-                                                                                                                                                                                                                                 |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                         |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> [**ms-PKI-Private-Key-Recovery-Agent**](c-mspki-privatekeyrecoveryagent.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x8C6A                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                       |
| Range-Lower            | \-                                                                                                                                                                                                                                 |
| Range-Upper            | \-                                                                                                                                                                                                                                 |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                         |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> [**ms-PKI-Private-Key-Recovery-Agent**](c-mspki-privatekeyrecoveryagent.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x8C6A                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                       |
| Range-Lower            | \-                                                                                                                                                                                                                                 |
| Range-Upper            | \-                                                                                                                                                                                                                                 |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                         |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> [**ms-PKI-Private-Key-Recovery-Agent**](c-mspki-privatekeyrecoveryagent.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x8C6A                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                       |
| Range-Lower            | \-                                                                                                                                                                                                                                 |
| Range-Upper            | \-                                                                                                                                                                                                                                 |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                         |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> [**ms-PKI-Private-Key-Recovery-Agent**](c-mspki-privatekeyrecoveryagent.md)<br/> [**User**](c-user.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                 |
| MAPI-Id                | 0x8C6A                                                                                                                                                                                                                             |
| System-Only            | False                                                                                                                                                                                                                              |
| Is-Single-Valued       | False                                                                                                                                                                                                                              |
| Is Indexed             | False                                                                                                                                                                                                                              |
| In Global Catalog      | True                                                                                                                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                       |
| Range-Lower            | \-                                                                                                                                                                                                                                 |
| Range-Upper            | \-                                                                                                                                                                                                                                 |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                         |
| System-Flags           | 0x00000010                                                                                                                                                                                                                         |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> [**ms-PKI-Private-Key-Recovery-Agent**](c-mspki-privatekeyrecoveryagent.md)<br/> [**User**](c-user.md)<br/> |



 

 





