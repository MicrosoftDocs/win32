---
title: DFSR Replicated Folders
description: A replicated folder defines a set of files and folders to be kept in sync across multiple servers in a replication group. DFSR uses fence values to ensure that the correct version of a resource is replicated where there is a conflict.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '67452355-315a-44eb-b78b-88322f66d1de'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Distributed File System Replication Files , replicated folders", "replicated folders Files"]
---

# DFSR Replicated Folders

A [*replicated folder*](dfsr-glossary.md#fs-dfsr-glossary-replicated-folder) defines a set of files and folders to be kept in sync across multiple servers in a replication group. Replicated folders are defined using the computer name, the local path of the data on each server in a replication group, and the replication configuration for each server, such as the staging folder path and the maximum size of the staging space assigned to the replicated folder.

The state of a replicated folder can be one of the following: uninitialized, initialized, initial sync, auto recovery, normal, or in error. When first configured, a replicated folder moves to the initialized or initial sync state, depending on whether the server is defined as the primary member of the replicated folder. If the server is defined as a primary member, Distributed File System Replication (DFSR) automatically initializes the folder. In addition, content within the folder is authoritative. That is, the content will win on conflict with another member.

If the server is defined as a non-primary member, DFSR on that member must first complete initial sync where its metadata (and data if necessary) is synchronized from a partner that is primary or has already completed initial sync.

DFSR uses [*fence*](dfsr-glossary.md#fs-dfsr-glossary-fence) values to ensure that the correct version of a resource (file or folder) is replicated where there is a conflict. The fence values are also used in initial sync where the versions on the primary member override versions on the non-primary member. Note that copying the same file without the knowledge of DFSR (such as using xcopy) to its members prior to starting DFSR on the non-primary member (as is done for seeding) will result in the version on the upstream partner overwriting the version on the non-primary member. If the file hashes are identical, the file is not downloaded; otherwise, RDC is used to download the changed portions of the file. If the file was updated on the non-primary member while it is in initial sync state then the file is in conflict with its partner (update conflict) and the file will be moved to the Conflict and Deleted folder where RDC is still used.

## Replicated Folder Initialization

DFSR on the primary member for a replicated folder performs the following actions when initializing the replicated folder:

-   Set the replicated folder state to initialized.
-   Mark each resource of the replicated folder with the initial-primary fence.
-   Log an event indicating that the replicated folder has been initialized and is in the normal state.

DFSR on a non-primary member for a replicated folder performs the following actions when initializing the replicated folder:

-   Set the replicated folder state to initialized.
-   Mark each resource of the replicated folder with the fence value of initial-sync.
-   Log an event indicating that the replicated folder has been initialized and is in the initial-sync state.

At this point, the replicated folder will be in the normal state on exactly one member in the replication group; it will be in initial-sync state on all other members. The replicated folder is ready for the initial replication sequence.

## Replication Sequence

Replication flow for a replicated folder begins at the designated primary member, flows to its downstream partners, then to their downstream partners, and so on.

DFSR attempts to establish connections between each member node and its upstream partners and initiate replication for each replicated folder in each replication group. DFSR does so regardless of whether the replicated folder is in the initial-primary or initial-sync state on the member.

If an upstream member receives a replication request for a replicated folder in the initial-sync state, the replication request fails. Therefore, no outbound replication occurs from a member on which the replicated folder is in the initial-sync state. It is required that a replicated folder have a primary member before replication can occur.

If an upstream member receives a replication request for a replicated folder in the normal state, the request succeeds. When the replication is completed, the state of the replicated folder is changed to normal on the downstream members.

## Fence Values

The fence values for resources are used to guarantee predictable outcomes from conflict resolution.

-   A version of a resource with a normal fence value takes precedence over versions with initial-primary and initial-sync fence values.
-   A version of a resource with an initial-primary fence value takes precedence over versions with an initial-sync fence value.
-   If two versions have the same fence value, the conflict is resolved using first create time, then last modified time.
-   A newly created file has a default fence value.
-   A file can also be unfenced, which guarantees that it will lose on conflict.
-   Time stamps can also be used as fence values; in this case, the version with the highest time stamp takes precedence over other time stamps or fence values.

## Automatic Recovery

DFSR has the ability to automatically recover from database loss by rebuilding the database. After a database is rebuilt, all fence values are set to default, and all replicated folders on the volume undergo initial sync.

The first replication after the database recovery on the recovered member proceeds in the following manner:

-   If the replicated folder is in the initial-sync state on the upstream member, DFSR will reject the replication request and the replicated folder will remain in the initialized state.
-   Because all fence values are set to default, conflicts are resolved using first create time, then last modified time.

If two recovered members replicate with other members first, there can be multiple certified versions of a resource in the replication group. Eventually, the conflicts will be detected and resolved correctly. However, having multiple recovered members would increase replication traffic and conflicts reported to the user.

## User-Initiated Restore of Replicated Data

Often it is necessary to rebuild a replication group member server from backup data. DFSR contains a Volume Shadow Copy Service (VSS) writer that supports component-mode restore where the component is the entire replicated folder. If the replicated folder is restored, DFSR is appropriately notified of the restore, so that after initialization it performs a recovery sync operation (similar to the initial sync) where it syncs from its upstream partner rebuilding its metadata. The data remains in place if identical to the upstream partner's data or is updated if a newer version exists on the upstream partner. Any data that exists on the downstream partner that does not exist on the upstream partner will be moved to the Preexisting folder at the end of the recovery sync. Such a recovery is termed "nonauthoritative" recovery and is the default restore option when restoring the replicated folder.

When a backup application performs a system state restore, it must indicate that it has done so by setting the **LastRestoreId** registry key. "System state restore" in this case refers to any restore that selectively restores operating system binaries and drivers. In addition, a backup application that performs system state restore of SYSVOL should set the **SYSVOL** registry key to specify whether the restore operation is authoritative or nonauthoritative.

For more information about the **LastRestoreId** and **SYSVOL** registry keys, see [Registry Keys for Backup and Restore](https://msdn.microsoft.com/library/windows/desktop/bb891959).

Sometimes it may be necessary to rebuild the replication folder on all participating members in the replication group. In this case, one of the members must be selected as a primary member (using DfsrAdmin.exe) and the restore must be performed on that member first, followed by the restore on all other members.

There is also the scenario where the user restores one or more files from a backup on a server. It is also possible for the user to completely restore an entire replicated folder as a set of files without invoking the DFSR writer. In these cases, DFSR has no knowledge that a restore has been performed. If the replicated folder has already been configured on the member, the files appear as new content and DFSR creates new versions for the files. These versions will get the default fence values, causing the files to be in conflict with identical files on other members. Therefore, depending on where the conflict is resolved, the files will be moved to the Conflict and Deleted folder or moved back into the replication folder if identical. Because RDC is used, the amount of data sent over the wire will still be minimal.

## Details on the DFSR VSS Writer

Writer Name: L"DFS Replication service writer"

Writer ID: 2707761b-2324-473d-88eb-eb007a359533

 

 




