---
Description: The manifest requires a public key pair. The private key is used to sign the manifest, and the associated public key is contained in a Pre-production or Production certificate signed by Microsoft.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dc14295d-54f6-4dcd-b7ca-862629bf2b04
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Obtaining a Key Pair for Manifest Signing
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Key Pair for Manifest Signing

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The manifest requires a public key pair. The private key is used to sign the manifest, and the associated public key is contained in a Pre-production or Production certificate signed by Microsoft.

## Obtaining a Pre-Production Key Pair and Certificate

To develop an AD RMS-enabled application, you must have a public key pair and a Pre-production certificate. The Pre-production key pair is included with the AD RMS SDK in the \\Bin folder of the SDK installation path. The private key is in the ISVTier5AppSigningPrivKey.dat file, and the public key is in ISVTier5AppSIgningPubKey.dat.

The SDK also includes a certificate that signs the public key into the Pre-production chain. The encoded certificate is in the ISVTier5AppSignSDK\_Client.xml file in the \\Bin folder. Also in that folder are two files, ISVTier5AppSignSDK.cc and ISVTier5AppSignSDK.xml, that will enable you to understand the structure of the encoded certificate.

## Obtaining a Production Key Pair and Certificate

A developer can use the Sn.exe program installed with Visual Studio 2005 to produce the key pair. This program is also available with the Microsoft .NET Framework, which can be obtained from the Microsoft website at no charge.

1.  Locate the Sn.exe program on your computer.

2.  In a Command window, navigate to the same folder that contains Sn.exe, and then type the following command to create a file, *MyPrivateKeyFile.dat*, that contains a public and a private key.

    **sn.exe** **-k** *MyPrivateKeyFile.dat*

3.  Separate the public and private keys into different files by using the following command. The file names must end with the **.dat** extension.

    **sn.exe** **-p** *MyPrivateKeyFile.dat* *MyPublicKeyFile.dat*

> \[!Important\]  
> You must also have your public key signed by Microsoft, to use as an input parameter for Genmanifest.exe. For more information about having your public key signed, see [Requesting a Production License Agreement](requesting-a-production-license-agreement.md).

 

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> </dl>

 

 



