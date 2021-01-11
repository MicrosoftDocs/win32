---
title: Registry Keys and Values for Backup and Restore
ms.assetid: 83449f78-cca1-449b-8c5f-3c8a91c8b3e7
description: "Learn more about: Registry Keys and Values for Backup and Restore"
keywords:
- backup Backup , registry keys
- registry keys Backup
- CustomPerformanceSettings Backup
- DisableMonitoring Backup
- FilesNotToBackup Backup
- FilesNotToSnapshot Backup
- KeysNotToRestore Backup
- LastInstance Backup
- LastRestoreId Backup
- MaxShadowCopies Backup
- MinDiffAreaFileSize Backup
- OverallPerformanceSetting Backup
- SYSVOL Backup
ms.topic: article
ms.date: 05/31/2018
---

# Registry Keys and Values for Backup and Restore

Applications that request or perform backup and restore operations should use the following registry keys and values to communicate with each other or with features such as the [Volume Shadow Copy Service (VSS)](/windows/desktop/VSS/volume-shadow-copy-service-portal) and Windows Backup:

-   [CustomPerformanceSettings](#customperformancesettings)
-   [DisableMonitoring](#disablemonitoring)
-   [FilesNotToBackup](#filesnottobackup)
-   [FilesNotToSnapshot](#filesnottosnapshot)
-   [IdleTimeout](#idletimeout)
-   [KeysNotToRestore](#keysnottorestore)
-   [LastInstance](#lastinstance)
-   [LastRestoreId](#lastrestoreid)
-   [MaxShadowCopies](#maxshadowcopies)
-   [MinDiffAreaFileSize](#mindiffareafilesize)
-   [OverallPerformanceSetting and CustomPerformanceSettings](#overallperformancesetting-and-customperformancesettings)
-   [SYSVOL](#sysvol)

## CustomPerformanceSettings

See [OverallPerformanceSetting and CustomPerformanceSettings](#overallperformancesetting-and-customperformancesettings).

## DisableMonitoring

On Windows client platforms beginning with Windows 7, users are automatically prompted to configure the Windows Backup feature if they have not already done so. These notifications appear at computer startup time, beginning seven days after the operating system is installed. They also appear when the user plugs in a hard disk drive; in this case, the notifications appear immediately.

OEMs and developers of third-party backup applications can use the **DisableMonitoring** registry value to turn off these automatic notifications.

This value does not exist by default, so it must be created under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**WindowsBackup**

The **DisableMonitoring** registry value has the data type REG\_DWORD and is interpreted as follows:

-   If the value's data is set to 1 and if users have not already configured the Windows Backup feature, the automatic notifications are turned off. If an automatic notification is already present in Action Center, setting this registry value causes the notification to be removed at 10:00 the following morning.
-   If the value does not exist, if its data is not set, or if its data is set to zero, the automatic notifications are not turned off.

**Windows Vista and Windows XP:** This registry value is not supported.

## FilesNotToBackup

The **FilesNotToBackup** registry key specifies the names of the files and directories that backup applications should not backup or restore. Each of the entries in this key is a REG\_MULTI\_SZ string in the following format:

\[*Drive*\]\[*Path*\]\\*FileName* \[/s\]

-   *Drive* specifies the drive and is optional. For example, c:. To specify all drives, use a backslash (\); no drive letters are needed.
-   *Path* specifies the path and is optional. It cannot contain wildcard characters.
-   *FileName* specifies the file or directory and is required. It can contain wildcard characters.
-   /s specifies that all subdirectories of the specified path are to be included.
-   Environment variables such as %Systemroot% can be substituted for all or part of the entire string.

The following table shows some typical entries.

| Entry name                             | Default value                                                                             |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| Internet Explorer                      | Temporary Files                                                                           |
| Memory Page File                       | \\Pagefile.sys                                                                            |
| MS Distributed Transaction Coordinator | C:\\Windows\\system32\\MSDtc\\MSDTC.LOG C:\\Windows\\system32\\MSDtc\\trace\\dtctrace.log |
| Offline Files Cache                    | %Systemroot%\\CSC\\\* /s                                                                  |
| Power Management                       | \\hiberfil.sys                                                                            |
| Single Instance Storage                | \\SIS Common Store\\\*.\* /s                                                              |
| Temporary Files                        | %TEMP%\\\* /s                                                                             |



 

> [!Note]  
> Applications that perform volume-level backups generally do so by copying the entire volume at the block level, so they cannot honor the **FilesNotToBackup** registry key at backup time. Instead, they wait until restore time to delete the files that were not to be backed up. In most cases, this is a reasonable strategy. However, in the case of Single Instance Storage files, the SIS Common Store files must not be deleted at restore time.

 

For block-level volume backups, Windows Server Backup and the Windows Wbadmin utility honor the **FilesNotToBackup** registry key by deleting the appropriate files at restore time. System Restore and System State Backup do not honor the **FilesNotToBackup** registry key.

**Windows XP:** System Restore honors the **FilesNotToBackup** registry key.

## FilesNotToSnapshot

VSS supports the **FilesNotToSnapshot** registry key. Applications and services can use this key to specify files to be deleted from newly created shadow copies. For more information, see [Excluding Files from Shadow Copies](/windows/desktop/VSS/excluding-files-from-shadow-copies).

**Windows Server 2003 and Windows XP:** This registry key is not supported.

For block-level volume backups, Windows Server Backup honors the **FilesNotToSnapshot** registry key by deleting the appropriate files at restore time.

## IdleTimeout

The **IdleTimeout** registry value specifies the amount of time, in seconds, that the VSS service will wait when it is idle. If this timeout value is reached and there are no tasks for it to perform, the VSS service will shut down.

This registry value can be found under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**VSS**\\**Settings**

If this registry value does not exist:

-   The actual timeout value that is used is 180 seconds (3 minutes) by default.
-   You can create a value with the name **IdleTimeout** and the type DWORD and set it to the desired value.

If this registry value is set to 0 seconds:

-   The actual timeout value that is used is 180 seconds (3 minutes).

If you set this registry value:

-   VSS uses the timeout value that you set.
-   You can specify any value between 1 and FFFFFFFF seconds. However, it is recommended that you choose a value between 1 and 180 seconds.

**Windows Server 2003 and Windows XP:** This registry key is not supported.

## KeysNotToRestore

The **KeysNotToRestore** registry key specifies the names of the registry subkeys and values that backup applications should not restore. For more information, see [KeysNotToRestore](/previous-versions/windows/it-pro/windows-server-2003/cc737538(v=ws.10)). It is not necessary to honor the **KeysNotToRestore** registry key.

**Windows Server 2003 and Windows XP:** You must honor the **KeysNotToRestore** registry key.

For block-level volume backups, Windows Server Backup honors the **KeysNotToRestore** registry key by deleting the appropriate files at restore time.

System State Backup honors the **KeysNotToRestore** registry key.

## LastInstance

The **LastInstance** registry value indicates that a bare-metal restore operation has been performed and that the volumes have been overwritten but not formatted. For more information, see [Using VSS Automated System Recovery for Disaster Recovery](/windows/desktop/VSS/using-vss-automated-system-recovery-for-disaster-recovery).

**Windows Server 2003 and Windows XP:** This registry value is not supported.

## LastRestoreId

When a backup application performs a system state restore, it must indicate that it has done so by setting the **LastRestoreId** registry value. "System state restore" in this case refers to any restore that selectively restores operating system binaries and drivers.

If the entire boot and system volume are restored at the volume level, this value must not be set.

If the **LastRestoreId** registry value does not exist, the backup application should create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**BackupRestore**\\**SystemStateRestore**

Create a value with the name **LastRestoreId** and type REG\_SZ. The value should be a unique opaque value such as a GUID.

Whenever a new system state restore is performed, the backup application should change the data of the **LastRestoreId** value.

Other applications that need to monitor system state restores should store the data of this registry value. This data can be compared against the current data of the **LastRestoreId** registry value to determine whether a new system state restore has been performed.

**Windows Vista, Windows Server 2003 and Windows XP:** This registry value is not supported until Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.

## MaxShadowCopies

The **MaxShadowCopies** registry value specifies the maximum number of [*client-accessible shadow copies*](/windows/desktop/VSS/vssgloss-c) that can be stored on each volume of the computer. A client-accessible shadow copy is a shadow copy that is created using the **VSS\_CTX\_CLIENT\_ACCESSIBLE** value of the [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/desktop/api/vss/ne-vss-vss_snapshot_context) enumeration. Client-accessible shadow copies are used by Shadow Copies for Shared Folders. For more information about shadow copies, see the [VSS](/windows/desktop/VSS/volume-shadow-copy-service-portal) documentation.

If the **MaxShadowCopies** registry value does not exist, the backup application can create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**VSS**\\**Settings**

Create a value with the name **MaxShadowCopies** and type DWORD. The default data for this value is 64. The minimum is 1. The maximum is 512.

> [!Note]  
> For other types of shadow copies, there is no registry value that corresponds to **MaxShadowCopies**. The maximum number of shadow copies is 512 per volume.

 

**Note**  The **MaxShadowCopies** setting is supported on Windows Server 2003 or later.

**Windows Server 2003:** On cluster servers, **MaxShadowCopies** registry value's data may need to be set to a lower number. For more information, see "When you use the Volume Shadow Copy Service on Windows Server 2003-based computers that run many I/O operations, disk volumes take longer to go online" in the Help and Support Knowledge Base at [https://support.microsoft.com/kb/945058](https://support.microsoft.com/kb/945058).

**Windows XP:** This registry value is not supported.

## MinDiffAreaFileSize

[VSS](/windows/desktop/VSS/volume-shadow-copy-service-portal) allocates a shadow copy storage area (or "diff area") to store data for shadow copies. The minimum size of the shadow copy storage area is a per-computer setting that can be specified by using the **MinDiffAreaFileSize** registry value.

If the **MinDiffAreaFileSize** registry value is not set, the minimum size of the shadow copy storage area is 32 MB for volumes that are smaller than 500 MB and 320 MB for volumes that are larger than 500 MB.

**Windows Server 2008, Windows Server 2003 with SP1 and Windows Vista:** If the **MinDiffAreaFileSize** registry value is not set, the shadow copy storage area has a minimum size of 300 MB. If the **MinDiffAreaFileSize** registry value is set, its data must be between 300 MB and 3000 MB (3 GB), and it must be a multiple of 300 MB.

**Windows Server 2003:** If the **MinDiffAreaFileSize** registry value is not set, the minimum size of the shadow copy storage area is 100 MB.

**Windows XP:** This registry value is not supported.

If the **MinDiffAreaFileSize** registry value does not exist, the backup application can create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**VolSnap**

Create a value with the name **MinDiffAreaFileSize** and type REG\_DWORD. The data for this key is specified in megabytes. 320 is equal to 320 MB, and 3200 is equal to 3.2 GB. You should specify a number that is a multiple of 32. If you specify a value that is not a multiple of 32, the next multiple of 32 will be used.

Shadow copies might not function correctly if the **MinDiffAreaFileSize** registry value specifies a minimum size that is larger than the maximum size of the shadow copy storage area. To specify the maximum size of the shadow copy storage area, use the [Vssadmin](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754968(v=ws.11)) add shadowstorage or the Vssadmin resize shadowstorage command. To see the current maximum size, use the [Vssadmin list shadowstorage](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754968(v=ws.11)) command. If you have not set a maximum size, there is no limit to the amount of space that can be used.

## OverallPerformanceSetting and CustomPerformanceSettings

The **OverallPerformanceSetting** and **CustomPerformanceSettings** registry values are used to specify performance settings for Windows Server Backup. These registry values are supported only on Windows server operating systems.

**Windows Server 2003:** These registry values are not supported.

If these registry values do not exist, the backup application can create them under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Windows Block Level Backup**

To specify performances settings for all volumes, create a value with the name **OverallPerformanceSetting** and type REG\_DWORD. The value's data should be set to one of the following values.

| Value | Meaning                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Normal backup performance (by using full backups). This setting corresponds to the Normal backup performance setting described in [Optimizing Backup and Server Performance](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd759145(v=ws.11)).            |
| 2     | Faster backup performance (by using incremental backups). This setting corresponds to the Faster backup performance setting described in [Optimizing Backup and Server Performance](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd759145(v=ws.11)).     |
| 3     | Custom backup performance (by specifying a performance setting for each volume). This setting corresponds to the Custom setting described in [Optimizing Backup and Server Performance](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd759145(v=ws.11)). |



 

If you set **OverallPerformanceSetting** to 3, you must also specify performances settings for each volume individually. To do this, create a value with the name **CustomPerformanceSettings** and type REG\_MULTI\_SZ. This value's data should be set as follows:

-   Each string in the REG\_MULTI\_SZ sequence of strings contains the setting for a volume.
-   Each string consists of a volume GUID, followed by a comma, followed by a DWORD value.
-   Each of the DWORD values is either 1 (full backup) or 2 (incremental backup).

For example, suppose the computer has two volumes as follows:

-   The two volumes are C:\\ and D:\\.
-   The GUID for volume C:\\ is 07c473ca4-2df8-11de-9d80-806e6f6e6963, and the GUID for volume D:\\ is 0ac22ea6c-712f-11de-adb0-00215a67606e.
-   You want to specify normal backup perfornance for volume C:\\ and faster backup performance for volume D:\\.

To do this, you would set **OverallPerformanceSetting** to 3 and **CustomPerformanceSettings** to "07c473ca4-2df8-11de-9d80-806e6f6e6963,1\\00ac22ea6c-712f-11de-adb0-00215a67606e,2".

If you set **OverallPerformanceSetting** to 1 or 2, the data in the **CustomPerformanceSettings** value is ignored.

## SYSVOL

The **SYSVOL** registry value is a way to notify the Distributed File System Replication (DFSR) service that a system state restore operation has been initiated. Any backup application that performs system state restore of SYSVOL should use this value to indicate whether the restore operation is authoritative or nonauthoritative. This value is read by the DFSR service. If this value is not set, the SYSVOL restore is performed nonauthoritatively by default.

If the **SYSVOL** registry value does not exist, the backup application should create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**DFSR**\\**Restore**

Create a value with the name **SYSVOL** and type REG\_SZ. The value's data should be set to either "authoritative" or "non-authoritative" based on the system administrator's request.

**Windows Vista, Windows Server 2003 and Windows XP:** This registry value is not supported.

 

 
