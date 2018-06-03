---
Description: Active Directory Rights Management Services (AD RMS) consists of separate client and server components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1b049ce6-d748-4110-a4d6-be6f9ec3ac20
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Install the Client and Server Components
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Install the Client and Server Components

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) consists of separate client and server components. The client software allows users to create, publish, and consume AD RMS-protected content. The server component is implemented as a set of web services that can be used to administer an AD RMS infrastructure, issue licenses to content consumers and publishers, and issue certificates to computers and users.

Beginning with Windows Vista, the client is included in the operating system, and both the client and the server components are included in Windows Server 2008. You can download the client and server components for prior operating systems from the following locations.

-   [32-bit RMS client v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=67736)
-   [64-bit RMS client v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=67935)
-   [RMS Server v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=73722)

To configure the server component on Windows Server 2008, you must install the AD RMS role. Before doing so, however, you must configure the registry to specify that you will be using the Pre-Production certificate hierarchy rather than the Production hierarchy. If, however, you are developing applications against a prior server operating system, configure the registry after installing RMS server v1.0 SP2 but before provisioning the AD RMS service. For more information, see [Configure the Registry](configure-the-registry.md).

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



