---
description: It may be necessary for a service to be stopped prior to and restarted following a restore operation.
ms.assetid: 111d1281-ad83-49bc-868c-1106a0e25a2a
title: Stopping Services for Restore by Requesters
ms.topic: article
ms.date: 05/31/2018
---

# Stopping Services for Restore by Requesters

It may be necessary for a service to be stopped prior to and restarted following a restore operation.

Typically, stopping and starting a service to support a restore would be performed by a writer when handling the [*PreRestore*](vssgloss-p.md) event (with [**CVssWriter::OnPreRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onprerestore)) and the [*PostRestore*](vssgloss-p.md) event (with [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore)).

However, there may be cases when it is necessary for a requester to explicitly stop a running service. Writers indicate if this is the case by setting the VSS\_RME\_STOP\_RESTORE\_START or VSS\_RME\_RESTORE\_STOP\_START value of the [**VSS\_RESTOREMETHOD\_ENUM**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restoremethod_enum) enumeration as the restore method argument of a call to the [**IVssCreateWriterMetadata::SetRestoreMethod**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setrestoremethod) method and specifying the name of the service to be stopped.

A requester obtains information about the restore method and the name of the service to be stopped when working with writer metadata by using the [**IVssExamineWriterMetadata::GetRestoreMethod**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getrestoremethod) method.

It is important that the writer, when specifying the name of a service to be stopped, uses the correct publicly known name of that service. An ambiguous or inaccurate name may result in requesters stopping the wrong service or being unable to determine which service to stop.

After the completion of the restore operation, requesters must restart the service.

You must be careful in designing and implementing writers that support services that requesters must stop and restart. Specifically, such writers should not actually be part of the service—that is, the writer itself should not need to be stopped and then restarted in the course of the restore operation.

A writer whose process is stopped will have a different writer instance upon restart. The new instance of the writer will not receive VSS events intended for the original instance of the writer. Specifically, if the process of a writer instance is stopped after handling a PreRestore event, the new instance will not receive the PostRestore event. Further, VSS will generate an error indicating the loss of a participating writer in the restore operation, and [**IVssBackupComponents::PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore) may return a failure.

 

 



