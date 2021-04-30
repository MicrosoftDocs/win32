---
description: Components are defined by and instantiated by writers in their Writer Metadata Document in response to an Identify event at the start of a backup operation (see Overview of Backup Initialization) when the Writer Metadata Document is populated.
ms.assetid: 5e1c3f9b-ca83-4e70-963b-0a237c6f4b0d
title: Definition of Components by Writers
ms.topic: article
ms.date: 05/31/2018
---

# Definition of Components by Writers

Components are defined by and instantiated by writers in their Writer Metadata Document in response to an [*Identify event*](vssgloss-i.md) at the start of a backup operation (see [Overview of Backup Initialization](overview-of-backup-initialization.md)) when the Writer Metadata Document is populated.

When creating a component in its Writer Metadata Document, using [**IVssCreateWriterMetadata**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscreatewritermetadata) and [**IVssCreateWriterMetadata::AddComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addcomponent), a writer must specify:

-   Whether the component is [*selectable for backup*](vssgloss-s.md)
-   A component type
-   A component name (which must be unique not only within a given [*writer instance*](vssgloss-w.md) but across all writer instances)
-   Whether the component has any writer-specific metadata associated with it
-   Whether the writer requires notification following a successful backup

Writers can optionally specify:

-   A component's [*logical path*](vssgloss-l.md) (which must be unique not only within a given writer instance but across all writer instances)
-   A component description (or caption)
-   An icon to be used with GUIs to indicate the component

It is not necessary for a component to actually contain any files. This sort of empty or "dummy" component can be useful in organizing components. Such a component can be used to define a [*component set*](vssgloss-c.md) and a writer's component (see [Logical Pathing of Components](logical-pathing-of-components.md)).

## Setting Up Component Organization

Setting a component's [*selectability*](vssgloss-s.md) (its [*selectability for backup*](vssgloss-s.md), and its [*selectability for restore*](/windows)) and its [*logical paths*](vssgloss-l.md) allows a writer to mandate or make optional the inclusion of certain components in a backup or restore operation, and to group components into [*component sets*](vssgloss-c.md) with one selectable component acting as an entry point to the whole group.

Membership in these groupings determines which components will be used during backup and restore operations. Using "selectable" to mean selectable for back for backup operation, and selectable for restore for restore operation, developers should understand that:

-   If any components managed by a given writer are backed up, then a requester must [*explicitly include*](vssgloss-e.md) all nonselectable [*components*](vssgloss-c.md) without selectable ancestors in their [*logical path*](vssgloss-l.md) to the Backup Components Document and back up and restore those components as a group.
-   A requester has the option of explicitly adding selectable components to the Backup Components Document during backup and restore operations; once added, the component must be backed up or restored.
-   If a component is selectable, the component and all of its [*subcomponents*](vssgloss-s.md) (as defined by logical paths) form a component set, which can be treated as a single unit that may optionally participate in backup and restore operations.
-   A requester never explicitly adds a nonselectable component with selectable ancestors, a subcomponent in a component set, to its Backup Components Document during backup and restore operations. These components must be [*implicitly included*](/windows) if their selectable ancestor is explicitly added, in which case they must be backed up or restored (see [Use of Components by the Requester](use-of-components-by-the-requestor.md)).
-   A selectable component with a selectable ancestor is still a [*subcomponent*](vssgloss-s.md) (a member of a component set) and may be implicitly included if its selectable ancestor is explicitly included in the operation. In this case, its information is not added to the Backup Components Document. If its selectable ancestor is not included in the operation, the component can be explicitly selected for inclusion in the operation, in which case its information is included in the Backup Components Document.
-   A subcomponent implicitly included in a backup can be explicitly included in a restore operation, regardless of the status of any selectable ancestor, if it is selectable for restore. Any selectable for restore subcomponent included during a restore operation must have its information added to the Backup Components Document.
-   A writer that has had no component explicitly added to the Backup Components Document prior to the generation of [*PrepareForBackup*](vssgloss-p.md) and [*PreRestore*](vssgloss-p.md) events will not receive any further VSS events.

For more information, see [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md).

## Adding Files to a Component

A component contains file information in the form of a [*file set*](vssgloss-f.md) that contains:

-   A root directory of the files in the component.
-   A file specification for the files in the component.
-   A flag that indicates whether the component's specification is recursive.

Depending on component type, which can be a database or a file group, and (in the case of database components) whether the files to be loaded are data or log files, a writer calls [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) to add a file set.

When using these functions, you should specify the files to be added to the file set as follows:

-   *wszPath*: This is the path to the directory that contains the files to be added to the file set. If the *bRecursive* parameter is set to **true**, the *wszPath* parameter specifies a hierarchy of directories to be traversed recursively, and all directories should be recreated, including empty directories.
-   *wszFilespec*: This string specifies the files in each directory to be added to the file set.

For example, suppose the following directory structure exists:

<dl> C:\\Directory1\\File1.txt  
C:\\Directory1\\File2.txt  
C:\\Directory1\\Directory2\\File1.txt  
C:\\Directory1\\Directory2\\File2.txt  
C:\\Directory1\\Directory3\\  
</dl>

If the writer specifies "C:\\Directory1" for *wszPath*, "File1.\*" for *wszFilespec*, and **true** for *bRecursive*, the requester should include these files:

<dl> C:\\Directory1\\File1.txt  
C:\\Directory1\\Directory2\\File1.txt  
</dl>

If the writer instead specifies "C:\\Directory1" for *wszPath*, "\*" for *wszFilespec*, and **true** for *bRecursive*, the requester should include these files:

<dl> C:\\Directory1\\File1.txt  
C:\\Directory1\\File2.txt  
C:\\Directory1\\Directory2\\File1.txt  
C:\\Directory1\\Directory2\\File2.txt  
</dl>

If the writer specifies "C:\\Directory1" for *wszPath*, "\*" for *wszFilespec*, and **false** for *bRecursive*, the requester should include these files:

<dl> C:\\Directory1\\File1.txt  
C:\\Directory1\\File2.txt  
</dl>

In all of the preceding examples, whenever the writer specifies **true** for *bRecursive*, the empty directory C:\\Directory1\\Directory3\\ should be recreated.

For a file set added to a file group component, in cases where files currently on disk are not in what the writer would consider the appropriate or default location, a writer has the option of adding an alternate path. In these cases, the file set's definition of the path contains the normal location of the files and to where files should be restored, while the alternate path contains the current location of files to be backed up.

All files in the file set must exist at the time of the backup. Requesters must assume that all files listed in the file set are required for the backup and will fail the backup if any files are missing. Note that when "\*" is specified for the *wszFilespec* parameter, it can match zero or more files.

Note that such Writer Metadata Document attributes as alternate location mappings, explicitly included and excluded files, and restore methods are set at the writer level, not the component level. (For more information, see [Working with the Writer Metadata Document](working-with-the-writer-metadata-document.md).)

## Component Definition for Backup and Restore Operations

Both restore and backup operations necessarily generate an [*Identify event*](vssgloss-i.md), and for both backups and restores it will be handled by the same [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) method.

During backup operations, requesters use the information returned by a writer's [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) methods to determine which writers are present on the system and then to determine which of their files to back up.

During restore operations, the information returned by a writer's [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) event is used only to establish the identity and status of writers currently present on the system; the file specification information generated during a restore is not used. Instead, Writer Metadata Documents stored at backup time are used to obtain this data.

Once generated during a backup operation, the writer component information, along with the rest of the writer information, is saved to be retrieved to support restore operations. It is typically the responsibility of the requester to store this information.

 

 
