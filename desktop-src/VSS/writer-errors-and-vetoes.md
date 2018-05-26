---
Description: A writer can fail for numerous programmatic reasons.
ms.assetid: 50eced73-3917-4d7e-96cc-2d793b448738
title: Writer Errors and Vetoes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Writer Errors and Vetoes

A writer can fail for numerous programmatic reasons. When this happens, it should veto the ongoing backup, restore, or shadow copy operation by calling the [**CVssWriter::SetWriterFailure**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-setwriterfailure?branch=master) method in one of its handler methods (for example, [**CVssWriter::OnFreeze**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onfreeze?branch=master) or [**CVssWriter::OnPreRestore**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onprerestore?branch=master)) and returning **TRUE**. It can also optionally set an error message string in response to a failure condition in certain handler methods with the [**IVssComponentEx::SetPrepareForBackupFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-setprepareforbackupfailuremsg?branch=master), [**IVssComponentEx::SetPostSnapshotFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-setpostsnapshotfailuremsg?branch=master), [**IVssComponent::SetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg?branch=master), and [**IVssComponent::SetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg?branch=master) methods. The requester can accept the veto or continue with the backup, ignoring the veto.

A requester should check the writer status (using [**IVssBackupComponents::GatherWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus?branch=master) and [**IVssBackupComponents::GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus?branch=master)) following each event it generates.

In some cases, error messages can be retrieved from these failures (using the [**IVssComponentEx::GetPrepareForBackupFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-getprepareforbackupfailuremsg?branch=master), [**IVssComponent::GetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getprerestorefailuremsg?branch=master), [**IVssComponentEx::GetPostSnapshotFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-getpostsnapshotfailuremsg?branch=master), and [**IVssComponent::GetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpostrestorefailuremsg?branch=master) methods), or a writer may choose to set metadata (using [**IVssComponent::SetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata?branch=master) and [**IVssComponent::SetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata?branch=master) with error state information). For example code that shows how to view such error messages, see [**IVssComponentEx::GetPrepareForBackupFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponentex-getprepareforbackupfailuremsg?branch=master).

Depending on the error state, a requester or its operator could restart the backup and shadow copy with any necessary modification to the state of the backup job or system.

For example, suppose [**GetWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus?branch=master) returned the following:

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

 

 



