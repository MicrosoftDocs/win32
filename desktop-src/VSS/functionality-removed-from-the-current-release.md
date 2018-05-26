---
Description: The Windows Server 2003 release of VSS no longer supports the following
ms.assetid: 01993cae-433e-4d01-b805-f97592369575
title: Functionality Removed From Windows Server 2003
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functionality Removed From Windows Server 2003

The Windows Server 2003 release of VSS no longer supports the following:

-   Writers cannot specify new file restore destinations ([*new target locations*](vssgloss-n.md#base-vssgloss-new-target-location)) at restore operations.
-   Remounting an exposed shadow copy as a writable volume is no longer supported. The **IVssBackupComponents::RemountReadWrite** method is no longer available.
-   Writers cannot specify explicitly included files (using [**IVssCreateWriterMetadata::AddIncludeFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addincludefiles?branch=master)). Files can be added to a component only as part of a file set by using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup?branch=master), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles?branch=master), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles?branch=master).

    Files can still be explicitly excluded from a component by using [**IVssCreateWriterMetadata::AddExcludeFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addexcludefiles?branch=master).

 

 



