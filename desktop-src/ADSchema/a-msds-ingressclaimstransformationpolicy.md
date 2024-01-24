---
title: ms-DS-Ingress-Claims-Transformation-Policy attribute
description: This is a link to a Claims Transformation Policy Object for the ingress claims (claims entering this forest) from the Trusted Domain.
ms.assetid: 67f87782-85ed-41bb-a60d-f6c11fcda80e
ms.tgt_platform: multiple
keywords:
- ms-DS-Ingress-Claims-Transformation-Policy attribute AD Schema
- msDS-IngressClaimsTransformationPolicy attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Ingress-Claims-Transformation-Policy
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Ingress-Claims-Transformation-Policy attribute

This is a link to a Claims Transformation Policy Object for the ingress claims (claims entering this forest) from the Trusted Domain. This is applicable only for an outgoing or bidirectional Cross-Forest Trust. If this link is absent, all the ingress claims are dropped.



| Entry | Value |
|-------------------|--------------------------------------------|
| CN                | ms-DS-Ingress-Claims-Transformation-Policy |
| Ldap-Display-Name | msDS-IngressClaimsTransformationPolicy     |
| Size              | \-                                         |
| Update Privilege  | \-                                         |
| Update Frequency  | \-                                         |
| Attribute-Id      | 1.2.840.113556.1.4.2191                    |
| System-Id-Guid    | 86284c08-0c6e-1540-8b15-75147d23d20d       |
| Syntax            | [**Object(DS-DN)**](s-object-ds-dn.md)    |



## Implementations

-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | 2190                                                 |
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



 

 





