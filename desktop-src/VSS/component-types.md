---
Description: 'Components indicate the sort of data they represent through a type.'
ms.assetid: '19d785d5-09a7-48b9-a0a2-eca3049d67fe'
title: Component Types
---

# Component Types

Components indicate the sort of data they represent through a type.

Currently, component types (see [**VSS\_COMPONENT\_TYPE**](vss-component-type.md)) are limited to the following:

-   Database components
-   File groups

For implementation information about setting component types, see [Definition of Components by Writers](definition-of-components-by-writers.md).

Writers have a data typing that indicates their usage (see [**VSS\_SOURCE\_TYPE**](vss-source-type.md)), which can be the following:

-   A transactional database (such as an SQL server)
-   A nontransactional database (such as a spreadsheet client)
-   File group (other)

Specifying a component type as database allows for easier identification of its content, allows for separate handling of log and data files (see [**IVssCreateWriterMetadata**](ivsscreatewritermetadata.md) and [**IVssExamineWriterMetadata**](ivssexaminewritermetadata.md) for details), and enforces greater rigor in file selection by not allowing either recursive file selection or using an [*alternate path*](vssgloss-a.md#base-vssgloss-alternate-path) (see [**IVssCreateWriterMetadata::AddDatabaseFiles**](ivsscreatewritermetadata-adddatabasefiles.md) and [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](ivsscreatewritermetadata-adddatabaselogfiles.md)).

With a file group component, on the other hand, at the price of not knowing what data it contains, you have greater freedom about how files are inserted, because you can use recursive specification and alternate paths.

Additional component types may be added in the future.

 

 



