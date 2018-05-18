---
Description: 'The combination of path, file specification, and recursion flag (wszPath, wszFileSpec, and bRecursive, respectively) must match that of one of the file sets added to one of the writer''s components using IVssCreateWriterMetadata::AddFilesToFileGroup, IVssCreateWriterMetadata::AddDatabaseFiles, or IVssCreateWriterMetadata::AddDatabaseLogFiles when:'
ms.assetid: 'debf181a-1579-46f2-86ef-a1d2a850e99e'
title: Semantic Changes to Windows Server 2003
---

# Semantic Changes to Windows Server 2003

The combination of path, file specification, and recursion flag (*wszPath*, *wszFileSpec*, and *bRecursive*, respectively) must match that of one of the file sets added to one of the writer's components using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](ivsscreatewritermetadata-addfilestofilegroup.md), [**IVssCreateWriterMetadata::AddDatabaseFiles**](ivsscreatewritermetadata-adddatabasefiles.md), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](ivsscreatewritermetadata-adddatabaselogfiles.md) when:

-   A requester adds a new target using [**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md).
-   A writer adds an alternate location mapping using [**IVssCreateWriterMetadata::AddAlternateLocationMapping**](ivsscreatewritermetadata-addalternatelocationmapping.md).
-   Existing files are added as differenced files using [**IVssComponent::AddDifferencedFilesByLastModifyTime**](ivsscomponent-adddifferencedfilesbylastmodifytime.md).
-   A requester indicates that an alternate location mapping was used to restore a file set using [**IVssBackupComponents::AddAlternativeLocationMapping**](ivssbackupcomponents-addalternativelocationmapping.md).

 

 



