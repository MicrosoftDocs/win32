---
description: 'The Windows Server 2003 release of VSS no longer supports the following:'
ms.assetid: 01993cae-433e-4d01-b805-f97592369575
title: Functionality Removed From Windows Server 2003
ms.topic: article
ms.date: 05/31/2018
---

# Functionality Removed From Windows Server 2003

The Windows Server 2003 release of VSS no longer supports the following:

-   Writers cannot specify new file restore destinations ([*new target locations*](vssgloss-n.md)) at restore operations.
-   Remounting an exposed shadow copy as a writable volume is no longer supported. The **IVssBackupComponents::RemountReadWrite** method is no longer available.
-   Writers cannot specify explicitly included files (using [**IVssCreateWriterMetadata::AddIncludeFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addincludefiles)). Files can be added to a component only as part of a file set by using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles).

    Files can still be explicitly excluded from a component by using [**IVssCreateWriterMetadata::AddExcludeFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addexcludefiles).

 

 



