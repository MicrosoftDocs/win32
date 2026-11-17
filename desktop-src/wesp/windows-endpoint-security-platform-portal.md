---
title: Windows endpoint security platform
description: The Windows endpoint security platform provides a user-mode API enabling development of endpoint security software without using kernel-mode drivers.
author: tomlavoy
ms.author: tlavoy
ms.topic: overview
ms.date: 11/16/2026
ai-usage: ai-assisted
---

# Windows endpoint security platform

## What is the Windows endpoint security platform?

The Windows endpoint security platform (WESP) is a Windows component that provides secure access to system monitoring and protection capabilities for use by antimalware, monitoring, and other endpoint protection software via user-mode APIs. This allows developers of endpoint security solutions to provide robust protection capabilities without requiring the use of kernel-mode drivers.

## Why would I want to use it?

Leveraging user-mode APIs rather than relying on kernel-mode drivers greatly reduces the impact of errors or misconfigurations on the stability of users' systems. The Windows endpoint security platform provides secure, efficient access to many capabilities that previously required kernel-mode drivers. In addition, the platform provides an alternative mechanism for early boot monitoring and access to [Protected Process Light (PPL)](/windows/win32/services/protecting-anti-malware-services-) without requiring an [Early Launch Antimalware (ELAM)](/windows-hardware/drivers/install/early-launch-antimalware) driver.

## How do I start using it?

The platform is available starting with the October 2026 (10D) Windows 11 client releases: version 25H2 (OS build 26200.9818) and version 26H2 (OS build 26300.9818). You can begin building and testing your product using the latest [Windows SDK](/windows/apps/windows-sdk/downloads) on a supported Windows build.

Note that, in the initial release, you must be a member of the [Microsoft Virus Initiative](/defender-xdr/virus-initiative-criteria) (MVI) program to register with the platform as a client. Future updates to the Windows endpoint security platform will provide access to some capabilities without requiring MVI membership. You will also need to sign your security application using Azure [Artifact Signing](/azure/artifact-signing/quickstart). Only applications properly signed using an Artifact Signing certificate profile with the Windows endpoint security platform program type can register with the platform and access these APIs.

## In this section

| Topic | Description |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Windows endpoint security platform requirements, signing, and enrollment](wesp-requirements.md) | Requirements for using the Windows endpoint security platform and how to enroll as a client |
| [Debug and validate WESP process tagging](wesp-debug-process-tagging.md) | Configure debug process tagging and verify the WESP permission claim on a process token |
| [Windows endpoint security platform (WESP) API overview](wesp-api-overview.md) | Learn how the preview Windows endpoint security platform (WESP) models events, rules, filters, notifications, properties, and context |
| [Windows endpoint security platform API reference](wesp-api-reference.md) | Detailed descriptions of interfaces, enumerations, and other programming elements for using the Windows endpoint security platform |
