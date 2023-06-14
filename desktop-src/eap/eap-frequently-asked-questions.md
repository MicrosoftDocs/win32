---
title: EAP Frequently Asked Questions
description: "Find answers to frequently asked questions (FAQs) about the EAP APIs, such as 'What is the lifetime of an EAP authentication?'."
ms.assetid: 4e26df7b-3cce-4522-ab39-e24f06b4c4b4
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# EAP Frequently Asked Questions

The following topic provides answers to commonly-asked questions about the EAP APIs.

| Question | Answer |
|--|--|
| What is the lifetime of an EAP authentication? | In a typical situation the authentication consists of everything that occurs between calling the [**RapEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)) and [**RasEapEnd**](/previous-versions/windows/desktop/legacy/aa363521(v=vs.85)) functions. When a user chooses to configure an EAP provider in the RRAS snap-in, an authentication consists of everything that occurs between calling the [**Initialize**](/windows/desktop/api/Rrascfg/nf-rrascfg-ieapproviderconfig-initialize) and [**Uninitialize**](/windows/desktop/api/Rrascfg/nf-rrascfg-ieapproviderconfig-uninitialize) methods.<br/> |
| What is "group policy"? | For a description of group policy, see [Group Policy Collection](/previous-versions/windows/it-pro/windows-server-2003/cc779838(v=ws.10)). |
| Can EAP functions override configuration policy specified by group policy? | No, never. If group policy is in use, group policy settings will always override EAP configuration settings. |
| I need to warn users about invalid PIN attempts. Is it possible to capture an invalid pin code? | When the user enters the wrong PIN, Extensible Authentication Protocol-Transport Layer Security (EAP-TLS) will send an error codes to the VPN supplicant. Once an error code is returned, the supplicant can implement its preferred retry logic. |
| What is EAP-Transport Level Security (EAP-TLS)? | EAP-TLS is a client-server protocol in which distinct certificate profiles are typically used for the client and server.For more information, see [IETF RTC 2716](/previous-versions/windows/embedded/ms885336(v=msdn.10)).|

## Related topics
- [Using Extensible Authentication Protocol](using-extenstible-authentication-protocol.md)
- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
