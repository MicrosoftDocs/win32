---
Description: 'There are certain circumstances where the files to be backed up are not the default location for those files.'
ms.assetid: 'b9e96827-a678-45ca-8ede-4508a406f071'
title: Working with Alternate Paths during Backup
---

# Working with Alternate Paths during Backup

There are certain circumstances where the files to be backed up are not the default location for those files.

For example, some writers cannot guarantee to have flushed of their data within the time window between [*Freeze*](vssgloss-f.md#base-vssgloss-freeze) and [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event) events. Such writers may choose to generate duplicate files containing a last known good configuration in a non-default source directory, or [*alternate path*](vssgloss-a.md#base-vssgloss-alternate-path).

The term alternate path, as used with VSS, should not be confused with the term [*alternate location mapping*](vssgloss-a.md#base-vssgloss-alternate-location-mapping). Alternate paths are used only during backup operations, and refer to an alternate source from which to back up. Alternate location mappings are used only during restore operations, and refer to an alternate destination for restore operations.

**To use an alternate path during backup**

1.  During the discovery phase of a backup operation (see [Overview of the Backup Discovery Phase](overview-of-the-backup-discovery-phase.md)) a requester would examine each writer's component data using [**IVssExamineWriterMetadata::GetComponent**](ivssexaminewritermetadata-getcomponent.md) and get instances of the [**IVssWMComponent**](ivsswmcomponent.md) interface.
2.  A requester then obtains the [*file set*](vssgloss-f.md#base-vssgloss-file-set) managed by each component, represented by instances of the [**IVssWMFiledesc**](ivsswmfiledesc.md) interface, by calling the [**IVssWMComponent::GetFile**](ivsswmcomponent-getfile.md) method.
3.  In addition to a path ([**IVssWMFiledesc::GetPath**](ivsswmfiledesc-getpath.md)), a file specification ([**IVssWMFiledesc::GetFilespec**](ivsswmfiledesc-getfilespec.md)), and a recursion flag ([**IVssWMFiledesc::GetRecursive**](ivsswmfiledesc-getrecursive.md)), a [**IVssWMFiledesc**](ivsswmfiledesc.md) object may contain an alternate location (used as an alternate path for backup operations and an alternate location mapping for restore operations) by using the [**IVssWMFiledesc::GetAlternateLocation**](ivsswmfiledesc-getalternatelocation.md) method.
4.  If the value returned by [**IVssWMFiledesc::GetAlternateLocation**](ivsswmfiledesc-getalternatelocation.md) is non-NULL, backup applications use that value instead of the value obtained from [**IVssWMFiledesc::GetPath**](ivsswmfiledesc-getpath.md) to select and locate files to back up.
5.  Despite using an alternate path, requesters should still respect the file specification and recursive settings returned by [**IVssWMFiledesc::GetFilespec**](ivsswmfiledesc-getfilespec.md) and [**IVssWMFiledesc::GetRecursive**](ivsswmfiledesc-getrecursive.md).

Note that on restore, any alternate path—that is, an alternate location returned by an instance of [**IVssWMFiledesc::GetAlternateLocation**](ivsswmfiledesc-getalternatelocation.md) gotten from an instance of [**IVssWMComponent**](ivsswmcomponent.md), which in turn was obtained from an instance of [**IVssExamineWriterMetadata**](ivssexaminewritermetadata.md) gotten by retrieving a stored Writer Metadata Document—is not used during restoration.

Either the default path (returned by the [**GetPath**](ivsswmfiledesc-getpath.md) method of the same instance of [**IVssWMFiledesc**](ivsswmfiledesc.md)) is used to define a restore location, or an alternate location mapping—found by using the [**IVssWMFiledesc::GetAlternateLocation**](ivsswmfiledesc-getalternatelocation.md) method—indicates where a file is to be restored (see [Working with Alternate Locations during Restore](working-with-alternate-locations-during-restore.md)).

 

 



