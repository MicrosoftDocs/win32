---
description: A writer can fail for numerous programmatic reasons.
ms.assetid: 50eced73-3917-4d7e-96cc-2d793b448738
title: Writer Errors and Vetoes
ms.topic: article
ms.date: 05/31/2018
---

# Writer Errors and Vetoes

A writer can fail for numerous programmatic reasons. When this happens, it should veto the ongoing backup, restore, or shadow copy operation by calling the [**CVssWriter::SetWriterFailure**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-setwriterfailure) method in one of its handler methods (for example, [**CVssWriter::OnFreeze**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onfreeze) or [**CVssWriter::OnPreRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onprerestore)) and returning **TRUE**. It can also optionally set an error message string in response to a failure condition in certain handler methods with the [**IVssComponentEx::SetPrepareForBackupFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponentex-setprepareforbackupfailuremsg), [**IVssComponentEx::SetPostSnapshotFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponentex-setpostsnapshotfailuremsg), [**IVssComponent::SetPreRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg), and [**IVssComponent::SetPostRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg) methods. The requester can accept the veto or continue with the backup, ignoring the veto.

A requester should check the writer status (using [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) and [**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus)) following each event it generates.

In some cases, error messages can be retrieved from these failures (using the [**IVssComponentEx::GetPrepareForBackupFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponentex-getprepareforbackupfailuremsg), [**IVssComponent::GetPreRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getprerestorefailuremsg), [**IVssComponentEx::GetPostSnapshotFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponentex-getpostsnapshotfailuremsg), and [**IVssComponent::GetPostRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpostrestorefailuremsg) methods), or a writer may choose to set metadata (using [**IVssComponent::SetRestoreMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata) and [**IVssComponent::SetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata) with error state information). For example code that shows how to view such error messages, see [**IVssComponentEx::GetPrepareForBackupFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponentex-getprepareforbackupfailuremsg).

Depending on the error state, a requester or its operator could restart the backup and shadow copy with any necessary modification to the state of the backup job or system.

For example, suppose [**GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus) returned the following:

-   **VSS\_E\_WRITERERROR\_INCONSISTENTSNAPSHOT** suggests that a requester might add additional volumes to the shadow copy
-   **VSS\_E\_WRITERERROR\_RETRYABLE** indicates that retrying without reconfiguration might work. If the writer continues to return the error after several retries, try restarting the service that hosts the writer. The following writers are hosted in the VSS service: registry writer, COM+ class registration database writer, shadow copy optimization writer, and Automated System Recovery (ASR) writer. If the writer belongs to an application that hosts the writer in its own process, try restarting the application.

    **Windows Server 2003 and Windows XP:** The following writers are hosted in the VSS service: registry writer, COM+ class registration database writer, application event log writer, and Microsoft SQL Server 2000 Desktop Engine (MSDE) writer.

-   VSS\_E\_WRITER\_STATUS\_NOT\_AVAILABLE indicates that a writer may have reached the maximum number of available backup and restore sessions, and retrying might work when the system is less busy.
-   **VSS\_E\_WRITERERROR\_OUTOFRESOURCES** or **VSS\_E\_WRITERERROR\_TIMEOUT** might suggest that system load be reduced prior to retrying
-   **VSS\_E\_WRITERERROR\_NONRETRYABLE** or **VSS\_E\_WRITER\_NOT\_RESPONDING** would likely indicate a writer error so severe as to preclude trying to back up its data with VSS.

Depending on which writer and which components generate them, it is not always necessary for a backup application to abort following a veto or error.

For example, a requester may decide that the intent of the shadow copy is to back up application A and the veto has been received from the writer for backup application B. In this case, it is perfectly acceptable to continue to back up application A while ignoring the veto.

The following are examples of a writer veto:

-   The writer vetoes the shadow copy creation process when it could not suspend its activities during the time the shadow copy was being created. This indicates that there is a high probability that the shadow copy is not valid because a write operation has occurred during the Freeze state.
-   A backup application has requested a shadow copy of only volume C: and a writer determines that a shadow copy of C: and D: is to back up its data. In this case, the writer will veto. The backup application may examine the metadata and determine whether the writer will be ignored or the shadow copy creation process will be aborted and later restarted.

 

 



