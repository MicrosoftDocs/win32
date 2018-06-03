---
Description: When you have completed developing and testing you application, perform the following steps to switch from the Pre-production to the Production certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7f364a0d-489b-498d-9960-f9e7c1be5b58
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Switching to the Production Environment
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Switching to the Production Environment

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

When you have completed developing and testing you application, perform the following steps to switch from the Pre-production to the Production certificate hierarchy.

1.  Remove the Active Directory Rights Management Services (AD RMS) role.
2.  Create a public key pair.
3.  Submit the public key to Microsoft and sign the license agreement. Microsoft creates and signs a Production certificate.
4.  Install the signed Production certificate forwarded by Microsoft.
5.  Reconfigure the AD RMS server registry as needed.
6.  Reconfigure affected client computer registries as needed.
7.  Remove all AD RMS certificates and licenses from the client computer(s).
8.  Reinstall the AD RMS role.
9.  Create a new manifest (.mcf) file for your application, specifying the paths of the new public and private keys.
10. Run Genmanifest.exe and specify the signed production certificate and the new .mcf file on the command line.

See the following topics for more information about the preceding steps.

| Topic                                                                                            | Description                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md)       | Discusses how to obtain a key pair. The public key is submitted to Microsoft to acquire a signed Production certificate, and both the public and private key are used to create an application manifest that signs your application into the Production hierarchy. |
| [Requesting a Production License Agreement](requesting-a-production-license-agreement.md)       | Discusses how to contact Microsoft to obtain a Production License Agreement for your custom AD RMS application.                                                                                                                                                    |
| [Production Server Settings](production-server-settings.md)                                     | Discusses the changes you must make to an AD RMS server registry before moving from the Pre-production to the Production certificate hierarchy.                                                                                                                    |
| [Production Client Settings](production-client-settings.md)                                     | Discusses the changes you must make to registries of affected client computers before moving from the Pre-production to the Production certificate hierarchy.                                                                                                      |
| [Restoring a Client Computer to a Clean State](restoring-a-client-computer-to-a-clean-state.md) | Discusses how to remove all AD RMS licenses and certificates from affected clients before switching to the Production hierarchy.                                                                                                                                   |
| [Creating an Application Manifest](creating-an-application-manifest.md)                         | Discusses how to create an application manifest.                                                                                                                                                                                                                   |
| [Genmanifest.exe](genmanifest-exe.md)                                                           | Specifies the syntax of the executable file used to create an application manifest.                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



