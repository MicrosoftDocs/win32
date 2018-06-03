---
Description: Active Directory Rights Management Services (AD RMS) consists of both a server and a client component.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b6cd1866-6a48-4a69-96b6-6f2a2bb11669
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Overview
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Overview

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) consists of both a server and a client component. The server component is made up of multiple web services that run on a Microsoft server such as Windows Server 2008. The client component can be run on either a client or server operating system and contains functions that enable an application to encrypt and decrypt content, retrieve templates and revocation lists, acquire licenses and certificates from a server, and many other related tasks.

You can create AD RMS-enabled applications by using the AD RMS SDK. Applications enable end-users to protect, publish, store, retrieve, and consume content. The SDK primarily leverages functionality exposed by the client in Msdrm.dll but also includes various SOAP web methods that enable a custom application to make calls directly to the AD RMS server component.

The following topics provide a brief overview of AD RMS servers, clients, and custom applications:

-   [AD RMS Server](ad-rms-server.md)
-   [AD RMS Client](ad-rms-client.md)
-   [AD RMS Applications](ad-rms-applications.md)

## Related topics

<dl> <dt>

[About the AD RMS SDK](about-the-ad-rms-sdk.md)
</dt> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



