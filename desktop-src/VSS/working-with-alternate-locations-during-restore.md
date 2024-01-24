---
description: There are many reasons why a requester either should not, or may not, be able to restore files from backup media to their original location.
ms.assetid: 2a9cfd99-5a2c-4c0c-98ff-11c745298cda
title: Working with Alternate Locations during Restore
ms.topic: article
ms.date: 05/31/2018
---

# Working with Alternate Locations during Restore

There are many reasons why a requester either should not, or may not, be able to restore files from backup media to their original location. For example, a restore method or target may require such a restoration, or the current restoration location may be occupied and unwritable.

To handle such cases, a writer may have defined an [*alternate location mapping*](vssgloss-a.md), a nonstandard restore destination to be used for special circumstances.

The term alternate location mapping, as used with VSS, should not be confused with the term [*alternate path*](vssgloss-a.md). Alternate location mappings are used only during restore operations, and refer to an alternate destination for restore operations. Alternate paths are used only during backup operations, and refer to an alternate source from which to back up.

To use alternate location mappings during restore, a requester would do the following (typically following the generation of a [**PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) event):

1.  Using an instance of the [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata) interface obtained by retrieving a stored writer, a requester uses the [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping) method to obtain a writer's alternate location mappings as instances of the [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) interface.

    > [!Note]  
    > The requester uses [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping), not [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping). The former returns those alternate location mappings available for use by a requester. The latter is used to indicate those alternate location mappings actually used by a requester.

     

2.  The call to the [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping) returns an instance of the [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) interface. This instance contains file set information—a path specified by [**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath), a file specification returned through [**IVssWMFiledesc::GetFilespec**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getfilespec), and a recursion flag obtained from [**IVssWMFiledesc::GetRecursive**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getrecursive)—matching one of the file sets added (using [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles), or [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup)) to one of the components managed by the writer.

    The value returned by [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) is the alternate location mapping for this file set.

3.  Alternate location mappings do not contain component information, so it will be necessary to compare the file set information (path, file specification, and recursion flag) obtained by calling [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping) to that contained by the writer's components.

    This information can be found by iterating over the writer's components and calling [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent) to get an instance of the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface and use [**IVssWMComponent::GetFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getfile) to obtain a [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) instance containing the component file set information.

    When the file set information returned by the instance of [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) obtained from [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent) and [**IVssWMComponent::GetFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getfile) matches that obtained from the **IVssWMFiledesc** instance derived from [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation), the component managing the files with the specific alternate location mapping has been found.

4.  Having located the component, the requester can determine the conditions under which an alternate location mapping should be used by doing the following:

    -   Examining the component's restore method, which is obtained by calling [**IVssExamineWriterMetadata::GetRestoreMethod**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getrestoremethod).
    -   Checking to see if a restore target overrides the restore method, by calling [**IVssComponent::GetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoretarget).

        If the component found in the Writer Metadata Document had been [*explicitly included*](vssgloss-e.md) in the backup, the instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface will correspond to that component. If the component had been [*implicitly included*](vssgloss-i.md) in the backup, then the instance of **IVssComponent** will correspond to the component defining the component set of which the component in the Writer Metadata Document is a subcomponent.

5.  With this information, the requester can determine on a component-by-component basis if it needs to restore a given file set of a given component to a destination defined by the alternate location mapping.

6.  When using an alternate location mapping, the requester respects the file set's file descriptor and recursive flag and uses the path provided by the alternate location mapping.

    The requester indicates that it has used an alternate location mapping during a restore operation by calling the [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping) with the file set's default location information, the alternate restore destination used, and a component name.

    If the file set was managed by a component that was explicitly included in the backup, that component name will be used. If the file set was managed by a component that was implicitly included in the backup, then the name used will be that of the component defining the component set of which the component managing the file set is a subcomponent.

Writers verify whether file sets from one of their components were restored to an alternate location mapping by calling [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping).

 

 



