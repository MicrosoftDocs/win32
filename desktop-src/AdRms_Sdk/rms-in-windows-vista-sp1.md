---
Description: The AD RMS client is included in the operating system, and the AD RMS SDK is included in the Microsoft Windows SDK which you can download from http://www.microsoft.com/downloads
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8103408a-b2ac-4a2a-ac1f-5d2bf402b399
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RMS in Windows Vista SP1
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RMS in Windows Vista SP1

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The AD RMS client is included in the operating system, and the AD RMS SDK is included in the Microsoft Windows SDK which you can download from [http://www.microsoft.com/downloads](http://go.microsoft.com/fwlink/p/?linkid=83468)

An AD RMS administrator can now enable AD RMS clients to automatically retrieve templates from an AD RMS server by using a Windows Management Instrumentation (WMI) job in the task scheduler. The [**DRMEnumerateLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmenumeratelicense) function can now be used to enumerate the retrieved templates. You can also use the following functions and web methods if you find it necessary to manually download the issuance license templates:

-   [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate)
-   [**AcquireTemplates**](-acquiretemplates.md)
-   [**AcquireTemplateInformation**](-acquiretemplateinformation.md)

## Related topics

<dl> <dt>

[What's New in the AD RMS SDK](what-s-new-in-the-ad-rms-sdk.md)
</dt> </dl>

 

 



