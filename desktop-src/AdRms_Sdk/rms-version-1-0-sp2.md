---
Description: Version 1.0 SP2 is intended to be used on operating systems released prior to Windows Vista.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a588ec45-1077-496f-9fc3-5b71ae0222b2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RMS Version 1.0 SP2
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RMS Version 1.0 SP2

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Version 1.0 SP2 is intended to be used on operating systems released prior to Windows Vista. It is identical to the AD RMS SDK released in Windows Vista except for the following:

-   It is not included with the operating system and requires a separate download.
-   The name remains the Rights Management Services SDK rather than the Active Directory Rights Management Services SDK.
-   The [**AcquireLicense**](-acquirelicense.md) web method now enables you to retrieve multiple use licenses for different user accounts from a single license request to the RMS server.
-   The [**GetServerInfo**](-getserverinfo.md) web method enables you to retrieve an XmlNode object that contains information about an AD RMS server.

## Related topics

<dl> <dt>

[What's New in the AD RMS SDK](what-s-new-in-the-ad-rms-sdk.md)
</dt> </dl>

 

 



