---
Description: Before you can use Active Directory Rights Management Services (AD RMS), your server must be enrolled in the AD RMS Production or Pre-Production hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 022d4f0b-aee1-4fe6-b095-485645d6278f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Server Enrollment
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Server Enrollment

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Before you can use Active Directory Rights Management Services (AD RMS), your server must be enrolled in the AD RMS Production or Pre-Production hierarchy. The enrollment process installs a server licensor certificate on the server. Beginning with Windows Server 2008, the certificate is installed automatically when AD RMS is configured. No information is exchanged with Microsoft. Preceding server operating systems and RMS versions required that you send an enrollment request to Microsoft.

The following diagram shows how the self-enrollment certificate and the server licensor certificate are introduced into the existing certificate hierarchy. For more information about the enrollment process, see [Enroll the Server](enroll-the-server.md).

![server self-enrollment certificate chain](images/server-self-enroll.png)

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



