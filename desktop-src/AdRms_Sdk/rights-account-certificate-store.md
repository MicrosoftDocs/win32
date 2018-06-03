---
Description: Each rights account certificate is installed in one of the following folders, depending on the Active Directory Rights Management (AD RMS) version and on the operating system.VersionCertificate locationAD RMS on Windows Vista and Windows Server 2008 using the client lockbox%USERPROFILE%\\AppData\\Local\\Microsoft\\DRMRMS client 1.0 SP2 using the client lockbox%USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM 
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6b8ce617-aee3-4dec-8010-c21cded312aa
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights Account Certificate Store
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rights Account Certificate Store

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Each rights account certificate is installed in one of the following folders, depending on the Active Directory Rights Management (AD RMS) version and on the operating system.

| Version                                                                  | Certificate location                                            |
|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| AD RMS on Windows Vista and Windows Server 2008 using the client lockbox | %USERPROFILE%\\AppData\\Local\\Microsoft\\DRM                   |
| RMS client 1.0 SP2 using the client lockbox                              | %USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM |



 

## Related topics

<dl> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[Rights Account Certificate XML Example](rights-account-certificate-xml-example.md)
</dt> <dt>

[Rights Account Certificates](rights-account-certificates.md)
</dt> </dl>

 

 



