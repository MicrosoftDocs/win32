---
description: This topic explains how to determine whether a SYSVOL folder is replicated by DFSR or FSR and explains how to backup and restore an FRS-replicated SYSVOL folder.
ms.assetid: 32d8a5bd-eeb4-4db6-8129-b5cd3508a7e5
title: Backing Up and Restoring an FRS-Replicated SYSVOL Folder
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring an FRS-Replicated SYSVOL Folder

The System Volume (SYSVOL) folder provides a standard location to store important elements of [Group Policy](/previous-versions/windows/it-pro/windows-server-2003/cc779838(v=ws.10)) objects and scripts. A copy of the SYSVOL folder exists on each domain controller in a domain. The SYSVOL folder is replicated by either [Distributed File System Replication (DFSR)](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) or the [File Replication Service (FRS)](/previous-versions/windows/it-pro/windows-server-2003/cc781582(v=ws.10)). This topic explains how to determine whether a SYSVOL folder is replicated by DFSR or FSR and explains how to backup and restore an FRS-replicated SYSVOL folder.

FRS can copy SYSVOL contents to other domain controllers within the domain. FRS monitors the SYSVOL folder and, if a change occurs to any file stored on the SYSVOL folder, then FRS automatically replicates the changed file to the SYSVOL folders on the other domain controllers in the domain.

> [!Note]  
> Only the Group Policy template is replicated by replicating the contents of the SYSVOL folder. The Group Policy container is replicated through Active Directory replication. For Group Policy to operate successfully, both the Group Policy template and the Group Policy container must be available on a domain controller.

 

This topic covers the following subjects:

