---
title: Extensible Authentication Protocol Host
description: Learn about the Extensible Authentication Protocol (EAP) host. See run-time requirements and view additional available resources.
ms.assetid: caaef367-2952-44fc-ac4c-f0db6387850e
ms.topic: article
ms.date: 06/12/2023
ms.contributor: samyun
---

# Extensible Authentication Protocol Host

## Purpose

EAPHost is a Microsoft Windows Networking component that provides an Extensible Authentication Protocol (EAP) infrastructure for the authentication of "supplicant" protocol implementations such as [802.1X](/previous-versions/windows/embedded/ms890287(v=msdn.10)). It also allows for authentication with "authenticator" technologies such as the Microsoft Network Policy Server (NPS) and other third-party servers.

The EAPHost APIs enable applications to authenticate using the EAPHost service, and provide a template for the development of conformant authentication methods for use with EAPHost.

## Run-time requirements

The EAPHost APIs are supported only in Windows Vista and later operating systems.

## Related topics

- [About EAPHost](about-eap-host.md)
- [Using EAPHost](using-eap-host.md)
- [EAPHost API Reference](eaphost-api-reference.md)
- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
