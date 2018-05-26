---
Description: Developing an application by using the Active Directory Rights Management (AD RMS) SDK typically requires a public key pair and a pre-production certificate chain that leads back to a Microsoft certificate at the root of trust.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7100a96c-b8d9-4d5c-94d9-875121de80cc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Developing an AD RMS Application
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Developing an AD RMS Application

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Developing an application by using the Active Directory Rights Management (AD RMS) SDK typically requires a public key pair and a pre-production certificate chain that leads back to a Microsoft certificate at the root of trust. Beginning with RMS 1.0 SP2 and Windows Vista, the public and private keys and the pre-production certificate are included with the SDK in the following files located in the *InstallPath*\\Bin folder.

| File name                      | Description                                                                                                 |
|--------------------------------|-------------------------------------------------------------------------------------------------------------|
| ISVTier5AppSigningPrivKey.dat  | Contains the private key used to sign a manifest for use during application development.                    |
| ISVTier5AppSIgningPubKey.dat   | Contains the public key signed into the pre-production certificate hierarchy.                               |
| ISVTier5AppSignSDK\_Client.xml | Contains the pre-production certificate used to generate a manifest for use during application development. |



 

You use the certificate and the private key to create and sign a manifest that identifies the files that can or must be loaded into the process space of your application and those that must not be loaded. The manifest is, in turn, used by the lockbox, which is software that protects the security of the process in which your application runs and the content consumed or published by your application.

Although it is possible to create an application that does not require a lockbox (or a manifest or a pre-production certificate) doing so is a legacy solution that is not typical and not recommended. Most applications developed by using this SDK use a lockbox.

Whether or not you have used a pre-production certificate during application development, when you are ready to release the application, you must generate a new key pair, acquire a production certificate from Microsoft and use the new private key and certificate to create and sign an application manifest. For more information, see [Releasing an AD RMS Application](releasing-an-ad-rms-application.md).

## Related topics

<dl> <dt>

[Application Licensing Information](application-licensing-information.md)
</dt> </dl>

 

 



