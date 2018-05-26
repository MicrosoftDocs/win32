---
Description: To publish and consume protected content, an Active Directory Rights Management Services (AD RMS) application makes use of several different types of certificates and licenses, each of which consists of a certificate chain that leads back ultimately to a Microsoft certification authority. Microsoft provides the following hierarchiesThe Pre-production hierarchy can be used to develop and test applications.The Production hierarchy must be used by released applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1d06606c-81f0-48f2-b51b-80496957b5c5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Setting Up the Pre-production Development Environment
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Setting Up the Pre-production Development Environment

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

To publish and consume protected content, an Active Directory Rights Management Services (AD RMS) application makes use of several different types of certificates and licenses, each of which consists of a certificate chain that leads back ultimately to a Microsoft certification authority. Microsoft provides the following hierarchies:

-   The Pre-production hierarchy can be used to develop and test applications.
-   The Production hierarchy must be used by released applications.

We recommend that you use the Pre-production hierarchy when developing an application. By doing so, you can work without signing a Production License Agreement with Microsoft. For more information, see [Application Licensing Information](application-licensing-information.md).

The following topics discuss how to set up your Pre-production development environment. The topics are listed in the order that you should perform the associated tasks.

-   [Install the SDK](install-the-sdk.md)
-   [Configure the Registry](configure-the-registry.md)
-   [Install the Client and Server Components](install-the-client-and-server-components.md)
-   [Enroll the Server](enroll-the-server.md)
-   [Activate the Development Computer](activate-the-development-computer.md)
-   [Activate a User Account](activate-a-user-account.md)
-   [Create an Application Manifest](create-an-application-manifest.md)
-   [Verify the Development Environment](verify-the-development-environment.md)

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



