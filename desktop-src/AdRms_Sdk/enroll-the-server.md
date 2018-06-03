---
Description: You must enroll an Active Directory Rights Management Services (AD RMS) server to identify it in the Pre-Production or Production hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 75e42363-fd83-4b1e-a806-e68217e5e589
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enroll the Server
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enroll the Server

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You must enroll an Active Directory Rights Management Services (AD RMS) server to identify it in the Pre-Production or Production hierarchy. The enrollment process leaves a server licensor certificate on the server computer. This certificate chains back to a Microsoft root of trust. How you enroll the server depends on which AD RMS version you are using.

## Self-Enrollment

Beginning with Windows Server 2008, you can enroll an AD RMS server in the appropriate hierarchy without sending information to Microsoft. When you install the AD RMS role, a self-enrollment certificate and private key are also installed. These are used to automatically create the server licensor certificate. No information is exchanged with Microsoft.

## Online Enrollment

If you are using AD RMS v1.0 SP2, you can enroll the server online. Enrollment takes place behind the scenes during the provisioning process, but you must have an Internet connection and you must specify the appropriate registry value to identify which hierarchy you are enrolling the server in. To enroll in the Pre-production hierarchy, add the following **REG\_SZ** value and provision the server. To enroll in the Production hierarchy, clear this value and provision the server. For more information about server registry settings, see [Configure the Registry](configure-the-registry.md).

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



