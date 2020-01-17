---
title: SSO EAPHost Scenario Overview
description: Contains two scenarios that demonstrate the advantages of a Single-Sign-On (SSO) enabled supplicant.
ms.assetid: 2a5cbcae-74fe-4241-9e20-ec1ec5d9ed8a
ms.topic: article
ms.date: 05/31/2018
---

# SSO EAPHost Scenario Overview

The following topic contains two scenarios that demonstrate the advantages of a Single-Sign-On (SSO) enabled supplicant.

## About the Scenarios

SSO provides functionality to retain additional user credential information than is traditionally stored in the EAP user BLOB. Unlike other credential processes, SSO-enabled supplicants can resolve login situations like AP roaming, and password change without user intervention.

## SSO EAP-TLS PIN Caching Behavior

A supplicant can attempt network authentication using a smartcard-based EAP method such as Extensible Authentication Protocol Transport Layer Security (EAP-TLS). In this and similar scenarios, the supplicant obtains the smartcard PIN from the user and retrieves a user certificate for network authentication followed by a call to WinLogin on the local computer. After successful authentication the supplicant caches the user BLOB, and does not store user PIN information.

When the user roams to a different location session resumption and re-authentication must occur. Since the certificate cannot be stored pre-logon, the user authentication will fail and the supplicant flushes the user BLOB. At this point the user PIN is required to retrieve the user certificate from the smartcard for network authentication. Because SSO caches the PIN, the certificate can be retrieved without user intervention. Without SSO, EAP-TLS would have to raise a PIN collection UI again.

For a step-by-step approach, see [SSO EAP-TLS PIN Caching Behavior](sso-eap-tls-pin-caching-behavior-.md).

## SSO Password Change Behavior

A supplicant can attempt network authentication using a password-based EAP method such as Microsoft Challenge Handshake Authentication Protocol version 2.0 (MS-CHAPv2), configured to use WinLogin credentials. In this scenario, the supplicant collects user credentials once and provides them to EAPHost for network authentication. After successful network authentication the supplicant uses the same set of credentials for WinLogin.

However, if credentials such as the user password were changed during network authentication without an SSO-enabled supplicant, the subsequent WinLogin call will result in failure. SSO retains the new credentials and allows a successful WinLogin without additional user intervention.

For a step-by-step approach, see [SSO Password Change Behavior](sso-password-change-behavior-.md).

## Related topics

<dl> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> </dl>

 

 




