---
Description: A manifest is a certificate that signs your application into the Active Directory Rights Management Services (AD RMS) Pre-production or Production hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8e9cd891-49d3-421a-a225-08e0e7a8c6b0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Application Manifests
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Application Manifests

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A manifest is a certificate that signs your application into the Active Directory Rights Management Services (AD RMS) Pre-production or Production hierarchy. It is used primarily to protect your application from viruses. By specifying required, optional, and prohibited files, the manifest enables you to control what is loaded into the process space and what is allowed to access protected content. This increases security by helping to prevent viruses from running in the same space as your application and by preventing an attacker from replacing libraries.

You create a manifest by first creating a configuration file and then calling the Genmanifest.exe program, providing the configuration file and the Pre-production or Production certificate as input. The configuration identifies your application and other applications or modules that can, cannot be, and must be included in the process space. The following example shows a basic configuration file.

``` syntax
AUTO-GUID

%MYBASEPATH%\\keys\\mypriv1024.dat

MODULELIST
  REQ HASH MyApp.exe
  REQ NOHASH %SystemRoot%\\system32\\kernel32.dll
  OPT     %SystemRoot%\\system32\\msvcrt.dll


POLICYLIST
  INCLUSION
       PUBLICKEY     C:\\mypub1024.dat

  EXCLUSION
       DIG          C:\\ecsrv.dll
       DIG          C:\\ud.dll
       PUBLICKEY     C:\\SampleExcPubKey.dat
       FILE          MyApp.exe 5.1.3500.0 5.1.3572.0
```

For more information about application manifests, see the following topics:

-   [Creating an Application Manifest](creating-an-application-manifest.md)
-   [Manifest Configuration File Syntax](manifest-configuration-file-syntax.md)
-   [Manifest Configuration File Example](manifest-configuration-file-example.md)
-   [Genmanifest.exe](genmanifest-exe.md)
-   [Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md)

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



