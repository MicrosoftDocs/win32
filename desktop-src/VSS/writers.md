---
description: Writers are applications or services that store persistent information in files on disk and that provide the names and locations of these files to requesters by using the shadow copy interface.
ms.assetid: '24fc2d7c-f8d6-49ca-9bb5-0179bef68e78'
title: Writers
ms.topic: article
ms.date: 05/31/2018
---

# Writers

[*Writers*](vssgloss-w.md) are applications or services that store persistent information in files on disk and that provide the names and locations of these files to requesters by using the shadow copy interface.

During backup operations, writers ensure that their data is quiescent and stable—suitable for shadow copy and backup. Writers collaborate with restores by unlocking files when possible and indicating alternate locations when necessary.

If no writers are present during a VSS backup operation, a shadow copy can still be created. In this case, all data on the shadow-copied volume will be in the [*crash-consistent state*](vssgloss-c.md).

## Writer State

Writers maintain their state in an XML-based metadata object, the [*Writer Metadata Document*](vssgloss-w.md).

This writer metadata is the only data structure that contains the [*file set*](vssgloss-f.md)—path, file specification, and recursion flag—of the data to be backed up and restored.

The Writer Metadata Document organizes the writer's file sets into groups or [*components*](vssgloss-c.md). The relationship of one of these components during backup and restore operations to the other components managed by the writer is described in the Writer Metadata Document by the component's [*selectability for backup*](vssgloss-s.md), its [*selectability for restore*](vssgloss-s.md), and its [*logical paths*](vssgloss-l.md). (For more information, see [Setting up Component Organization](definition-of-components-by-writers.md) and [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md).)

Additional information that governs file restoration and other issues is also contained in this document.

The requester needs the writer metadata, in conjunction with its own Backup Components Document, to process a backup or a restore.

Unlike the Backup Components Document, the Writer Metadata Document should be thought of as a read-only structure. Once a writer creates it, the document is not altered.

## Writer Event Handling

A writer's VSS operations are initiated through the receipt of COM events.

When no events are present, a writer does not perform VSS operations (such as a VSS backup or restore). Instead, it performs its normal work, such as responding to database queries, managing user data, or providing other services.

To ensure that error handling for multiple parallel backup and restore sessions is performed correctly, and to ensure that one backup or restore session does not corrupt another, you must do the following:

-   If a writer's event handler (such as [**CVssWriter::OnFreeze**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onfreeze)) calls the [**CVssWriterEx2::GetSessionId**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriterex2-getsessionid), [**CVssWriter::SetWriterFailure**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-setwriterfailure), or [**CVssWriterEx2::SetWriterFailureEx**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriterex2-setwriterfailureex) method, the event handler must call the method in the same thread that called the event handler.
-   Your writer’s implementation of an event handler such as [**OnFreeze**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onfreeze) can offload work to worker threads if desired, as long as each worker thread marshals any needed error reporting back to the original event handler thread.

## Handling Identify Events

With the exception of the Identify event, the type and order of the events a writer receives depends uniquely on the type of VSS operations that are currently ongoing.

The Identify event requires writers to provide the system information about their configuration and the files they manage through their [*Writer Metadata Document*](vssgloss-w.md). An Identify event is generated in support of almost any VSS operation, including system queries as well as shadow copy and backup and restore operations. Therefore, any writer's implementation of the Identify event handler [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) must be able to handle an Identify event at any time—including in the middle of processing another VSS operation, such as a backup or restore. An Identify event should never be thought of as part of the life cycle of a VSS operation, even though its generation may be expected and required prior to the start of that operation.

It is particularly important that state information about a VSS operation not be modified in [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify), because receipt of an out-of-order event would reset that information.

## Backup and Restore Events

Depending on whether it is participating in a backup or restore, a writer will receive between two and seven events, in addition to an initial Identify event.

Handling these events constitutes (from the point of view of a writer) the life cycle of a backup or restore operation.

In a typical backup operation (see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md)), a writer would handle the following events (in addition to an initial Identify event):

-   PrepareForBackup
-   PrepareForSnapshot
-   Freeze
-   Thaw
-   PostSnapshot
-   BackupComplete
-   BackupShutdown

In a typical restore operation (see [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md)), a writer would handle the following events:

-   PreRestore
-   PostRestore

 

 



