---
description: A backup set is a list of all files to be backed up, their locations, and how to back them up.
ms.assetid: 34a66a9c-c1bc-437d-b034-59dc0c88228c
title: Generating A Backup Set
ms.topic: article
ms.date: 05/31/2018
---

# Generating A Backup Set

A backup set is a list of all files to be backed up, their locations, and how to back them up.

A requester must make use of the files contained on the shadow-copied volumes after the [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) returns successfully to generate the full list of files to be backed up.

In addition, a requester must deal with the possibility that some files have [*alternate paths*](vssgloss-a.md) and that some files have been excluded.

An algorithm for selecting files to back up should go on a [*writer instance*](vssgloss-w.md) by writer instance, component-by-component basis (as will be the case during restore; see [Generating a Restore Set](generating-a-restore-set.md)) and might proceed by doing the following:

1.  Determining the volumes that contain the writer's files and the corresponding device objects
2.  Using the [*file set*](vssgloss-f.md) information (contained in [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) objects returned by [**IVssExamineWriterMetadata::GetExcludeFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getexcludefile)) to create a list of the explicitly excluded files, if necessary using **FindFileFirst**, **FindFileFirstEx**, and **FindNextFile**.
3.  Iterating over all of a writer's components, using [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent). If a selectable component is selected, use [*logical path*](vssgloss-l.md) to obtain those nonselectable components associated with it in a component set. (See [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md).)
4.  Obtaining the [*file sets*](vssgloss-f.md) contained in each selected component by using the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface corresponding to each component it contains.
5.  Generating a list of files from the specifications—if necessary using **FindFileFirst**, **FindFileFirstEx**, and **FindNextFile**.
6.  Checking each file in the list generated from component information against the list of excluded files generated above. This should be done using the default path for the file (returned by [**IVssWMFiledesc::GetPath**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getpath)), not by the alternate path returned by [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation)). If the file matches the excluded list, it will not be backed up.
7.  Choosing the actual location from which to back up (using the alternate path if it was set)
8.  At this point, a full list of files and their locations is available and a backup can begin.

After an initial backup set has been generated for all writers that are present on the system, the requester then checks the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\BackupRestore\\FilesNotToBackup**

The requester uses the subkeys under this key as follows:

-   If a writer is present on the system, and there is a subkey whose name matches the writer's name, that subkey must be ignored.
-   If a writer was present on the system but is currently absent from the backup set, and there is a matching subkey, any files specified in the subkey data are excluded and must be removed from the backup set.
-   The backup application adds files to the subkey data by creating a MULTI\_SZ value containing a list of file specifications for the files that must not be backed up. Each string in the MULTI\_SZ value should contain one file specification.
-   File specifications can contain the ? and \* wildcard characters. A specification can be made recursive by appending /s to the end. For example, specifying "%TEMP%\\\* /s" causes all files in the %TEMP% directory and all of its subdirectories not to be backed up.

 

 



