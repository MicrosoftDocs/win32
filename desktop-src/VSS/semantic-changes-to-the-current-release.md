---
Description: The combination of path, file specification, and recursion flag (wszPath, wszFileSpec, and bRecursive, respectively) must match that of one of the file sets added to one of the writers components using IVssCreateWriterMetadataAddFilesToFileGroup, IVssCreateWriterMetadataAddDatabaseFiles, or IVssCreateWriterMetadataAddDatabaseLogFiles when
ms.assetid: debf181a-1579-46f2-86ef-a1d2a850e99e
title: Semantic Changes to Windows Server 2003
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Semantic Changes to Windows Server 2003

The combination of path, file specification, and recursion flag (*wszPath*, *wszFileSpec*, and *bRecursive*, respectively) must match that of one of the file sets added to one of the writer's components using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup?branch=master), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles?branch=master), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles?branch=master) when:

-   A requester adds a new target using [**IVssBackupComponents::AddNewTarget**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget?branch=master).
-   A writer adds an alternate location mapping using [**IVssCreateWriterMetadata::AddAlternateLocationMapping**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addalternatelocationmapping?branch=master).
-   Existing files are added as differenced files using [**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime?branch=master).
-   A requester indicates that an alternate location mapping was used to restore a file set using [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping?branch=master).

 

 



