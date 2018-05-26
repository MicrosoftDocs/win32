---
Description: Requesters control a shadow copys features by setting its context. This context indicates whether the shadow copy will survive the current operation, and the degree of writer/provider coordination.
ms.assetid: adf79bc8-e893-444a-b750-d7ffd09de7c9
title: Shadow Copy Context Configurations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shadow Copy Context Configurations

Requesters control a shadow copy's features by setting its context. This context indicates whether the shadow copy will survive the current operation, and the degree of writer/provider coordination.

## Persistence and Shadow Copy Context

A shadow copy may be [*persistent*](vssgloss-p.md#base-vssgloss-persistent-shadow-copy)—that is, the shadow copy is not deleted following the termination of a backup operation or the release of an [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) object.

Persistent shadow copies require [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/win32/Vss/ne-vss-_vss_snapshot_context?branch=master) contexts of **VSS\_CTX\_CLIENT\_ACCESSIBLE**, **VSS\_CTX\_APP\_ROLLBACK**, or **VSS\_CTX\_NAS\_ROLLBACK**. Persistent shadow copies can be made only for NTFS volumes.

Nonpersistent shadow copies are created with contexts of **VSS\_CTX\_BACKUP** or **VSS\_CTX\_FILE\_SHARE\_BACKUP**. Nonpersistent shadow copies can be made for NTFS and non-NTFS volumes.

## Writer Participation and Shadow Copies

A shadow copy context can be classified as either involving writers or not involving writers.

Shadow copy contexts that involve writers in their creation include:

-   **VSS\_CTX\_APP\_ROLLBACK**
-   **VSS\_CTX\_BACKUP**
-   **VSS\_CTX\_CLIENT\_ACCESSIBLE\_WRITERS**

Those that do not involve writers in their creation include:

-   **VSS\_CTX\_CLIENT\_ACCESSIBLE**
-   **VSS\_CTX\_FILE\_SHARE\_BACKUP**
-   **VSS\_CTX\_NAS\_ROLLBACK**

One context can be used with both types of shadow copies, but cannot be used in creating a shadow copy:

-   **VSS\_CTX\_ALL**

Creating a shadow copy with a context of **VSS\_CTX\_ALL** (using [**IVssBackupComponents::StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master) and [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master)) is not supported.

Operations that support a context of **VSS\_CTX\_ALL** are the administrative operations [**IVssBackupComponents::Query**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-query?branch=master), [**IVssBackupComponents::DeleteSnapshots**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-deletesnapshots?branch=master), [**IVssBackupComponents::BreakSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset?branch=master), and [**IVssBackupComponents::ExposeSnapshot**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-exposesnapshot?branch=master).

## Obtaining Shadow Copy Information

If a requester knows the identifying GUID of a shadow copy (its **VSS\_ID**), it can obtain information about the context of a specific shadow copy (identified by its **VSS\_ID**) by unpacking the [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) structure returned by a call to [**IVssBackupComponents::GetSnapshotProperties**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getsnapshotproperties?branch=master).

To obtain context information about all shadow copies on a system, a requester examines the **m\_lSnapshotAttributes** member of the **Obj.Snap** member of the [**VSS\_OBJECT\_PROP**](/windows/win32/Vss/ns-vss-_vss_object_prop?branch=master) (which is a [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) structure) structure obtained by using [**IVssEnumObject**](/windows/win32/Vss/nn-vss-ivssenumobject?branch=master) to iterate over the list of objects returned by a call to [**IVssBackupComponents::Query**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-query?branch=master).

 

 



