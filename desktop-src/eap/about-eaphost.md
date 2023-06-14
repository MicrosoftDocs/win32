---
title: About the EAP and EAPHost relationship
description: Describes the relationship between the Extensible Authentication Protocol (EAP) and Extensible Authentication Protocol Host.
ms.assetid: 7f585fc6-71ed-4a64-88a7-6acb1550e825
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Learn about the EAP and EAPHost relationship

This topic describes the relationship between the Extensible Authentication Protocol (EAP) and Extensible Authentication Protocol Host. For new EAP method development, see [Extensible Authentication Protocol Host](../eaphost/portal.md).

## EAPHost Framework

EAPHost is considered to be a framework for EAP for two reasons.

- EAPHost is a Windows infrastructure component that hosts the EAP plug-ins
- EAPHost implements the EAP protocol as per [RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84063). An EAP authentication consists of the EAP protocol as per [RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84063), and the EAP method-specific aspects of the protocol.

## Related topics

- [About EAP and EAPHost](about-extenstible-authentication-protocol-and-eaphhost.md)