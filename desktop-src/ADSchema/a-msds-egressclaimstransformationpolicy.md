---
title: ms-DS-Egress-Claims-Transformation-Policy attribute
description: This is a link to a Claims Transformation Policy Object for the egress claims (claims leaving this forest) to the Trusted Domain.
ms.assetid: 693ebb45-e90c-4629-8afc-f048c83b4b95
ms.tgt_platform: multiple
keywords:
- ms-DS-Egress-Claims-Transformation-Policy attribute AD Schema
- msDS-EgressClaimsTransformationPolicy attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Egress-Claims-Transformation-Policy
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Egress-Claims-Transformation-Policy attribute

This is a link to a Claims Transformation Policy Object for the egress claims (claims leaving this forest) to the Trusted Domain. This is applicable only for an incoming or bidirectional Cross-Forest Trust. When this link is not present, all claims are allowed to egress as-is.



| Entry | Value |
|-------------------|-------------------------------------------|
| CN                | ms-DS-Egress-Claims-Transformation-Policy |
| Ldap-Display-Name | msDS-EgressClaimsTransformationPolicy     |
| Size              | \-                                        |
| Update Privilege  | \-                                        |
| Update Frequency  | \-                                        |
| Attribute-Id      | 1.2.840.113556.1.4.2192                   |
| System-Id-Guid    | c137427e-9a73-b040-9190-1b095bb43288      |
| Syntax            | [**Object(DS-DN)**](s-object-ds-dn.md)   |



## Implementations

-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | 2192                                                 |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | \-                                                   |
| Range-Upper            | \-                                                   |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000010                                           |
| Classes used in        | [**Trusted-Domain**](c-trusteddomain.md)<br/> |



 

 





