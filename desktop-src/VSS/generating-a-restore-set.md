---
description: A restore set is a list of all files to be restored and the locations to which they will be restored.
ms.assetid: 3196c26c-3407-4c00-a800-c3497df583e5
title: Generating A Restore Set
ms.topic: article
ms.date: 05/31/2018
---

# Generating A Restore Set

A restore set is a list of all files to be restored and the locations to which they will be restored.

As when generating the backup file list (see [Generating A Backup Set](generating-a-backup-set.md)), an algorithm for determining which files to restore and where to restore them must proceed [*writer instance*](vssgloss-w.md) by writer instance, and on a component-by-component basis for each writer instance.

It is necessary to associate each file on the backup media with the component that managed it. It is also necessary to obtain the managing component's [*restore method*](vssgloss-r.md), and the file's [*restore target*](vssgloss-r.md) information, and its [*alternate location mappings*](vssgloss-a.md) (if any).

Some files may also require [*partial files*](vssgloss-p.md) operations or [*directed targets*](vssgloss-d.md) for restore.

By examining the components' [*selectability for backup*](vssgloss-s.md) and [*logical paths*](vssgloss-l.md) (see [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md)), a requester is able to determine the component structure of the backup operation it is going to restore.

With the component structure of the backup established, the requester can get each component's [*file set*](vssgloss-f.md) information (file specification, path, and recursion flag). A requester can then generate a restore set.

Files requiring [*partial files*](vssgloss-p.md), or [*directed targets*](vssgloss-d.md) provide their own detailed restoration instructions (see [Non-Default Backup and Restore Locations](non-default-backup-and-restore-locations.md)), which can then be added to the restore set.

A typical mechanism for generating a restore set for files not involved with partial files operations, or [*directed targets*](vssgloss-d.md) might proceed by doing the following:

1.  Obtain a list of files on the backup media, including their original paths.

2.  Identify the [*writer class*](vssgloss-w.md) and component for each file on the backup media by doing the following:

    -   For each writer, obtain component information ([**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent)) by calling [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent) on all its components.
    -   For each component, obtain file descriptor ([**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc)) information for every set of files the component contains (depending on the types of data the component contains by calling [**IVssWMComponent::GetFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getfile), [**IVssWMComponent::GetDatabaseFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabasefile), and [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile).
    -   Compare the file's name and path information against that returned by the path information contained in the file descriptor for each set of files in a component (returned by [**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath), [**IVssWMFiledesc::GetFilespec**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getfilespec), and [**IVssWMFiledesc::GetRecursive**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getrecursive)) against stored files path information to determine whether the file is part of the component.
        > [!Note]  
        > You should ignore any alternate location information in the file descriptor retrieved from a component found in a stored Writer Metadata Document (that is, [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) does not return **NULL**). This alternate location is the [*alternate path*](vssgloss-a.md), which is used only during backup.

         

3.  Obtain alternate mapping information for each file on the backup media:

    -   Alternate file mappings are stored at the writer, not the component level, and are obtained from the object [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) returned by [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping).
    -   You can determine if a particular file has an alternate location mapping by checking the file's path and name against the path and file specification contained in the alternate location mapping returned by [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping), via [**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath), [**IVssWMFiledesc::GetFilespec**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getfilespec), and [**IVssWMFiledesc::GetRecursive**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getrecursive). (If an alternate path was used during backup, that information should be ignored during this check in processing a restore.)
    -   If a file and an alternate location mappings file descriptors match, you then use the [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) method of the [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) object returned by [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping) to find the alternate location to which you can restore the file.
    -   The alternate location mapping obtained in this way will not necessarily agree with that returned from the Backup Components Document by [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping). The [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) value is nonblank only if the alternate location mapping is used for a file.

4.  With this file and component information, the Backup Components Document can be queried to obtain information about restore targets, options, and new restore locations for each file. This information can be combined with the list of files, components, and alternate locations.

5.  Files not protected by writers can be selected in a manner consistent with traditional restore operations.

At this point, a requester should have a list of all the files it needs to restore, along with instructions about how to restore them, and can begin restoring files on the basis of:

-   Whether alternate location mappings, or the original file location is to be used as the target for the restore will depend on the presence or absence of a file at that target location and component settings of [**VSS\_RESTORE\_TARGET**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restore_target) and [**VSS\_RESTOREMETHOD\_ENUM**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restoremethod_enum) (see [Non-Default Backup and Restore Locations](non-default-backup-and-restore-locations.md)).
-   Whether an attempt at restoration succeeds will depend on issues such as the access permissions of the target, if target files are locked, and other conventional issues involved in file restoration.
-   The success or failure of restoring a given component for a given writer instance should be preserved in the Backup Components Document by calling [**IVssBackupComponents::SetFileRestoreStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setfilerestorestatus). This will make the information accessible to writers when they process the PostRestore event.
-   If a file is restored to an alternate location mapping, the requester must call [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping). This will allow writers to determine whether their files have been restored to alternate locations through the [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping).
-   Requesters may find it desirable to restore files to completely new locations. This is acceptable, but the requester must indicate this to the writer by using the [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget) method.

 

 



