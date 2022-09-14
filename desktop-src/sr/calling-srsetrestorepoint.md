---
title: Calling SRSetRestorePoint
description: An application can create a restore point before it causes a significant system change, such as an install, uninstall, or feature update.
ms.assetid: 77981e75-8c3f-4ecc-82f4-e88d68df661a
ms.topic: article
ms.date: 05/31/2018
---

# Calling SRSetRestorePoint

An application can create a restore point before it causes a significant system change, such as an install, uninstall, or feature update.

Installers should create a restore point just prior to installation by calling the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function with the **dwEventType** member of the [**RESTOREPOINTINFO**](/windows/win32/api/srrestoreptapi/ns-srrestoreptapi-restorepointinfoa) structure set to BEGIN\_SYSTEM\_CHANGE. To notify System Restore that the installation has been completed, call **SRSetRestorePoint** with **dwEventType** set to END\_SYSTEM\_CHANGE.

If the user cancels the application installation, the installer may remove the restore point it created when the installation began. Removing the restore point is optional and can prevent the user from recovering from unintentional changes made by the installer during the cancellation. If the installer is to remove a restore point, it can call the [**SRRemoveRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srremoverestorepoint) function, or call [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) with **dwRestorePointType** set to CANCELLED\_OPERATION, **dwEventType** set to END\_SYSTEM\_CHANGE, and **llSequenceNumber** set to the value returned by the initial call to **SRSetRestorePoint**.

**Windows 8:  **

A new registry key enables application developers to change the frequency of restore-point creation.

Applications should create this key to use it because it will not preexist in the system. The following will apply by default if the key does not exist. If an application calls the **SRSetRestorePoint** function to create a restore point, Windows skips creating this new restore point if any restore points have been created in the last 24 hours. System Restore sets the **IISequenceNumber** member of the [**STATEMGRSTATUS**](/windows/win32/api/srrestoreptapi/ns-srrestoreptapi-statemgrstatus) structure to the sequence number for the restore point created previously in the day and sets the value of the **nStatus** member to **ERROR\_SUCCESS**. The **SRSetRestorePoint** function returns **TRUE**.

Developers can write applications that create the **DWORD** value **SystemRestorePointCreationFrequency** under the registry key **HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore**. The value of this registry key can change the frequency of restore point creation. The value of this registry key can change the frequency of restore point creation.

If the application calls **SRSetRestorePoint** to create a restore point, and the registry key value is 0, system restore does not skip creating the new restore point.

If the application calls **SRSetRestorePoint** to create a restore point, and the registry key value is the integer N, system restore skips creating a new restore point if any restore points were created in the previous N minutes.

**Windows 8:  **

System Restore running on Windows 8 monitors files in the boot volume that are relevant for system restore only. Snapshots of the boot volume created by System Restore running on Windows 8 may be deleted if the snapshot is subsequently exposed by an earlier version of Windows. Note that although there is only one system volume, there is one boot volume for each operating system in a multi-boot system.

Developers can write applications that create the **DWORD** value **ScopeSnapshots** under the registry key **HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore**. If this registry key value is 0, System Restore creates snapshots of the boot volume in the same way as in earlier versions of Windows. If this value is deleted, System Restore running on Windows 8 resumes creating snapshots that monitor files in the boot volume that are relevant for system restore only.

For an example, see [Using System Restore](using-system-restore.md).

 

 




