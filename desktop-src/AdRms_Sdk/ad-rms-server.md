---
Description: The server component of Active Directory Rights Management Services (AD RMS) is implemented by a set of web services that run on Microsoft Internet Information Services (IIS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0f0bfaf6-52b8-4e37-ac90-3b816f015d2a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Server
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Server

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The server component of Active Directory Rights Management Services (AD RMS) is implemented by a set of web services that run on Microsoft Internet Information Services (IIS). Beginning with Windows Server 2008, you can install and configure the AD RMS service by adding it as a role. To install the service on prior operating systems, download it from the Microsoft download center at [Microsoft Windows Rights Management Services with Service Pack 2](http://go.microsoft.com/fwlink/p/?linkid=73722). Of the many web services installed, the following are important for application development.

| Service               | Description                                                                                                                                                                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administration        | Hosts the Administration website that enables you to manage AD RMS. The service runs on root certification servers and on licensing servers. You can use the [Active Directory Rights Management Services Scripting API](https://msdn.microsoft.com/library/bb968797) to write administration scripts.                                                                      |
| Account Certification | Creates machine certificates that identify computers in the AD RMS certificate hierarchy and rights account certificates that associate users with specific computers. For more information, see [Activating a Computer](activating-a-computer.md) and [Activating a User](activating-a-user.md). This service runs on the root certification server. |
| Licensing             | Issues [*end-user licenses*](https://www.bing.com/search?q=*end-user licenses*). The service runs on root certification servers and on licensing servers.                                                                                                                                                                                                              |
| Publishing            | Creates [*issuance licenses*](https://www.bing.com/search?q=*issuance licenses*) which define the policies that can be enumerated in an end-user license. For more information, see [Creating and Using Issuance Licenses](creating-an-issuance-license.md). The service runs on root certification servers and on licensing servers.                                 |
| Precertification      | Enables a server to request a [*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*) on behalf of a user. The service runs on root certification servers and on licensing servers.                                                                                                                                                |
| Service Locator       | Provides the URL of the account certification, licensing, and publishing services to Active Directory so that they can be discovered by AD RMS clients. The service runs on root certification servers and on licensing servers.                                                                                                                        |



 

## Related topics

<dl> <dt>

[AD RMS Overview](ad-rms-overview.md)
</dt> </dl>

 

 



