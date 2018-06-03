---
Description: Before you can release an application developed by using the Active Directory Rights Management (AD RMS) SDK, you must generate a public key pair, submit your public key to Microsoft, and sign a Production License Agreement to obtain a production certificate. The production certificate and the pre-production certificate discussed in Developing an AD RMS Application perform a similar function but are intended for use in different environments. Both contain a certificate chain with a Microsoft certification authority (CA) certificate at the root of trust, but the pre-production certificate is used only when developing an AD RMS application. The production certificate is used in post-release environments.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5ae4a1c4-3aff-42c4-8a61-1423c2e93342
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Releasing an AD RMS Application
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Releasing an AD RMS Application

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Before you can release an application developed by using the Active Directory Rights Management (AD RMS) SDK, you must generate a public key pair, submit your public key to Microsoft, and sign a Production License Agreement to obtain a production certificate. The production certificate and the pre-production certificate discussed in [Developing an AD RMS Application](developing-an-ad-rms-application.md) perform a similar function but are intended for use in different environments. Both contain a certificate chain with a Microsoft certification authority (CA) certificate at the root of trust, but the pre-production certificate is used only when developing an AD RMS application. The production certificate is used in post-release environments.

The production certificate and the associated private key are used to create and sign a manifest that identifies the files that can or must be loaded into the process space of your application and those that must not be loaded. The manifest is used by the lockbox to provide a secure environment for your application and for the content created or published by your application. For more information about obtaining a production certificate, see [Requesting a Production License Agreement](requesting-a-production-license-agreement.md).

## Related topics

<dl> <dt>

[Application Licensing Information](application-licensing-information.md)
</dt> </dl>

 

 



