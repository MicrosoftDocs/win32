---
Description: A VSS backup-and-recovery application that performs disaster recovery (also called bare-metal recovery) can use the Automated System Recovery (ASR) writer together with Windows Preinstallation Environment (Windows PE) to back up and restore critical volumes and other components of the bootable system state. The backup application is implemented as a VSS requester.
ms.assetid: 13adfd79-f26a-4385-9b59-129d06fa72eb
title: Using VSS Automated System Recovery for Disaster Recovery
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using VSS Automated System Recovery for Disaster Recovery

A VSS backup-and-recovery application that performs disaster recovery (also called bare-metal recovery) can use the Automated System Recovery (ASR) writer together with Windows Preinstallation Environment (Windows PE) to back up and restore critical volumes and other components of the bootable system state. The backup application is implemented as a VSS requester.

**Note**  Applications that use ASR must license Windows PE.

**Windows Server 2003 and Windows XP:** ASR is not implemented as a VSS writer.

For information about tracing tools that you can use with ASR, see [Using Tracing Tools with VSS ASR Applications](using-tracing-tools-with-vss-asr-applications.md).

**In this article:**

-   [Overview of Backup Phase Tasks](#overview-of-backup-phase-tasks)
-   [Choosing Which Critical Components to Back Up](#choosing-which-critical-components-to-back-up)
-   [Overview of Restore Phase Tasks](#overview-of-restore-phase-tasks)
-   [Excluding All Disks for a Volume](#excluding-all-disks-for-a-volume)

## Overview of Backup Phase Tasks

At backup time, the requester performs the following steps.

> [!Note]  
> All steps are required unless otherwise indicated.

 

1.  Call the [**CreateVssBackupComponents**](/windows/win32/VsBackup/nf-vsbackup-createvssbackupcomponents?branch=master) function to create an instance of the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface and call the [**IVssBackupComponents::InitializeForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup?branch=master) method to initialize the instance to manage a backup.
2.  Call [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master) to set the context for the shadow copy operation.
3.  Call [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master) to configure the backup. Set the *bBackupBootableSystemState* parameter to **true** to indicate that the backup will include a bootable system state.
4.  Choose which critical components in the ASR writer's Writer Metadata Document to back up and call [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master) for each of them.
5.  Call [**IVssBackupComponents::StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master) to create a new, empty shadow copy set.
6.  Call [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master) to initiate asynchronous contact with writers.
7.  Call [**IVssBackupComponents::GetWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata?branch=master) to retrieve the ASR writer's Writer Metadata Document. The writer ID for the ASR writer is BE000CBE-11FE-4426-9C58-531AA6355FC4, and the writer name string is "ASR Writer".
8.  Call [**IVssExamineWriterMetadata::SaveAsXML**](/windows/win32/VsBackup/nf-vsbackup-ivssexaminewritermetadata-saveasxml?branch=master) to save a copy of the ASR writer's Writer Metadata Document.
9.  Call [**IVssBackupComponents::AddToSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset?branch=master) for each volume that can participate in shadow copies to add the volume to the shadow copy set.
10. Call [**IVssBackupComponents::PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master) to notify writers to prepare for a backup operation.
11. Call [**IVssBackupComponents::GatherWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus?branch=master) and [**IVssBackupComponents::GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus?branch=master) (or [**IVssBackupComponentsEx3::GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponentsex3-getwriterstatusex?branch=master)) to verify the status of the ASR writer.
12. At this point, you can query for failure messages that were set by the writer in its [**CVssWriter::OnPrepareBackup**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpreparebackup?branch=master) method. For example code that shows how to view these messages, see [**IVssComponentEx::GetPrepareForBackupFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-getprepareforbackupfailuremsg?branch=master).
13. Call [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master) to create a volume shadow copy.
14. Call [**IVssBackupComponents::GatherWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus?branch=master) and [**IVssBackupComponents::GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus?branch=master) to verify the status of the ASR writer.
15. Back up the data.
16. Indicate whether the backup operation succeeded by calling [**IVssBackupComponents::SetBackupSucceeded**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded?branch=master).
17. Call [**IVssBackupComponents::BackupComplete**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete?branch=master) to indicate that the backup operation has completed.
18. Call [**IVssBackupComponents::GatherWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus?branch=master) and [**IVssBackupComponents::GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus?branch=master). The writer session state memory is a limited resource, and writers must eventually reuse session states. This step marks the writer’s backup session state as completed and notifies VSS that this backup session slot can be reused by a subsequent backup operation.
    > [!Note]  
    > This is only necessary on Windows Server 2008 with Service Pack 2 (SP2) and earlier.

     

19. Call [**IVssBackupComponents::SaveAsXML**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-saveasxml?branch=master) to save a copy of the requester's Backup Components Document. The information in the Backup Components Document is used at restore time when the requester calls the [**IVssBackupComponents::InitializeForRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforrestore?branch=master) method.

## Choosing Which Critical Components to Back Up

In the backup initialization phase, the ASR writer reports the following types of components in its Writer Metadata Document:

-   Critical volumes, such as the boot, system, and Windows Recovery Environment (Windows RE) volumes and the Windows RE partition that is associated with the instance of Windows Vista or Windows Server 2008 that is currently running. A volume is a *critical volume* if it contains system state information. The boot and system volumes are included automatically. The requester must include all volumes that contain system-critical components reported by writers, such as the volumes that contain the Active Directory. System-critical components are marked as "not selectable for backup." In VSS, "not selectable" means "not optional." Thus, the requester is required to back them up as part of system state. For more information, see [Backing Up and Restoring System State](locating-additional-system-files.md). Components for which the VSS\_CF\_NOT\_SYSTEM\_STATE flag is set are not system-critical.
    > [!Note]  
    > The ASR component is a system-critical component that is reported by the ASR writer.

     

-   Disks. Every fixed disk on the computer is exposed as a component in ASR. If a disk was not excluded during backup, it will be assigned during restore and can be re-created and reformatted. Note that during restore, the requester can still re-create a disk that was excluded during backup by calling the [**IVssBackupComponents::SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master) method. If one disk in a dynamic disk pack is selected, all other disks in that pack must also be selected. If a volume is selected because it is a critical volume (that is, a volume that contains system state information), every disk that contains an extent for that volume must also be selected. To find the extents for a volume, use the [**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](fs.ioctl_volume_get_volume_disk_extents) control code.

    > [!Note]  
    > During backup, the requester should include all fixed disks. If the disk that contains the requester's backup set is a local disk, this disk should be included. During restore, the requester must exclude the disk that contains the requester's backup set to prevent it from being overwritten.

     

    In a clustering environment, ASR does not re-create the layout of the cluster's shared disks. Those disks should be restored online after the operating system is restored in the Windows RE.

-   Boot Configuration Data (BCD) store. This component specifies the path of the directory that contains the BCD store. The requester must specify this component and back up all of the files in the BCD store directory. For more information about the BCD store, see [About BCD](bcd.about_bcd).
    > [!Note]  
    > On computers that use the Extended Firmware Interface (EFI), the EFI System Partition (ESP) is always hidden and cannot be included in a volume shadow copy. The requester must back up the contents of this partition. Because this partition cannot be included in a volume shadow copy, the backup can only be performed from the live volume, not from the shadow copy. For more information about EFI and ESP, see [UEFI and Windows](http://go.microsoft.com/fwlink/p/?linkid=86780).

     

The component names use the following formats:

-   For disk components, the format is

    &lt;COMPONENT logicalPath="Disks" componentName="harddisk*n*" componentType="filegroup" /&gt;

    where *n* is the disk number. Only the disk number is recorded. To get the disk number, use the [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](base.ioctl_storage_get_device_number) control code.

-   For volume components, the format is

    &lt;COMPONENT logicalPath="Volumes" componentName="Volume{*GUID*}" componentType="filegroup" /&gt;

    where *GUID* is the volume GUID.

-   For the BCD store component, the format is

    &lt;COMPONENT logicalPath="BCD" componentName="BCD" componentType="filegroup" componentCaption = "This is the path to the boot BCD store and the boot managers...All the files in this directory need to be backed up..."&gt;

    If the system partition has a volume GUID name, this component is selectable. Otherwise, it is not selectable.

    > [!Note]  
    > ASR adds the files to the BCD store component's file group as follows:
    >
    > -   For EFI disks, ASR adds
    >
    >     *SystemPartitionPath*\\EFI\\Microsoft\\Boot\\\*.\*
    >
    >     where *SystemPartitionPath* is the path to the system partition.
    >
    > -   For GPT disks, ASR adds
    >
    >     *SystemPartitionPath*\\Boot\\\*.\*
    >
    >     where *SystemPartitionPath* is the path to the system partition.
    >
    > -   The system partition path can be found under the following registry key: **HKEY\_LOCAL\_MACHINE**\\**System**\\**Setup**\\**SystemPartition**

     

On restore, all components that are marked as critical volumes must be restored. If one or more critical volumes cannot be restored, the restore operation fails.

In the [**PreRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore?branch=master) phase of the restore sequence, disks that were not excluded during backup are re-created and reformatted by default. However, they are not re-created or reformatted if they meet the following conditions:

-   A basic disk is not re-created if its disk layout is intact or only additive changes have been made to it. The disk layout is intact if the following conditions are true:
    -   The disk signature, disk style (GPT or MBR), logical sector size, and volume start offset are not changed.
    -   The volume size is not decreased.
    -   For GPT disks, the partition identifier is not changed.
-   A dynamic disk is not re-created if its disk layout is intact or only additive changes have been made to it. For a dynamic disk to be intact, all of the conditions for a basic disk must be met. In addition, the entire disk pack's volume structure must be intact. The disk pack's volume structure is intact if it meets the following conditions, which apply to both MBR and GPT disks:
    -   The number of volumes that are available in the physical pack during restore must be greater than or equal to the number of volumes that were specified in the ASR writer metadata during backup.
    -   The number of [*plexes*](base.virtual_disk_service_glossary_all#base-plex) per volume must be unchanged.
    -   The number of [*members*](base.virtual_disk_service_glossary_all#base-member) must be unchanged.
    -   The number of physical disk extents must be greater than the number of disk extents specified in the ASR writer metadata.
    -   An intact pack remains intact when additional volumes are added, or if a volume in the pack is extended (for example, from a simple volume to a spanned volume).
        > [!Note]  
        > If a simple volume is mirrored, the pack is not intact and will be re-created to ensure that the BCD and boot volume state remain consistent after restore. If volumes are deleted, the pack is re-created.

         
-   If the dynamic disk pack's volume structure is intact and only additive changes have been made to it, the disks in the pack are not re-created.

    **Windows Vista:** Dynamic disks are always re-created. Note that this behavior has changed with Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

At any time before the beginning of the restore phase, the requester can specify that the disks should be quick-formatted by setting the **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**ASR**\\**RestoreSession** registry key. Under this key, there is a value named **QuickFormat** with the data type REG\_DWORD. If this value does not exist, you should create it. Set the data of the **QuickFormat** value to 1 for quick formatting or 0 for slow formatting.

If the **QuickFormat** value does not exist, the disks will be slow-formatted.

Quick formatting is significantly faster than slow formatting (also called full formatting). However, quick formatting does not verify each sector on the volume.

## Overview of Restore Phase Tasks

At restore time, the requester performs the following steps:

> [!Note]  
> All steps are required unless otherwise indicated.

 

1.  Call the [**CreateVssBackupComponents**](/windows/win32/VsBackup/nf-vsbackup-createvssbackupcomponents?branch=master) function to create an instance of the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface and call the [**IVssBackupComponents::InitializeForRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforrestore?branch=master) method to initialize the instance for restore by loading the requester's Backup Components Document into the instance.
2.  \[This step is required only if the requester needs to change whether "IncludeDisk" or "ExcludeDisk" is specified for one or more disks.\] Call [**IVssBackupComponents::SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master) to set the restore options for the ASR writer components. The ASR writer supports the following options: "IncludeDisk" allows the requester to include a disk on the target system to be considered for restore, even if it was not selected during the backup phase. "ExcludeDisk" allows the requester to prevent a disk on the target system from being re-created. Note that if "ExcludeDisk" is specified for a disk that contains a critical volume, the subsequent call to [**IVssBackupComponents::PreRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore?branch=master) will fail.

    The following example shows how to use [**SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master) to prevent disk 0 and disk 1 from being re-created and inject third-party drivers into the restored boot volume.

    **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** Injection of third-party drivers is not supported.

    The example assumes that the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) pointer, m\_pBackupComponents, is valid.

    ```C++
        m_pBackupComponents->SetRestoreOptions(
            AsrWriterId,
            VSS_CT_FILEGROUP,
            NULL,
            TEXT("ASR"),
            TEXT("\"ExcludeDisk\"=\"0\", \"ExcludeDisk\"=\"1\" "),
            TEXT("\"InjectDrivers\"=\"1\" ")
            );
    ```

    

    To exclude all disks for a specified volume, see the following "Excluding All Disks for a Volume."

3.  Call [**IVssBackupComponents::PreRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore?branch=master) to notify the ASR writer to prepare for a restore operation. Call [**IVssAsync::QueryStatus**](/windows/win32/Vss/nf-vss-ivssasync-querystatus?branch=master) as many times as necessary until the status value returned in the *pHrResult* parameter is not VSS\_S\_ASYNC\_PENDING.
4.  Restore the data. In the restore phase, ASR reconfigures the volume GUID path (\\\\?\\Volume{GUID}) for each volume to match the volume GUID path that was used during the backup phase. However, drive letters are not preserved, because this would cause collisions with the drive letters that are automatically assigned in the recovery environment. Thus, when restoring data, the requester must use volume GUID paths, not drive letters, to access the volumes.
5.  Set the **HKLM**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**ASR**\\**RestoreSession** registry key to indicate the set of volumes that have been restored or reformatted.

    Under this key, there is a value named **RestoredVolumes** with the data type REG\_MULTI\_SZ. If this value does not exist, you should create it. Under this value, your requester should create a volume GUID entry for each volume that has been restored. This entry should be in the following format: \\\\?\\Volume{78618c8f-aefd-11da-a898-806e6f6e6963}. Each time a bare-metal recovery is performed, ASR sets the **RestoredVolumes** value to the set of volumes that ASR restored. If the requester restored additional volumes, it should set this value to the union of the set of volumes that the requester restored and the set of volumes that ASR restored. If the requester did not use ASR, it should replace the list of volumes.

    You should also create a value named **LastInstance** with the data type REG\_SZ. This key should contain a random cookie that uniquely identifies the current restore operation. Such a cookie can be created by using the [**UuidCreate**](rpc.uuidcreate) and [**UuidToString**](rpc.uuidtostring) functions. Each time a bare-metal recovery is performed, ASR resets this registry value to notify requesters and non-VSS backup applications that the recovery has occurred.

6.  Call [**IVssBackupComponents::PostRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore?branch=master) to indicate the end of the restore operation. Call [**IVssAsync::QueryStatus**](/windows/win32/Vss/nf-vss-ivssasync-querystatus?branch=master) as many times as necessary until the status value returned in the *pHrResult* parameter is not VSS\_S\_ASYNC\_PENDING.

In the restore phase, ASR may create or remove partitions to restore the computer to its previous state. Requesters must not attempt to map disk numbers from the backup phase to the restore phase.

On restore, the requester must exclude the disk that contains the requester's backup set. Otherwise, the backup set can be overwritten by the restore operation.

On restore, a disk is excluded if it was not selected as a component during backup, or if it is explicitly excluded by calling [**IVssBackupComponents::SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master) with the "ExcludeDisk" option during restore.

It is important to note that during WinPE disaster recovery, ASR writer functionality is present, but no other writers are available, and the VSS service is not running. After WinPE disaster recovery has completed, the computer has restarted, and the Windows operating system is running normally, the VSS service can be started, and the requester can perform any additional restore operations that require participation of writers other than the ASR writer.

If during the restore session the backup application detects that the volume unique IDs are unchanged, and therefore all volumes from the time of the backup are present and intact in WinPE, the backup application can proceed to restore only the contents of the volumes, without involving ASR. In this case, the backup application should indicate that the computer was restored by setting the following registry key in the restored operating system: **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**ASR**\\**RestoreSession**

Under this key, specify **LastInstance** for the value name, REG\_SZ for the value type, and a random cookie (such as a GUID created by the [**UuidCreate**](rpc.uuidcreate) function) for the value data.

If during the restore session the backup application detects that one or more volumes are changed or missing, the backup application should use ASR to perform the restore. ASR will re-create the volumes exactly the way they were at the time of the backup and set the **RestoreSession** registry key.

## Excluding All Disks for a Volume

The following example shows how to exclude all disks for a specified volume.


```C++
HRESULT BuildRestoreOptionString
(
    const WCHAR             *pwszVolumeNamePath,
    CMyString               *pstrExclusionList
)
{
    HANDLE                  hVolume           = INVALID_HANDLE_VALUE;
    DWORD                   cbSize            = 0;
    VOLUME_DISK_EXTENTS     * pExtents        = NULL;
    DISK_EXTENT             * pExtent         = NULL;
    ULONG                   i                 = 0;
    BOOL                    fIoRet            = FALSE;
    WCHAR                   wszDest[MAX_PATH] = L"";
    CMyString               strVolumeName;
    CMyString               strRestoreOption;

    // Open a handle to the volume device.
    strVolumeName.Set( pwszVolumeNamePath );
    // If the volume name contains a trailing backslash, remove it.
    strVolumeName.UnTrailing( L'\\' );
    hVolume = ::CreateFile(strVolumeName, 0, FILE_SHARE_READ | FILE_SHARE_WRITE, NULL, OPEN_EXISTING, NULL, 0);
    // Check whether the call to CreateFile succeeded.

    // Get the list of disks used by this volume.
    cbSize = sizeof(VOLUME_DISK_EXTENTS);
    pExtents = (VOLUME_DISK_EXTENTS *)::CoTaskMemAlloc(cbSize);

    ::ZeroMemory(pExtents, cbSize);

    fIoRet = ::DeviceIoControl(hVolume, IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS, NULL, 0, pExtents, cbSize, &amp;cbSize, 0);
    if ( !fIoRet &amp;&amp; GetLastError() == ERROR_MORE_DATA )
    {
        // Allocate more memory.
        cbSize = FIELD_OFFSET(VOLUME_DISK_EXTENTS, Extents) + pExtents->NumberOfDiskExtents * sizeof(DISK_EXTENT);
        ::CoTaskMemFree(pExtents);
        pExtents = NULL;

        pExtents = (VOLUME_DISK_EXTENTS *) ::CoTaskMemAlloc(cbSize);
        // Check whether CoTaskMemAlloc returned an out-of-memory error.
        ::ZeroMemory(pExtents, cbSize);

        // Now the buffer should be big enough.
        ::DeviceIoControl(hVolume, IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS, NULL, 0, pExtents, cbSize, &amp;cbSize, 0);
        // Check whether the IOCTL succeeded.
    }
    // Check for errors; note that the IOCTL can fail for a reason other than insufficient memory.

    // For each disk, mark it to be excluded in the Restore Option string.
    for (i = 0; i < pExtents->NumberOfDiskExtents; i++)
    {
        pExtent = &amp;pExtents->Extents[i];

        *wszDest = L'\0';
        StringCchPrintf(wszDest, MAX_PATH, L"\"ExcludeDisk\"=\"%d\", ", pExtent->DiskNumber); // check errors

        strRestoreOption.Append(wszDest);
        // Check for an out-of-memory error.
    }

    // Remove the trailing comma.
    strRestoreOption.TrimRight();
    strRestoreOption.UnTrailing(',');

    // Set the output parameter.
    strRestoreOption.Transfer( pstrExclusionList );

Exit:
    if( pExtents )
    {
        ::CoTaskMemFree(pExtents);
        pExtents = NULL;
    }

    if( hVolume != INVALID_HANDLE_VALUE )
    {
        ::CloseHandle(hVolume);
        hVolume = INVALID_HANDLE_VALUE;
    }

    return ( hr );
}

```



 

 