-   [Determining Whether a Domain Controller's SYSVOL Folder is Replicated by DFSR or FRS](#determining-whether-a-domain-controllers-sysvol-folder-is-replicated-by-dfsr-or-frs)
-   [Backing Up a DFSR-Replicated SYSVOL Folder](#backing-up-a-dfsr-replicated-sysvol-folder)
-   [Backing Up an FRS-Replicated SYSVOL Folder on a Windows Server 2008 or Windows Server 2003 Domain](#backing-up-an-frs-replicated-sysvol-folder-on-a-windows-server-2008-or-windows-server-2003-domain)
-   [Sample FRS Writer Metadata Document](#sample-frs-writer-metadata-document)
-   [Setting Registry Keys for a Restore of an FRS-Replicated SYSVOL Folder](#setting-registry-keys-for-a-restore-of-an-frs-replicated-sysvol-folder)
-   [Performing a Nonauthoritative Restore of an FRS-Replicated SYSVOL Folder](#performing-a-nonauthoritative-restore-of-an-frs-replicated-sysvol-folder)
-   [Performing an Authoritative Restore of an FRS-Replicated SYSVOL Folder](#performing-an-authoritative-restore-of-an-frs-replicated-sysvol-folder)

## Determining Whether a Domain Controller's SYSVOL Folder is Replicated by DFSR or FRS

The following table summarizes how to determine whether a domain controller's SYSVOL folder is being replicated by [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) or FRS.

| If the domain controller is running                                                                                                                  | SYSVOL is replicated by |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Windows Server 2008 + domain functional level of Windows Server 2008 + [SYSVOL migration](https://techcommunity.microsoft.com/t5/storage-at-microsoft/sysvol-migration-series-part-1-8211-introduction-to-the-sysvol/ba-p/423456) completed | DFSR                    |
| Windows Server 2008 + domain functional level below Windows Server 2008                                                                              | FRS                     |
| Windows Server 2003                                                                                                                                  | FRS                     |



 

If the domain's [functional level](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754918(v=ws.10)) is Windows Server 2008 and the domain has undergone [SYSVOL migration](https://techcommunity.microsoft.com/t5/storage-at-microsoft/sysvol-migration-series-part-1-8211-introduction-to-the-sysvol/ba-p/423456), [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) will be used to replicate the SYSVOL folder. If the first domain controller in the domain was promoted directly into the Windows Server 2008 [functional level](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754918(v=ws.10)), DFSR is automatically used for SYSVOL replication. In such cases, there is no need for migration of SYSVOL replication from FRS to DFSR. If the domain was upgraded to Windows Server 2008 [functional level](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754918(v=ws.10)), FRS is used for SYSVOL replication until the [migration](https://techcommunity.microsoft.com/t5/storage-at-microsoft/sysvol-migration-series-part-1-8211-introduction-to-the-sysvol/ba-p/423456) process from FRS to DFSR is complete.

To determine whether DFSR or FRS is being used on a domain controller that is running Windows Server 2008, check the value of the **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**DFSR**\\**Parameters**\\**SysVols**\\**Migrating Sysvols**\\**LocalState** registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

## Backing Up a DFSR-Replicated SYSVOL Folder

If the SYSVOL folder is replicated by [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr), the DFSR VSS writer can be used to back it up. For more information about the DFSR VSS writer, see [DFSR Replicated Folders](/previous-versions/windows/desktop/dfsr/dfsr-replicated-folders).

## Backing Up an FRS-Replicated SYSVOL Folder on a Windows Server 2008 or Windows Server 2003 Domain

On a domain controller that is running Windows Server 2008 or Windows Server 2003, the VSS infrastructure is present, and therefore the FRS VSS writer can be used to back up the SYSVOL folder and FRS components.

The FRS VSS writer's Writer Metadata Document provides information about the location of the SYSVOL folder and the exclusion lists for the writer. Based on this information, a VSS backup application (requester) can back up the SYSVOL folder using the regular VSS-based backup techniques.

The Writer Metadata Document contains information about the writer, the data that the writer owns, and how to restore that data. This is a read-only document that can be retrieved by the backup application before taking a backup. The [DiskShadow](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc772172(v=ws.11)) tool can be used to view the FRS VSS writer's Writer Metadata Document. The [DiskShadow list writers](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc772172(v=ws.11)) command provides information about the writers present on the system. This list contains information about the FRS writer on domain controllers that use FRS for SYSVOL replication or on file servers that use FRS for replication of [DFS link targets](/previous-versions/windows/it-pro/windows-server-2003/cc782417(v=ws.10)).

The following Sample FRS Writer Metadata Document section shows a sample FRS Writer Metadata Document for a domain controller that has the SYSVOL folder on D:\\Windows\\Sysvol. The path shown in the "Excluded files" section will be the same as that obtained when querying the Netlogon service's **SysVol** registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NetLogon**\\**Parameters**\\**SysVol**

The only exception to this rule occurs when the domain controller is in the REDIRECTED state of [SYSVOL migration](https://techcommunity.microsoft.com/t5/storage-at-microsoft/sysvol-migration-series-part-1-8211-introduction-to-the-sysvol/ba-p/423456). In this state, the writers corresponding to both FRS and the [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) service report their respective copies of the SYSVOL folder. However, the [DFSR](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr) service's copy of the SYSVOL folder (usually a folder called SYSVOL\_DFSR) is the one that is shared by the domain controller; this path is the one referenced by the **SysVol** registry key.

The FRS VSS writer requires a custom restore method. This means that certain custom steps must be performed when restoring files that are being replicated by FRS. For more information, see Performing a Nonauthoritative Restore of an FRS-Replicated SYSVOL Folder.

> [!Note]  
> System state backups for Windows domain controllers do not include the FRS database that maintains state information for the FRS service pertaining to the files within the SYSVOL folder and other content sets. The FRS database, debug logs, staging area files, and files in the [pre-existing data folder](/previous-versions/windows/it-pro/windows-server-2003/cc758169(v=ws.10)) are excluded from a system state backup. The following sample FRS writer specification contains the exclusion list in the "Excluded files" section.

 

## Sample FRS Writer Metadata Document

The following is a sample FRS Writer Metadata Document for a domain controller whose SYSVOL folder path is D:\\Windows\\Sysvol.

``` syntax
* WRITER "FRS Writer"
    - Writer ID   = {d76f5a28-3092-4589-ba48-2958fb88ce29}
    - Writer Instance ID = {07ae58e5-6977-4e34-9dfe-399bbd2cbe40}
    - Supports restore events = FALSE
    - Writer restore conditions = VSS_WRE_NEVER
    - Restore method = VSS_RME_CUSTOM
    - Requires reboot after restore = FALSE

    - Excluded files:
       - Exclude: Path = d:\windows\ntfrs\jet, Filespec = *
       - Exclude: Path = d:\Windows\debug\NtFrs, Filespec = NtFrs*
       - Exclude: Path = d:\windows\sysvol\domain\DO_NOT_REMOVE_NtFrs_PreInstall_Directory, Filespec = *
       - Exclude: Path = d:\windows\sysvol\domain\NtFrs_PreExisting___See_EventLog, Filespec = *
       - Exclude: Path = d:\windows\sysvol\staging\domain, Filespec = NTFRS_*

    - Component "FRS Writer:\SYSVOL\da45368c-b2d3-4cf0-bdc338a2cde15a7b"
       - Name: 'da45368c-b2d3-4cf0-bdc338a2cde15a7b'
       - Logical Path: 'SYSVOL'
       - Full Path: '\SYSVOL\da45368c-b2d3-4cf0-bdc338a2cde15a7b'
       - Caption: ''
       - Type: VSS_CT_FILEGROUP [2]
       - Is Selectable: 'TRUE'
       - Is top level: 'TRUE'
       - Notify on backup complete: 'TRUE'
       - Components:
       - File List: Path = d:\windows\sysvol, Filespec = *
       - Affected paths by this component:
         - d:\windows\sysvol
       - Affected volumes by this component:
         - \\?\Volume{da897ba5-5840-11db-93c1-806e6f6e6963}\ [D:\]
       - Component Dependencies:
```

## Setting Registry Keys for a Restore of an FRS-Replicated SYSVOL Folder

The **BurFlags** registry key is used to perform authoritative or nonauthoritative restores on FRS members of DFS or SYSVOL replica sets. The global (computer-wide) **BurFlags** registry key contains REG\_DWORD values and is located in the following location in the registry:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NtFrs**\\**Parameters**\\**Backup/Restore**\\**Process at Startup**

The most common values for the **BurFlags** registry key are:

-   D2, also known as a nonauthoritative mode restore.
-   D4, also known as an authoritative mode restore.

There are global and replica set-specific **BurFlags** registry keys. Setting the global **BurFlags** registry key reinitializes all replica sets that the member holds. This global key should be set when the server holds only one replica set, or when the replica sets that it holds are relatively few in number and small in size. For example, if the server is a domain controller that does not host any content sets that are replicated using FRS other than the SYSVOL folder, the global **BurFlags** registry key can be set.

The global **BurFlags** registry key is found in the following location in the registry:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NtFrs**\\**Parameters**\\**Backup/Restore**\\**Process At Startup**

In contrast to the global **BurFlags** key, the replica set-specific **BurFlags** key permits the re-initialization of discrete, individual replica sets, allowing healthy replication sets to be left intact.

Replica set-specific **BurFlags** registry keys can be located by determining the GUID for that particular replica set.

The following procedure describes how to determine which GUID corresponds to a particular replica set and describes how to configure a restore.

**To determine which GUID corresponds to a particular replica set and to configure a restore**

1.  Stop the FRS service.
2.  To determine the GUID that represents a particular replica set:
    1.  Locate the following key in the registry.

        **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NtFrs**\\**Parameters**\\**Replica Sets**

    2.  Below the **Replica Sets** subkey, there are one or more subkeys that are each identified by a GUID.
    3.  The **Replica Set Root** value for each GUID is a file system path that indicates the replica set that is represented by this GUID.
    4.  Iterate over this list of GUIDs until the desired replica set is located. Note the corresponding GUID.

3.  Locate the following subkey in the registry:

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NtFrs**\\**Parameters**\\**Cumulative Replica Sets**

4.  Below this subkey, locate the same GUID that was noted in step 2. Below the GUID subkey, create an entry for the **BurFlags** key.
5.  Restart the FRS service.

## Performing a Nonauthoritative Restore of an FRS-Replicated SYSVOL Folder

The nonauthoritative restore is the most common way to reinitialize SYSVOL replication on individual domain controllers. Domain controllers that are nonauthoritatively restored must have inbound connections from other working domain controllers, which are participating in Active Directory and FRS replication. In a large deployment environment consisting of many domain controllers, the remaining domain controllers can be recovered using a nonauthoritative mode restore under the following conditions:

-   There must be at least one known good replica member (a domain controller with a healthy SYSVOL folder).
-   The other domain controllers must be reinitialized in direct replication partner order.

The following procedure describes how to perform a nonauthoritative restore.

**To perform a nonauthoritative restore**

1.  Stop the FRS service.
2.  Restore the backed-up data to the SYSVOL folder.
3.  Configure the **BurFlags** registry key by setting the value of the following registry key to the DWORD value D2.

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NtFrs**\\**Parameters**\\**Backup/Restore**\\**Process at Startup**\\**BurFlags**

4.  Restart the FRS service.

When the FRS service is restarted, the following actions occur:

-   The value of the **BurFlags** registry key is reset to zero.
-   Files in the reinitialized FRS folders are moved to a pre-existing folder.
-   Event 13565 is logged in the FRS event log to signal that a nonauthoritative restore has started.
    > [!Note]  
    > FRS event codes are documented in "FRS event log error codes" in the Help and Support Knowledge Base at <https://go.microsoft.com/fwlink/p/?linkid=117779>

     

-   The FRS database is rebuilt.
-   The member performs an initial join of the replica set from an upstream partner or from the computer that is specified in the **Replica Set Parent** registry key if a parent has been specified for SYSVOL replica sets.
-   The reinitialized computer runs a full replication of the affected replica sets when the relevant replication schedule begins.
-   When the process is complete, an event 13516 is logged to signal that FRS is operational. If the event is not logged, there is a problem with the FRS configuration.

> [!Note]  
> The placement of files in the [pre-existing](/previous-versions/windows/it-pro/windows-server-2003/cc758169(v=ws.10)) folder on reinitialized members is a safeguard in FRS that is designed to prevent accidental data loss. Any files destined for the replica that exist only in the local pre-existing folder and were replicated after the initial replication may then be copied to the appropriate folder. When outbound replication has occurred, files in the pre-existing folder can be deleted to free additional drive space.

 

## Performing an Authoritative Restore of an FRS-Replicated SYSVOL Folder

Authoritative restores are used as a last resort in case of critical situations such as divergence of data on the content set caused by directory collisions. For example, an authoritative restore might be needed to restore an FRS replica set where replication has completely stopped and a rebuild from scratch is required.

If you must perform an authoritative restore of the SYSVOL folder, be aware that it is a very complicated process. Comprehensive guidelines detailing the operations that need to be performed for an authoritative restore of the contents of the SYSVOL folder are documented in "How to rebuild the SYSVOL tree and its content in a domain" in the Help and Support Knowledge Base at <https://go.microsoft.com/fwlink/p/?linkid=117780>.

The following requirements must be met before an authoritative FRS restore is performed:

1.  The FRS service must be disabled on all downstream replication partners (direct and transitive) for the reinitialized SYSVOL folder before the authoritative restore has been configured to occur.
2.  Events 13553 and 13516 have been logged in the FRS event log. These events indicate that the membership of the SYSVOL replica set has been established on the domain controller that is configured for the authoritative restore.
    > [!Note]  
    > FRS event codes are documented in "FRS event log error codes" in the Help and Support Knowledge Base at <https://go.microsoft.com/fwlink/p/?linkid=117779>

     

3.  The domain controller that is configured for the authoritative restore is configured to be authoritative for all the SYSVOL data that is to be replicated to the remaining domain controllers.
4.  All other partners in the replica set must be reinitialized with a nonauthoritative restore.

 

 
