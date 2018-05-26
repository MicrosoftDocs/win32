---
Description: Genmanifest.exe is a command-line program that creates a manifest.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6d21fa54-253c-45ff-8ac4-15a9834fd23f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Genmanifest.exe
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Genmanifest.exe

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Genmanifest.exe is a command-line program that creates a [*manifest*](m-gly.md#-rm-manifest-gly). The syntax is

**genmanifest** \[**-chain** *SignedChainPathAndFile*\] *SourceMCFPath* *DestinationXMLPath*

where:

-   **-chain** *SignedChainPathAndFile* contains the path of the signed Pre-production or Production certificate. If you are using the Pre-production environment on Windows Server 2008, use the ISVTier5AppSignSDK\_Client.xml file located in the *SDKInstallPath*\\Bin folder. Before you can switch to the Production hierarchy, however, you must apply for a Production License Agreement and request a Production certificate from Microsoft. For more information, see [Requesting a Production License Agreement](requesting-a-production-license-agreement.md).
    > [!Note]  
    > Although the syntax specifies that this argument is optional, it is in fact required for all practical purposes.

     

-   *SourceMCFPath* contains the path of the manifest configuration file. This file has a .mcf extension.
-   *DestinationXMLPath* contains the path of the generated XrML manifest file. Give the file a .xml extension.

The following example uses the Pre-production certificate and a manifest configuration file named MCF\_in.mcf to create a signed XrML manifest in the Man\_out.xml file.

**c:\\&gt;genmanifest.exe -chain ISVTier5AppSignSDK\_Client.xml MCF\_in.mcf Man\_out.xml**

## Related topics

<dl> <dt>

[Create an Application Manifest](create-an-application-manifest.md)
</dt> <dt>

[Manifest Configuration File Example](manifest-configuration-file-example.md)
</dt> <dt>

[Manifest Configuration File Syntax](manifest-configuration-file-syntax.md)
</dt> </dl>

 

 



