---
title: Endpoint Identity
description: The types defined in this section are used to define the security identity of an endpoint address.
ms.assetid: 39639b9a-32e2-44d2-9bda-a2ad23850de8
keywords:
- Endpoint Identity Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Endpoint Identity

The types defined in this section are used to define the security identity of an endpoint address.

The following API elements are part of endpoint indentity:



| Enumeration                                                       | Description                                                                                                                   |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ENDPOINT\_IDENTITY\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_endpoint_identity_type?branch=master) | The type of the endpoint identity, used as a selector for subtypes of [**WS\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_endpoint_identity?branch=master). |



 



| Structure                                                               | Description                                                                                  |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WS\_CERT\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_cert_endpoint_identity?branch=master)       | The type for certificate endpoint identity .                                                 |
| [**WS\_DNS\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_dns_endpoint_identity?branch=master)         | The type for specifying an endpoint identity represented by a DNS name.                      |
| [**WS\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_endpoint_identity?branch=master)                  | The base type for all endpoint identities.                                                   |
| [**WS\_RSA\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_rsa_endpoint_identity?branch=master)         | Type for RSA endpoint identity.                                                              |
| [**WS\_SPN\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_spn_endpoint_identity?branch=master)         | The type for specifying an endpoint identity represented by an SPN (service principal name). |
| [**WS\_UNKNOWN\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_unknown_endpoint_identity?branch=master) | The type for an unknown endpoint identity.                                                   |
| [**WS\_UPN\_ENDPOINT\_IDENTITY**](/windows/win32/WebServices/ns-webservices-_ws_upn_endpoint_identity?branch=master)         | The type for specifying an endpoint identity represented by a UPN (user principal name).     |



 

 

 




