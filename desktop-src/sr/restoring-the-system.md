---
title: Restoring the System
description: As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user.
ms.assetid: 9581eff5-44d0-407e-b7cb-d3e13910a936
ms.topic: concept-article
ms.date: 07/13/2026
# Customer intent: As a Windows developer, I want to understand how System Restore works so that I can create applications that are compatible with it.
---

# Restoring the system

As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user.

After installing the July 2026 Windows security update, devices running Windows 11, versions 24H2, 25H2, and 26H1, and Windows Server 2025 can restore from restore points that pass the required security checks while Virtualization-Based Security (VBS) is enabled and running. To pass the security check, a restore point must meet the minimum VBS CI Policy requirement or, when the VBS CI Policy version cannot be compared, fall within the 60-day limitation. For more information about VBS CI Policy, see [Code integrity](/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity) and [Virtualization-based Security (VBS)](/windows/security/identity-protection/credential-guard/how-it-works#virtualization-based-security-vbs).

As a security measure, restoring Windows from restore points that do not meet the required security checks is not possible on these versions of Windows. Future versions of Windows will be able to access only restore points that pass the required security checks.

All versions of Windows Server and Windows client released before Windows Server 2025 and Windows 11, version 24H2, will continue to support restore points without these security requirements. To access restore points that do not meet the required security checks, you must disable Virtualization-Based Security (VBS).

To restore a system, System Restore undoes file changes made to monitored files, recapturing the file state at the time of the selected restore point. It then replaces the current registry with the one saved for the selected restore point.

## System restore and application behavior

To ensure that your application has the desired behavior after a restore, do the following:

- Do not store information in the registry that prevents user access to personal data files or applications on system restore. Otherwise, you must provide a mechanism by which the user can download and reinstall the applications without having to pay for them again.
- Use the [System Restore API](system-restore-api.md) to create meaningful restore points at install and uninstall.
- In Windows XP, the key application binaries to be protected must use extensions consistent with those used in Filelist.xml. For more information, see [Monitored File Name Extensions](monitored-file-extensions.md). This file is not used by Windows 7 and Windows Vista. Do not use monitored extension types for user-editable files. For example, if you name a user's personal data file using the extension .ini, the user may lose work as a result of a system restore.

## Related content

- [System Restore API](system-restore-api.md)
- [Monitored File Name Extensions](monitored-file-extensions.md)
- [About System Restore](about-system-restore.md)
