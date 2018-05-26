---
Description: Certificates obtained for applications that use Active Directory Rights Management Services must be used correctly and must meet the minimum standard specified in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4601671d-5550-49f2-84cf-f55ea80ac7a9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Certificate Use
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Certificate Use

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Certificates obtained for applications that use Active Directory Rights Management Services must be used correctly and must meet the minimum standard specified in the following table.

## 



| Standard level       | Description                                                                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum standard     | Never sign a debug build with a production certificate. Debugging symbols must be off when you build the release version of your application. |
| Recommended standard | None at this time.                                                                                                                            |
| Preferred standard   | None at this time.                                                                                                                            |



 

## Related topics

<dl> <dt>

[Required Application Security Standards](required-application-security-standards.md)
</dt> </dl>

 

 



