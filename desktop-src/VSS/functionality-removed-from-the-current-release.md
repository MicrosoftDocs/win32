---
Description: 'The Windows Server 2003 release of VSS no longer supports the following:'
ms.assetid: '01993cae-433e-4d01-b805-f97592369575'
title: Functionality Removed From Windows Server 2003
---

# Functionality Removed From Windows Server 2003

The Windows Server 2003 release of VSS no longer supports the following:

-   Writers cannot specify new file restore destinations ([*new target locations*](vssgloss-n.md#base-vssgloss-new-target-location)) at restore operations.
-   Remounting an exposed shadow copy as a writable volume is no longer supported. The **IVssBackupComponents::RemountReadWrite** method is no longer available.
-   Writers cannot specify explicitly included files (using [**IVssCreateWriterMetadata::AddIncludeFiles**](ivsscreatewritermetadata-addincludefiles.md)). Files can be added to a component only as part of a file set by using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](ivsscreatewritermetadata-addfilestofilegroup.md), [**IVssCreateWriterMetadata::AddDatabaseFiles**](ivsscreatewritermetadata-adddatabasefiles.md), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](ivsscreatewritermetadata-adddatabaselogfiles.md).

    Files can still be explicitly excluded from a component by using [**IVssCreateWriterMetadata::AddExcludeFiles**](ivsscreatewritermetadata-addexcludefiles.md).

 

 



