---
Description: Exclusion is the process of preventing specified users or computers from acquiring new issuance licenses, end-user licenses, or rights account certificates. Exclusion does not affect licenses or certificates that have already been acquired.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 06d7053c-d143-4759-933f-dc8746a725c5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Exclusion
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exclusion

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Exclusion is the process of preventing specified users or computers from acquiring new [*issuance licenses*](https://www.bing.com/search?q=*issuance licenses*), [*end-user licenses*](https://www.bing.com/search?q=*end-user licenses*), or [*rights account certificates*](https://www.bing.com/search?q=*rights account certificates*). Exclusion does not affect licenses or certificates that have already been acquired.

Exclusion is set on an Active Directory Rights Management Services (AD RMS) server by an administrator. A license creator cannot specify or control exclusion. A user can be excluded by rights account certificate, or by lockbox, operating system, or application version number.

Exclusion is the best way to prevent a compromised lockbox from acquiring new licenses.

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Revocation](revocation.md)
</dt> </dl>

 

 



