---
Description: The Active Directory Rights Management Services client software is included with the Windows 7 operating system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dccabb5d-7af1-4b7a-85ac-9e00823368f6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RMS in Windows 7
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RMS in Windows 7

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services client software is included with the Windows 7 operating system. The AD RMS SDK is included in the Microsoft Windows Software Development Kit (SDK), which you can download from the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=83468) on the Microsoft website.

Some of the added features for AD RMS in Windows 7 are highlighted in the following list:

-   4 KB cipher block chaining (CBC) support for encryption has been added. For more information see [**DRMEncrypt**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmencrypt) or [**DRMDecrypt**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmdecrypt).
-   You can reuse the content key from a signed issuance license when you create a new issuance license, in some cases. For more information see [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense).
-   A new API, [**DRMGetSignedIssuanceLicenseEx**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicenseex), allows you to control which rights account certificate (RAC)/client licensor certificate (CLC) pair is used for each call to retrieve a signed issuance license.
-   You can set the size limit for signed issuance licenses, using a registry key. If the size of a signed issuance license exceeds the limit you set, the **E\_DRM\_ISSUANCELICENSE\_LENGTH\_LIMIT\_EXCEEDED** error code is returned. For more information, see [Configure the Registry.](configure-the-registry.md)

 

 



