---
description: The \_SummaryInformation table is a special table used with the Summary Information Stream. You can get or set the Summary Information Stream of a Windows Installer database by exporting or importing a text archive file named \_SummaryInformation.idt.
ms.assetid: 'b1b42e03-7a05-46d4-9c42-b87906535adb'
title: '_SummaryInformation'
ms.topic: article
ms.date: 05/31/2018
---

# \_SummaryInformation

The \_SummaryInformation table is a special table used with the [Summary Information Stream](summary-information-stream.md). You can get or set the Summary Information Stream of a Windows Installer database by exporting or importing a [text archive file](text-archive-files.md) named \_SummaryInformation.idt.

The .idt file of an exported \_SummaryInformation table has the following format.

-   The first row contains the table column names separated by tabs: PropertyId and Value. See the [Summary Information Stream Property Set](summary-information-stream-property-set.md) topic for a list of the properties and their ids (PID).
-   The second row contains the column definitions separated by tabs. The column definitions are specified in the same way as in the basic .idt [archive file format](archive-file-format.md). The PropertyId column can be a non-nullable short integer. The Value column can be a non-nullable localizable string 255 characters long.
-   The third row is the table name and the primary key column name separated by tabs: \_SummaryInformation and PropertyId.
-   The remaining rows in the file represent the PID and associated value, separated by tabs. Date and time in\_SummaryInformation are in the format: YYYY/MM/DD hh::mm::ss. For example, 1999/03/22 15:25:45.

The following is an example of the [Summary Information Stream](summary-information-stream.md) of a database in .idt format.

``` syntax
PropertyId   Value
i2  l255
_SummaryInformation PropertyId
1   1252
2   Installation Database
3   Internal Quick Test
4   Microsoft Corporation
5   Installer,MSI,Database
6   Installer Internal Release Quick Test
7   Intel;1033
9   {00000002-0001-0000-0000-624474736554}
12  1999/06/21
14  110
15  1
18  Windows Installer
```

When you use [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) or the [Import](database-import.md) method of the [**Database**](database-object.md) object to import a text archive table named \_SummaryInformation into an installer database, you write the "05SummaryInformation" stream in the database.

 

 



