---
description: "The combination of path, file specification, and recursion flag (wszPath, wszFileSpec, and bRecursive, respectively) must match that of one of the file sets added to one of the writer's components using IVssCreateWriterMetadata::AddFilesToFileGroup, IVssCreateWriterMetadata::AddDatabaseFiles, or IVssCreateWriterMetadata::AddDatabaseLogFiles when:"
ms.assetid: debf181a-1579-46f2-86ef-a1d2a850e99e
title: Semantic Changes to Windows Server 2003
ms.topic: article
ms.date: 05/31/2018
---

# Semantic Changes to Windows Server 2003

The combination of path, file specification, and recursion flag (*wszPath*, *wszFileSpec*, and *bRecursive*, respectively) must match that of one of the file sets added to one of the writer's components using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) when:

-   A requester adds a new target using [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget).
-   A writer adds an alternate location mapping using [**IVssCreateWriterMetadata::AddAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addalternatelocationmapping).
-   Existing files are added as differenced files using [**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime).
-   A requester indicates that an alternate location mapping was used to restore a file set using [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping).

 

 



