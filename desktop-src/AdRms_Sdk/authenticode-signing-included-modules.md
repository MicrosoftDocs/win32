---
Description: You can specify Microsoft Authenticode-signed modules in a manifest by designating your DLLs with the NOHASH tag in the MODULELIST section, and including the Microsoft code-signing root public key in the INCLUSION section.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ce7f3b9a-cf70-4a5b-bffc-bc9774e3da25
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Authenticode Signing Included Modules
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Authenticode Signing Included Modules

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can specify Microsoft Authenticode-signed modules in a manifest by designating your DLLs with the **NOHASH** tag in the **MODULELIST** section, and including the Microsoft code-signing root public key in the **INCLUSION** section. For more information about these elements, see [Manifest Configuration File Syntax](manifest-configuration-file-syntax.md).

> [!Note]  
> Third-party Authenticode-signed modules are not supported.

 

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> </dl>

 

 



