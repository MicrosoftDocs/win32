---
description: There are certain circumstances where the files to be backed up are not the default location for those files.
ms.assetid: b9e96827-a678-45ca-8ede-4508a406f071
title: Working with Alternate Paths during Backup
ms.topic: article
ms.date: 05/31/2018
---

# Working with Alternate Paths during Backup

There are certain circumstances where the files to be backed up are not the default location for those files.

For example, some writers cannot guarantee to have flushed of their data within the time window between [*Freeze*](vssgloss-f.md) and [*Thaw*](vssgloss-t.md) events. Such writers may choose to generate duplicate files containing a last known good configuration in a non-default source directory, or [*alternate path*](vssgloss-a.md).

The term alternate path, as used with VSS, should not be confused with the term [*alternate location mapping*](vssgloss-a.md). Alternate paths are used only during backup operations, and refer to an alternate source from which to back up. Alternate location mappings are used only during restore operations, and refer to an alternate destination for restore operations.

**To use an alternate path during backup**

1.  During the discovery phase of a backup operation (see [Overview of the Backup Discovery Phase](overview-of-the-backup-discovery-phase.md)) a requester would examine each writer's component data using [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent) and get instances of the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface.
2.  A requester then obtains the [*file set*](vssgloss-f.md) managed by each component, represented by instances of the [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) interface, by calling the [**IVssWMComponent::GetFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getfile) method.
3.  In addition to a path ([**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath)), a file specification ([**IVssWMFiledesc::GetFilespec**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getfilespec)), and a recursion flag ([**IVssWMFiledesc::GetRecursive**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getrecursive)), a [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) object may contain an alternate location (used as an alternate path for backup operations and an alternate location mapping for restore operations) by using the [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) method.
4.  If the value returned by [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) is non-NULL, backup applications use that value instead of the value obtained from [**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath) to select and locate files to back up.
5.  Despite using an alternate path, requesters should still respect the file specification and recursive settings returned by [**IVssWMFiledesc::GetFilespec**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getfilespec) and [**IVssWMFiledesc::GetRecursive**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getrecursive).

Note that on restore, any alternate path—that is, an alternate location returned by an instance of [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) gotten from an instance of [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent), which in turn was obtained from an instance of [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata) gotten by retrieving a stored Writer Metadata Document—is not used during restoration.

Either the default path (returned by the [**GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath) method of the same instance of [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc)) is used to define a restore location, or an alternate location mapping—found by using the [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) method—indicates where a file is to be restored (see [Working with Alternate Locations during Restore](working-with-alternate-locations-during-restore.md)).

 

 



