---
Description: Beginning with Windows Vista, the client software is now included in the operating system, and the name has been changed to Active Directory Rights Management Services (AD RMS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5926adfc-43ac-420f-9220-2acc3e9169d4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RMS in Windows Vista
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RMS in Windows Vista

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Beginning with Windows Vista, the client software is now included in the operating system, and the name has been changed to Active Directory Rights Management Services (AD RMS). The name of all other versions, including version 1.0 SP2, remains Rights Management Services (RMS). The AD RMS SDK is included in the Microsoft Windows SDK which you can download from [http://www.microsoft.com/downloads](http://go.microsoft.com/fwlink/p/?linkid=83468).

The AD RMS SDK is identical to the RMS version 1.0 SP1 SDK except for the following:

-   The public/private key pair and Pre-production certificate used when developing an AD RMS-enabled application are included with the SDK.
-   64-bit application development is now supported.
-   The [**DRMDeleteLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmdeletelicense?branch=master) function now allows you to delete an end-user license based on a handle to the client session or a handle to the license storage session.
-   The [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function returns a new error code, E\_DRM\_PLATFORM\_POLICY\_VIOLATION, if a system DLL fails the module authentication check.

## Related topics

<dl> <dt>

[What's New in the AD RMS SDK](what-s-new-in-the-ad-rms-sdk.md)
</dt> </dl>

 

 



