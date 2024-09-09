---
title: Extensible Authentication Protocol
description: The Extensible Authentication Protocol (EAP) is a standard supported by several system components. EAP is crucial for protecting the security of wireless (802.1X) and wired LANs, Dial-up, and Virtual Private Networks (VPNs).
ms.assetid: bdbac41e-064c-445f-8f86-a6e2eff2a683
keywords:
- Extensible Authentication Protocol
- Extensible Authentication Protocol, start page
- EAP
- EAP, See Extensible Authentication Protocol
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Extensible Authentication Protocol

## Purpose

The Extensible Authentication Protocol (EAP) is a standard supported by several system components. EAP is crucial for protecting the security of wireless (802.1X) and wired LANs, Dial-up, and Virtual Private Networks (VPNs).

## Where applicable

EAP improves on previous authentication protocols such as Password Authentication Protocol (PAP) and Challenge Handshake Authentication Protocol (CHAP).

For new EAP method development, see [Extensible Authentication Protocol Host](../eaphost/portal.md).

## Developer audience

The EAP API is designed for use by C/C++ programmers. Programmers should be familiar with networking concepts.

> [!NOTE]
> This API is intended for developers implementing EAP methods. It's not intended for users consuming the EAP methods - see [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access).

## Run-time requirements

EAP is supported on client and server computers running on Windows 2000 and later. EAP is also supported on computers running on Windows 2000 Server and later if they are running Network Policy Server (NPS), formerly Internet Authentication Service (IAS). For more information about supported operating systems, see the Requirements section in the documentation.

## Related topics

- [Remote Access Service](/windows/desktop/RRAS/remote-access-start-page)
- [Network Policy Server Extensions](/windows/desktop/nps/ias-extensions)
- [Using Extensible Authentication Protocol](using-extenstible-authentication-protocol.md)
- [Extensible Authentication Protocol Reference](extensible-authentication-protocol-reference.md)
- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
