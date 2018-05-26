---
Description: The machine certificate is named CERT-Machine.drm and is installed in one of the following folders, depending on the Active Directory Rights Management Services (AD RMS) version and on the operating system.VersionCertificate locationAD RMS on Windows Vista and Windows Server 2008 using the client lockbox%USERPROFILE%\\AppData\\Local\\Microsoft\\DRMAD RMS on Windows Vista and Windows Server 2008 using the server lockbox%ALLUSERSPROFILE%\\Microsoft\\DRM\\Server\\UserSid RMS client 1.0 SP2 using the client lockbox%USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRMRMS server 1.0 SP2 using the server lockbox%ALLUSERSPROFILE%\\Application Data\\Microsoft\\DRM\\Server\\UserSid  
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bd9da046-1bac-47d2-a149-91e7f25df3d5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Machine Certificate Store
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Machine Certificate Store

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The machine certificate is named CERT-Machine.drm and is installed in one of the following folders, depending on the Active Directory Rights Management Services (AD RMS) version and on the operating system.

| Version                                                                  | Certificate location                                                 |
|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| AD RMS on Windows Vista and Windows Server 2008 using the client lockbox | %USERPROFILE%\\AppData\\Local\\Microsoft\\DRM                        |
| AD RMS on Windows Vista and Windows Server 2008 using the server lockbox | %ALLUSERSPROFILE%\\Microsoft\\DRM\\Server\\UserSid                   |
| RMS client 1.0 SP2 using the client lockbox                              | %USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM      |
| RMS server 1.0 SP2 using the server lockbox                              | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\DRM\\Server\\UserSid |



 

## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Machine Certificate XML Example](machine-certificate-xml-example.md)
</dt> <dt>

[Machine Certificates](machine-certificates.md)
</dt> </dl>

 

 



