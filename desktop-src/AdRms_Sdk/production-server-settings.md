---
Description: To specify that you are using the Production certificate hierarchy, set the following registry value(s) before installing the AD RMS service (Windows Server 2008 R2 and Windows Server 2008) or after installation but before provisioning (Windows Server 2003).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 66bdd570-b0b0-41c2-8d76-a5d7bab8abd8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Production Server Settings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Production Server Settings

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

To specify that you are using the Production certificate hierarchy, set the following registry value(s) before installing the AD RMS service (Windows Server 2008 R2 and Windows Server 2008) or after installation but before provisioning (Windows Server 2003).

-   If you are using AD RMS on Windows Server 2008 R2, you must set the following **REG\_DWORD** value to zero (0) to switch to the Production hierarchy.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**Hierarchy** = 0x00000000

-   If you are using AD RMS on Windows Server 2008 R2 and you previously set the following **REG\_SZ** value so that your Pre-production AD RMS server would be compatible with RMS 1.0 clients, remove this value before you switch to the Production chain.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

-   If you are using AD RMS on Windows Server 2008 R2 and you set the following empty string because another AD RMS service was already deployed in Active Directory as a Pre-production Service, remove this value.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**GICURL** = ""

-   If you are using AD RMS on Windows Server 2008, you must set the following **REG\_DWORD** value to zero (0) to switch to the Production hierarchy.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**2.0**\\**Hierarchy** = 0x00000000

-   If you are using AD RMS on Windows Server 2008 and you previously set the following **REG\_SZ** value so that your Pre-production AD RMS server would be compatible with RMS 1.0 clients, remove this value before you switch to the Production chain.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**2.0**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

-   If you are using AD RMS on Windows Server 2008 and you set the following empty string because another AD RMS service was already deployed in Active Directory as a Pre-production Service, remove this value.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**2.0**\\**GICURL** = ""

-   If you are using RMS 1.0 SP2 with Windows Server 2003 or earlier, and you added the following **REG\_SZ** value to work in the Pre-production chain, you should remove it before switching to the Production hierarchy.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

-   If you are using RMS 1.0 SP2 with Windows Server 2003 or earlier, and you added the following empty string value because another AD RMS service was already deployed in Active Directory as a Pre-production Service, you should remove this value from the registry.

    **Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**GICURL** = ""

## Related topics

<dl> <dt>

[Production Client Settings](production-client-settings.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> <dt>

[Switching to the Production Environment](switching-to-the-production-environment.md)
</dt> </dl>

 

 



