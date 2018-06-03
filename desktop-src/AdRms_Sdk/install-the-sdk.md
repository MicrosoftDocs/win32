---
Description: The AD RMS SDK contains functions and other data types that enable the development of applications that extend the AD RMS client and server components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 930624c8-9747-4867-8529-e461192a978a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Install the SDK
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Install the SDK

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The AD RMS SDK contains functions and other data types that enable the development of applications that extend the AD RMS client and server components. The SDK is included in the Microsoft Windows Software Development Kit (SDK) which can be downloaded from MSDN at the following location:

-   [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=84091)

If you are developing for operating systems prior to Windows Vista and Windows Server 2008, you can download the SDK from:

-   [Rights Management Services with SP2 SDK](http://go.microsoft.com/fwlink/p/?linkid=104548)

## Files Installed with the Operating System

Beginning with Windows Vista and Windows Server 2008, the following files are installed in *%SystemRoot%*\\System32 (32-bit files) or *%SystemRoot%*\\SysWow64 (64-bit files). If you are using a previous RMS version, the files are downloaded with the client.



| File name                | Description                                                                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Msdrm.dll                | Dynamic link library (DLL) that contains the AD RMS functions.                                                                                        |
| Secproc.dll              | The client lockbox for the Production hierarchy.                                                                                                      |
| Secproc\_ssp.dll         | The server lockbox for the Production hierarchy.                                                                                                      |
| Secproc\_isv.dll         | The client lockbox for the Pre-production hierarchy.                                                                                                  |
| Secproc\_ssp\_isv.dll    | The server lockbox for the Pre-production hierarchy.                                                                                                  |
| Rmactivate.exe           | Retrieves a machine certificate that signs the computer into the Production hierarchy.                                                                |
| Rmactivate\_isv.exe      | Retrieves a machine certificate that signs the computer into the Pre-production hierarchy.                                                            |
| Rmactivate\_ssp.exe      | Retrieve a machine certificate that signs the computer into the Production hierarchy. Use when developing applications that require a server lockbox. |
| Rmactivate\_ssp\_isv.exe | Retrieve a machine certificate that signs the computer into the Pre-production hierarchy. Use for applications that require a server lockbox.         |



 

## Files and Folders Installed with the SDK

The following files are installed with the SDK.



| File or folder name            | Location                                   | Description                                                                                                                 |
|--------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Genmanifest.exe                | *SDKInstallPath*                           | Generates a manifest for use during development of an AD RMS-enabled application.                                           |
| ISVTier5AppSigningPrivKey.dat  | *SDKInstallPath*\\Bin                      | Contains the private key used to generate a manifest for use during development of an AD RMS-enabled application.           |
| ISVTier5AppSIgningPubKey.dat   | *SDKInstallPath*\\Bin                      | Contains the public key used to generate a manifest for use during development of an AD RMS-enabled application.            |
| ISVTier5AppSignSDK\_Client.xml | *SDKInstallPath*\\Bin                      | Contains the certificate used to generate a manifest for use during the development phase of an AD RMS-enabled application. |
| ISVTier5AppSignSDK.cc          | *SDKInstallPath*\\Bin                      | Can be used to understand the structure of the Pre-production certificate.                                                  |
| ISVTier5AppSignSDK.xml         | *SDKInstallPath*\\Bin                      | Can be used to understand the structure of the Pre-production certificate.                                                  |
| Msdrm.h                        | *SDKInstallPath*\\Include                  | Contains the signatures of the functions exported by the AD RMS SDK.                                                        |
| Msdrmdefs.h                    | *SDKInstallPath*\\Include                  | Contains the signatures of the structures, enumeration types, and flags exposed by the SDK.                                 |
| Msdrmerror.h                   | *SDKInstallPath*\\Include                  | Defines custom error codes that can be returned by AD RMS functions.                                                        |
| Msdrmgetinfo.h                 | *SDKInstallPath*\\Include                  | Contains global constants that can be used to query for license information.                                                |
| Msdrm.lib                      | *SDKInstallPath*\\Lib                      | Import library used to represent Msdrm.dll during compilation.                                                              |
| \\AcquireClientLicensor        | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to acquire a client licensor certificate.                                                             |
| \\AcquireTemplates             | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to download and enumerate templates from an AD RMS server.                                            |
| \\Consumption                  | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to encrypt and decrypt content.                                                                       |
| \\MachineActivation            | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to activate a machine.                                                                                |
| \\OfflinePublishing            | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to create and sign a license offline.                                                                 |
| \\OnlinePublishing             | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to create an unsigned issuance license.                                                               |
| \\PublishingACL                | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to create an unsigned issuance license.                                                               |
| \\PublishingTemplate           | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to create an unsigned issuance license from an existing template.                                     |
| \\SbActivation                 | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to activate a machine and user by using the server lockbox.                                           |
| \\UserActivation               | *SDKInstallPath*\\Samples\\Security\\ADRMS | Sample that shows how to activate a user.                                                                                   |



 

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



