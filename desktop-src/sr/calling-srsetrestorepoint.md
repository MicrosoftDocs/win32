---
title: Calling SRSetRestorePoint
description: An application can create a restore point before it causes a significant system change, such as an installation, uninstallation, or update.
ms.assetid: 77981e75-8c3f-4ecc-82f4-e88d68df661a
ms.topic: concept-article
ms.date: 05/31/2018
---

# Calling SRSetRestorePoint

An application can create a restore point before it causes a significant system change, such as an installation, uninstallation, or update.

Installers should create a restore point before installation by calling the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function with the `dwEventType` member of the [`RESTOREPOINTINFO`](/windows/win32/api/srrestoreptapi/ns-srrestoreptapi-restorepointinfoa) structure set to `BEGIN_SYSTEM_CHANGE`. To notify System Restore that the installation has been completed, call **SRSetRestorePoint** with `dwEventType` set to `END_SYSTEM_CHANGE`.

If the user cancels the application installation, the installer may remove the restore point it created when the installation began. Removing the restore point is optional and can prevent the user from recovering from unintentional changes made by the installer during the cancellation. If the installer is to remove a restore point, it can call the [**SRRemoveRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srremoverestorepoint) function, or call [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) with `dwRestorePointType` set to `CANCELLED_OPERATION`, `dwEventType` set to `END_SYSTEM_CHANGE`, and `llSequenceNumber` set to the value returned by the initial call to **SRSetRestorePoint**.

Starting with Windows 8, developers can write applications that create the DWORD value **SystemRestorePointCreationFrequency** under the `HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore` registry key. The value of this registry key can change the frequency of restore point creation. By default, this key doesn't exist.

When an application calls the **SRSetRestorePoint** function to create a restore point, one of the following happens depending on the contents of the key:

- If the key does not exist (default) and any restore points have been created in the last 24 hours, Windows skips creating this new restore point. System Restore sets the `IISequenceNumber` member of the [`STATEMGRSTATUS`](/windows/win32/api/srrestoreptapi/ns-srrestoreptapi-statemgrstatus) structure to the sequence number for the restore point created previously in the day and sets the value of the `nStatus` member to `ERROR_SUCCESS`. The **SRSetRestorePoint** function returns `TRUE`.

- If the registry key value is 0, system restore does not skip creating the new restore point.

- If the registry key value is the integer N, system restore skips creating a new restore point if any restore points were created in the previous N minutes.

System Restore running on Windows 8 monitors files in the boot volume that are relevant for system restore only. Snapshots of the boot volume created by System Restore running on Windows 8 may be deleted if the snapshot is subsequently exposed by an earlier version of Windows. Note that although there is only one system volume, there is one boot volume for each operating system in a multi-boot system.

Developers can write applications that create the DWORD value **ScopeSnapshots** under the `HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore` registry key. If this registry key value is 0, System Restore creates snapshots of the boot volume in the same way as in earlier versions of Windows. If this value is deleted, System Restore running on Windows 8 resumes creating snapshots that monitor files in the boot volume that are relevant for system restore only.

For an example, see [Using System Restore](using-system-restore.md).

 

 




