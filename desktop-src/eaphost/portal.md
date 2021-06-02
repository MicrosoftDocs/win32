---
title: Extensible Authentication Protocol Host
description: Learn about the Extensible Authentication Protocol (EAP) host. See run-time requirements and view additional available resources.
ms.assetid: caaef367-2952-44fc-ac4c-f0db6387850e
ms.topic: article
ms.date: 05/31/2018
---

# Extensible Authentication Protocol Host

## Purpose


EAPHost is a Microsoft Windows Networking component that provides an Extensible Authentication Protocol (EAP) infrastructure for the authentication of "supplicant" protocol implementations such as [802.1X](/previous-versions/windows/embedded/ms890287(v=msdn.10)) and [Point-to-Point](https://go.microsoft.com/fwlink/p/?linkid=83919) (PPP). It also allows for authentication with "authenticator" technologies such as the Microsoft network policy server (NPS). Unlike the previous IAS Server ([RADIUS](/windows/desktop/Nps/ias-about-internet-authentication-service)), NPS supports [Network Access Protection](/windows/desktop/NAP/network-access-protection-start-page) (NAP).


The EAPHost APIs enable applications to authenticate using the EAPHost service, and provide a template for the development of conformant authentication methods for use with EAPHost.

## Run-time requirements

The EAPHost APIs are supported only in Windows Vista and later operating systems.

## Related topics

<dl> <dt>

[About EAPHost](about-eap-host.md)
</dt> <dt>

[Using EAPHost](using-eap-host.md)
</dt> <dt>

[EAPHost API Reference](eaphost-api-reference.md)
</dt> </dl>

 

 