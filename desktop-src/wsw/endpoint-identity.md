---
title: Endpoint Identity
description: The types defined in this section are used to define the security identity of an endpoint address.
ms.assetid: 39639b9a-32e2-44d2-9bda-a2ad23850de8
keywords:
- Endpoint Identity Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Endpoint Identity

The types defined in this section are used to define the security identity of an endpoint address.

The following API elements are part of endpoint indentity:



| Enumeration                                                       | Description                                                                                                                   |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ENDPOINT\_IDENTITY\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_endpoint_identity_type) | The type of the endpoint identity, used as a selector for subtypes of [**WS\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_identity). |



 



| Structure                                                               | Description                                                                                  |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WS\_CERT\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_endpoint_identity)       | The type for certificate endpoint identity .                                                 |
| [**WS\_DNS\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_dns_endpoint_identity)         | The type for specifying an endpoint identity represented by a DNS name.                      |
| [**WS\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_identity)                  | The base type for all endpoint identities.                                                   |
| [**WS\_RSA\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_rsa_endpoint_identity)         | Type for RSA endpoint identity.                                                              |
| [**WS\_SPN\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_spn_endpoint_identity)         | The type for specifying an endpoint identity represented by an SPN (service principal name). |
| [**WS\_UNKNOWN\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_unknown_endpoint_identity) | The type for an unknown endpoint identity.                                                   |
| [**WS\_UPN\_ENDPOINT\_IDENTITY**](/windows/desktop/api/WebServices/ns-webservices-ws_upn_endpoint_identity)         | The type for specifying an endpoint identity represented by a UPN (user principal name).     |



 

 

 




