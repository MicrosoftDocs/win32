---
title: About EAP
description: Extensible Authentication Protocol (EAP), a standard supported by many Microsoft networking components.
ms.assetid: a2f41808-4316-431a-ab58-f1e25d3c61f6
keywords:
- Extensible Authentication Protocol,described
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# About EAP

This topic describes Extensible Authentication Protocol (EAP), a standard supported by many Microsoft networking components.

## EAP Components

EAP is crucial for protecting the security of wireless (802.1X) LANs, wired LANs, and dial-up and Virtual Private Networks (VPNs).

The following components support the EAP protocol.

- Microsoft Remote Access Clients and Servers for both dial-up and VPN (PPTP and L2TP/IPSec) implement EAP as an extension to PPP. For more information, see [RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84063).
- Microsoft IEEE 802.1X compatible wireless and wired LAN clients implement EAP as defined in the IEEE 802.1X draft standard.
- Microsoft RADIUS server, called Internet Authentication Service (IAS) implement EAP as defined in [RFC 2865](https://go.microsoft.com/fwlink/p/?linkid=84055).

All of the above components support this extensible architecture through the Microsoft Windows Software Development Kit (SDK), making it possible to integrate third-party authentication modules. This extensible mechanism can be used to support token cards, Kerberos, Public Key, and S/Key authentication protocols.

## Protected Extensible Authentication Protocol

In addition to EAP, the wireless (802.1X) implementation and RADIUS server also support an emerging standard called Protected EAP (PEAP).

PEAP provides several key services to other EAP authentication protocols, as follows.

- PEAP encrypts EAP packets of other EAP authentication protocols using Transport Layer Security (TLS), a Secure Socket Layer (SSL) based technology. For more information, see [RFC 2716](https://go.microsoft.com/fwlink/p/?linkid=84050).
- PEAP authenticates the server-side using a Server Certificate, with RADIUS server.
- PEAP offers fast re-authentication capability that supports efficient roaming between wireless devices.
- PEAP manages the fragmentation and re-assembly of EAP packets.
- PEAP generates keys used for encrypting wireless traffic.

PEAP makes it much easier to write an EAP protocol because the programmer no longer has to address these issues.

## Related topics

- [About EAP and EAPHost](about-extenstible-authentication-protocol-and-eaphhost.md)
- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
