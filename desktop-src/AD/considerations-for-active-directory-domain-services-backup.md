---
title: Considerations for Active Directory Domain Services Backup
description: Directory service data can be replicated. A recovery plan must be created prior to restoration.
ms.assetid: b03215db-1b8d-45b0-85e8-c325b225c6eb
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services Active Directory , recovery planning
- Active Directory Domain Services Active Directory , backup
ms.topic: article
ms.date: 05/31/2018
---

# Considerations for Active Directory Domain Services Backup

Directory service data can be replicated. A recovery plan must be created prior to restoration. One option is to restore a replica of a directory and then propagate changes that occurred since the backup from other replicas in the domain.

In some cases you may want the restored replica to take precedence over the other replicas in the domain. For example, if an object is accidentally deleted and the deletion is replicated to all domain controllers, you could restore the object by restoring one replica from a backup that was made before the object was deleted. Then you would use the NTDSUtil utility to mark the restored object as authoritatively restored. The restored object will then be replicated to the other DCs, and the replica that was restored will receive the updates for all other objects that occurred since the time the backup was made. The end result for all the replicas is the same as that prior to the restore, except that the authoritatively restored object is no longer deleted.

All changes occurring during backup are stored in a temporary log and added to the end of the backup set when the backup is complete.

Any recovery plan should ensure that the age of the backup should not exceed the Active Directory Tombstone Lifetime. For more information on Tombstone Lifetime, see the TechNet topic - [Introduction to Administering Active Directory Backup and Recovery](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816677(v=ws.10)). Restoration of a backup older than the tombstone lifetime may cause the restored domain controller to have objects that will not be replicated on other DCs. This occurs if an object is deleted after the backup is made and the restore occurs after the tombstone for the deleted object has been permanently removed. The restored DC would have the object as it existed before the deletion, and the other DCs would have no record that the object ever existed. In this case, an administrator will have to manually delete each non-replicated object on the restored domain controller.

Incremental backups of Active Directory Domain Services are not supported; full backups are required.

 

 