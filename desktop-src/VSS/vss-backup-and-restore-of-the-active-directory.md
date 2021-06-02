---
description: The Active Directory writer requires no special actions during backup operations.
ms.assetid: 66efd5e5-e6c9-4179-b119-1b5b977b0f9f
title: VSS Backup and Restore of the Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# VSS Backup and Restore of the Active Directory

The Active Directory writer requires no special actions during backup operations. The writer will provide the requester with component and file set information, and the requester uses that information to decide which files to copy to backup media. There is no need to use any special APIs to back up the Active Directory.

How a restore is performed depends on whether the Active Directory is be restored as part of a disaster recovery operation, or if the restore is to a system on which the Active Directory is running. In addition, the age of the backup copy of the Active Directory state may be an issue because of Active Directory tombstones.

## Active Directory Restoration following Disaster Recovery

Following a crash requiring disaster recovery, the Active Directory can be restored as part of the restoration of the operating system state.

This restore operation is essentially a writerless restore.

## Active Directory Restoration on the System where It Is Running

The system must be rebooted in Directory Services Restore mode if the Active Directory is currently running on the server.

The operating system will then be running without the Active Directory, and all user validation occurs through the Security Accounts Manager (SAM) in the registry. Only the administrator has permission to recover the Active Directory.

Once in Directory Service Restore mode, a VSS restore can proceed normally. There is no reason to use non-VSS Win32 Active Directory APIs to restore the Active Directory state.

## Active Directory Restores and Active Directory Tombstones

Any recovery plan should ensure that the age of the backup should not exceed the Active Directory Tombstone Lifetime (default is 60 days).

Restoration of a backup older than the tombstone will cause a domain controller to have objects that are not replicated to the other servers.

Those objects that are not replicated will not be deleted automatically on that (restored) domain controller because the tombstones of those objects on the other replicas have already been deleted.

An administrator will have to manually delete each of the objects on the restored domain controller that are not replicated. Incremental backups of the Active Directory are not supported; a full backup is required.

 

 



