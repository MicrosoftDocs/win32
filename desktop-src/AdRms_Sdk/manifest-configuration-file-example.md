---
Description: The following example shows a basic manifest configuration file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9559ddd6-3d0c-47dd-a5c2-f041f878fe48
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Manifest Configuration File Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Manifest Configuration File Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows a basic manifest configuration file.

``` syntax
AUTO-GUID

"C:\\myfolder\\TestSigningKeyPriv.dat"

MODULELIST
    REQ HASH "C:\\Development Programs\\My Program.exe"
    REQ NOHASH "C:\\Windows\\system32\\msdrm.dll"

POLICYLIST
    INCLUSION
        PUBLICKEY "C:\\myfolder\\TestSigningKeyPub.dat"
    EXCLUSION
```

## Example Highlights

For more information about the elements used in a configuration file, see [Manifest Configuration File Syntax](manifest-configuration-file-syntax.md). Note the following points about the preceding example:

-   TestSigningKeyPriv.dat is the name of the file that contains the private key used to sign the manifest. For more information, see [Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md).
-   TestSigningKeyPub.dat is the name of the file that contains the public key associated with the private key.
-   The application name is specified in the MODULELIST element and associated with the **REQ HASH** element. Quotation marks are used because there is a space in the application name. The quotation marks used elsewhere in the configuration file are not required.
-   The **NOHASH** element indicates that the Msdrm.dll library is not hashed. This enables you to incorporate updated versions of Msdrm.dll without creating a new manifest.

## Creating a Manifest

Save the configuration file with an .mcf extension and call the Genmanifest.exe command–line program by using the following syntax:

**genmanifest** \[**-chain** *SignedChainPathAndFile*\] *SourceMCFPath* *DestinationXMLPath*

For more information, see [Genmanifest.exe](genmanifest-exe.md). You must generate a new manifest each time you compile your program, and the manifest can contain only one executable file. This file must own the process that is running Active Directory Rights Management.

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> <dt>

[Manifest Configuration File Syntax](manifest-configuration-file-syntax.md)
</dt> <dt>

[Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md)
</dt> <dt>

[Authenticode Signing Included Modules](authenticode-signing-included-modules.md)
</dt> </dl>

 

 



