---
description: The WebAuthn technology (webauthn.h) provides Win32 apps with APIs for communicating to Windows Hello and external security keys as part of WebAuthN and CTAP specifications.
ms.assetid: c4655297-58a3-4dec-8278-a6e65d21d4d5
title: WebAuthN API
ms.topic: article
ms.date: 08/22/2022
---

# WebAuthn API

## Purpose

The Windows WebAuthn API provides Win32 apps a way to register new phishing-resistant credentials or sign in a user via the Windows Hello platform authenticator and/or external FIDO2 security keys, leveraging the [Web Authentication (WebAuthn)](https://w3c.github.io/webauthn/) and [Client to Authenticator Protocol (CTAP)](https://fidoalliance.org/specs/fido-v2.0-ps-20190130/fido-client-to-authenticator-protocol-v2.0-ps-20190130.html) specifications.

## Developer audience

The Windows WebAuthn API is designed for use by C/C++ developers of Windows applications. Developers can use this Windows API to register new phishing-resistant credentials or sign in a user using the Windows Hello platform authenticator and/or external FIDO2 security keys, leveraging the Web Authentication (WebAuthn) and Client to Authenticator Protocol (CTAP) specifications.

## Runtime requirements

| Requirement | Value |
|--------|--------|
| Operating system | Windows 10 version 1903 and later<br/>Windows 11 |
| Header | webauthn.h |

## In this section

- [WebAuthn functions](webauthn-functions.md)
- [WebAuthn structures](webauthn-structures.md)
- [WebAuthn constants](webauthn-constants.md)
