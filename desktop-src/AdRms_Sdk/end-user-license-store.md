---
Description: End-user licenses are installed in one of the following folders, depending on the Active Directory Rights Management Services (AD RMS) version and on the operating system.VersionCertificate locationFor AD RMS on Windows Vista and Windows Server 2008 using the client lockbox%USERPROFILE%\\AppData\\Local\\Microsoft\\DRMFor RMS client 1.0 SP2 using the client lockbox%USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM 
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fc297cf3-156e-4ad3-9cf2-1431e0c9e87b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: End-User License Store
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# End-User License Store

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

End-user licenses are installed in one of the following folders, depending on the Active Directory Rights Management Services (AD RMS) version and on the operating system.

| Version                                                                      | Certificate location                                            |
|------------------------------------------------------------------------------|-----------------------------------------------------------------|
| For AD RMS on Windows Vista and Windows Server 2008 using the client lockbox | %USERPROFILE%\\AppData\\Local\\Microsoft\\DRM                   |
| For RMS client 1.0 SP2 using the client lockbox                              | %USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM |



 

## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[End-User License](end-user-license.md)
</dt> <dt>

[End User License XML Example](end-user-license-xml-example.md)
</dt> </dl>

 

 



