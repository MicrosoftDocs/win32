---
title: Restoring the System
description: As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user.
ms.assetid: 9581eff5-44d0-407e-b7cb-d3e13910a936
ms.topic: article
ms.date: 05/31/2018
---

# Restoring the System

As the computer is used over time, restore points are collected in the data archive without any management or intervention required by the user. If the user ever needs to restore the system to a previous state, the available restore points are made visible to the user through the System Restore user interface. The user can choose any of these restore points. The only way to access this archive of restore points is through the System Restore user interface and the System Restore API; this is to protect data integrity and prevent accidental changes made by the user, applications, or other agents.

To restore a system, System Restore undoes file changes made to monitored files, recapturing the file state at the time of the selected restore point. It then replaces the current registry with the one saved for the selected restore point.

To ensure that your application has the desired behavior after a restore, do the following:

-   Do not store information in the registry that prevents user access to personal data files or applications on system restore. Otherwise, you must provide a mechanism by which the user can download and reinstall the applications without having to pay for them again.
-   Use the [System Restore API](system-restore-api.md) to create meaningful restore points at install and uninstall.
-   In Windows XP, the key application binaries to be protected must use extensions consistent with those used in Filelist.xml. For more information, see [Monitored File Name Extensions](monitored-file-extensions.md). This file is not used by Windows 7 and Windows Vista. Do not use monitored extension types for user-editable files. For example, if you name a user's personal data file using the extension .ini, the user may lose work as a result of a system restore.

 

 




