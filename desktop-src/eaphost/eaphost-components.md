---
title: Components of EAPHost
description: Learn about the three components of EAPHost authentication. View additional available resources for using EAPHost authentication.
ms.assetid: f875c3f8-d2fb-461e-b356-e1b2ccaf9981
ms.topic: article
ms.date: 05/31/2018
---

# Components of EAPHost

This topic describes the three components of EAPHost authentication.

## EAPHost Components

EAPHost authentication has the following three components.

-   The supplicant, which makes the authentication requests.
-   The peer (or client) EAP methods, which implement the specific EAP methods and manage the authentication session on the client side.
-   The authenticator (or server) EAP methods, which implement the server side of the EAP protocol.

The supplicant APIs are called directly from an application that wants to authenticate via EAPHost. The peer method and authenticator method APIs, however, are function prototypes that must be implemented for a specific EAP authentication method type - such as the Microsoft Challenge Handshake Authentication Protocol version 2.0 (MS-CHAPv2).

If you are authoring an application that will use EAPHost for authentication, please refer to the [EAPHost Supplicant API Reference](eap-host-supplicant-api-reference.md).

If you are authoring a new EAP authentication method to be managed by EAPHost, please refer to the [EAPHost Peer Method API Reference](eap-host-peer-method-api-reference.md) and the [EAPHost Authenticator Method APIs](eaphost-authenticator-method-apis.md). Note that you will be creating implementations of these APIs exposed in a new DLL that EAPHost loads, rather than calling them directly.

 

 




