---
Description: When you are ready to switch from the Pre-production to the Production hierarchy, you must configure the registry on the client as shown.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2da68028-f17d-40c9-b949-a00b144f9d43
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Production Client Settings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Production Client Settings

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

When you are ready to switch from the Pre-production to the Production hierarchy, you must configure the registry on the client as shown.

## Production Client Settings

If you are running a 32-bit client on a 32-bit operating system or a 64-bit client on a 64-bit operating system, set the following **REG\_DWORD** value to zero (0).

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**uDRM**\\    **Hierarchy** = 0x00000000

If you are running a 32-bit client on a 64-bit operating system, set the following **REG\_DWORD** value to zero (0).

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Wow6432Node**\\**Microsoft**\\**uDRM**\\**Hierarchy** = 0x00000000

Because the client uses the same license store for both the Production and Pre-production hierarchy, you should restore the client machine to a clean state each time you switch between Production and Pre-production hierarchies. For more information, see [Restoring a Client Computer to a Clean State](restoring-a-client-computer-to-a-clean-state.md).

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> <dt>

[Switching to the Production Environment](switching-to-the-production-environment.md)
</dt> </dl>

 

 



