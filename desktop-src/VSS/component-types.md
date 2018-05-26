---
Description: Components indicate the sort of data they represent through a type.
ms.assetid: 19d785d5-09a7-48b9-a0a2-eca3049d67fe
title: Component Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Component Types

Components indicate the sort of data they represent through a type.

Currently, component types (see [**VSS\_COMPONENT\_TYPE**](/windows/win32/VsWriter/ne-vswriter-vss_component_type?branch=master)) are limited to the following:

-   Database components
-   File groups

For implementation information about setting component types, see [Definition of Components by Writers](definition-of-components-by-writers.md).

Writers have a data typing that indicates their usage (see [**VSS\_SOURCE\_TYPE**](/windows/win32/VsWriter/ne-vswriter-vss_source_type?branch=master)), which can be the following:

-   A transactional database (such as an SQL server)
-   A nontransactional database (such as a spreadsheet client)
-   File group (other)

Specifying a component type as database allows for easier identification of its content, allows for separate handling of log and data files (see [**IVssCreateWriterMetadata**](/windows/win32/VsWriter/nl-vswriter-ivsscreatewritermetadata?branch=master) and [**IVssExamineWriterMetadata**](/windows/win32/VsBackup/nl-vsbackup-ivssexaminewritermetadata?branch=master) for details), and enforces greater rigor in file selection by not allowing either recursive file selection or using an [*alternate path*](vssgloss-a.md#base-vssgloss-alternate-path) (see [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles?branch=master) and [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles?branch=master)).

With a file group component, on the other hand, at the price of not knowing what data it contains, you have greater freedom about how files are inserted, because you can use recursive specification and alternate paths.

Additional component types may be added in the future.

 

 



