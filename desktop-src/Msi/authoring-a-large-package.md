---
description: Use this guideline to author a Windows Installer package that contains more than 32767 files.
ms.assetid: 3145629f-cc0a-4216-8549-76bb61070772
title: Authoring a Large Package
ms.topic: article
ms.date: 05/31/2018
---

# Authoring a Large Package

Use this guideline to author a Windows Installer package that contains more than 32767 files.

If your Windows Installer package contains more than 32767 files, you must change the schema of the database to increase the limit of the following columns:

-   The Sequence column of the [File table](file-table.md).
-   The LastSequence column of the [Media table](media-table.md).
-   The Sequence column of the [Patch table](patch-table.md).

For more information, see [Column Definition Format](column-definition-format.md).

**To increase the limit of a database column**

1.  Export the table to an .idt file. For details, see [Msidb.exe](msidb-exe.md), [Export Files](export-files.md), and [Importing and Exporting](importing-and-exporting.md).
2.  Edit the .idt file to change the column type from i2 to i4, or from I2 to I4.
3.  Export the [\_Validation](-validation-table.md) table to an .idt file.
4.  Edit the .idt file to change the values in the MaxValue column of the [\_Validation](-validation-table.md) table to accommodate the increased column widths.
5.  Import the .idt files back into the database.

Note that transforms and patches cannot be created between two packages with different column types.

 

 



