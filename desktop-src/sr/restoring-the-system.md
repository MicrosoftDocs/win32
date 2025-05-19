---
title: Restoring the System
description: As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user.
ms.assetid: 9581eff5-44d0-407e-b7cb-d3e13910a936
ms.topic: concept-article
ms.date: 05/02/2025
# Customer intent: As a Windows developer, I want to understand how System Restore works so that I can create applications that are compatible with it.
---

# Restoring the system

As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user.

**After installing the June 2025 Windows security update, devices running Windows 11, version 24H2 and Windows Server 2025** will have restore points up to the previous 60 days. These points are accessible through the System Restore user interface. As a security measure, restoring Windows with restore points older than 60 days will not be possible for these client and server versions of Windows. Future versions of Windows will also be able to access restore points that are up to 60 days old All versions of Windows Server and Windows client released prior to Windows Server 2025 and Windows 11, version 24H2 will support restore points without the 60-day limitation.

The only way to access this archive of restore points is through the System Restore user interface and the System Restore API; this is to protect data integrity and prevent accidental changes made by the user, applications, or other agents.

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
