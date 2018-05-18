---
title: Endpoint Identity
description: The types defined in this section are used to define the security identity of an endpoint address.
ms.assetid: '39639b9a-32e2-44d2-9bda-a2ad23850de8'
keywords: ["Endpoint Identity Web Services for Windows", "WWSAPI", "WWS"]
---

# Endpoint Identity

The types defined in this section are used to define the security identity of an endpoint address.

The following API elements are part of endpoint indentity:



| Enumeration                                                       | Description                                                                                                                   |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ENDPOINT\_IDENTITY\_TYPE**](ws-endpoint-identity-type.md) | The type of the endpoint identity, used as a selector for subtypes of [**WS\_ENDPOINT\_IDENTITY**](ws-endpoint-identity.md). |



 



| Structure                                                               | Description                                                                                  |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WS\_CERT\_ENDPOINT\_IDENTITY**](ws-cert-endpoint-identity.md)       | The type for certificate endpoint identity .                                                 |
| [**WS\_DNS\_ENDPOINT\_IDENTITY**](ws-dns-endpoint-identity.md)         | The type for specifying an endpoint identity represented by a DNS name.                      |
| [**WS\_ENDPOINT\_IDENTITY**](ws-endpoint-identity.md)                  | The base type for all endpoint identities.                                                   |
| [**WS\_RSA\_ENDPOINT\_IDENTITY**](ws-rsa-endpoint-identity.md)         | Type for RSA endpoint identity.                                                              |
| [**WS\_SPN\_ENDPOINT\_IDENTITY**](ws-spn-endpoint-identity.md)         | The type for specifying an endpoint identity represented by an SPN (service principal name). |
| [**WS\_UNKNOWN\_ENDPOINT\_IDENTITY**](ws-unknown-endpoint-identity.md) | The type for an unknown endpoint identity.                                                   |
| [**WS\_UPN\_ENDPOINT\_IDENTITY**](ws-upn-endpoint-identity.md)         | The type for specifying an endpoint identity represented by a UPN (user principal name).     |



 

 

 




