---
description: If the value of this per-machine system policy is set to &\#0034;2&\#0034; the installer is always disabled for all applications. If this policy value is set to &\#0034;1&\#0034;, the installer is disabled for unmanaged applications but is still enabled for managed applications.
ms.assetid: 7f941559-54c3-4802-b827-5954bd4669f8
title: DisableMSI
ms.topic: article
ms.date: 05/31/2018
---

# DisableMSI

If the value of this per-machine [system policy](system-policy.md) is set to "2" the installer is always disabled for all applications. If this policy value is set to "1", the installer is disabled for unmanaged applications but is still enabled for managed applications.

The following table lists the possible configurations.



| DisableMSI | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Default*  | On Windows Server 2003, Windows Server 2003 R2, Windows Server 2008, and Windows Server 2008 R2, if the policy value is Null, absent, or any number other than 1 or 2, the Windows Installer is enabled for managed applications. Unmanaged application installs are blocked.<br/> On Windows XP, Windows Vista, and Windows 7, the Windows Installer is enabled for all applications. All install operations are allowed.<br/> |
| 0          | Windows Installer is enabled for all applications. All install operations are allowed.                                                                                                                                                                                                                                                                                                                                                      |
| 1          | The Windows Installer is disabled for unmanaged applications but is still enabled for managed applications. Non-elevated per-user installations are blocked. Per-user elevated and per-machine installs are allowed.                                                                                                                                                                                                                        |
| 2          | Windows Installer is always disabled for all applications. No installs are allowed including repairs, reinstalls, or on-demand installations.                                                                                                                                                                                                                                                                                               |



 

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




