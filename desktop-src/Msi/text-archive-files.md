---
description: The Windows Installer database tables can be exported to ASCII text files by using MsiDatabaseExport or the Export method of the Database object.
ms.assetid: '49210242-bd32-4e5c-b782-a132d670fdfe'
title: Text Archive Files
ms.topic: article
ms.date: 05/31/2018
---

# Text Archive Files

The Windows Installer database tables can be exported to ASCII text files by using [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) or the [**Export**](database-export.md) method of the [**Database**](database-object.md) object. The information in these text archive files can then be imported back into a Windows Installer database using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) or the [Import](database-import.md) method of the **Database** object.

Tools such as [msidb.exe](msidb-exe.md) are capable of exporting and importing text archive files. See [Export Files](export-files.md) and [Import Files](import-files.md) for [Windows Installer Scripting Examples](windows-installer-scripting-examples.md) that can export and import text archive files from a database.

> [!Note]  
> Text archive files are not intended as a means to edit the installation database. You should use a Windows Installer table editing tool, such as [Orca](orca-exe.md) or a third-party tool, to create and modify an installation package.

 

Text archive files can be used for the following purposes.

-   Text archive files can be used with version control systems.
-   To remove wasted storage space and reduce the final size of .msi files. See [Reducing the Size of an .msi File](reducing-the-size-of-an--msi-file.md).
-   To add localization information to an installation database. For more information, see [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md).

-   To determine the code page of a database. See [Determining an Installation Database's Code Page](determining-an-installation-database-s-code-page.md).
-   To set the code page of a database. See [Setting the code page of a database](setting-the-code-page-of-a-database.md).
-   To increase the limit of a database column. Export the table using [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta), edit the exported .idt file, and then import the table using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). Authors cannot change the column data types, nullability, or localization attributes of any columns in standard tables. See also [Authoring a Large Package](authoring-a-large-package.md).

The following pages describe text archive pages and their formats.

-   [Archive File Format](archive-file-format.md)
-   [ASCII Data in Text Archive Files](ascii-data-in-text-archive-files.md)
-   [\_ForceCodepage](-forcecodepage.md)
-   [\_SummaryInformation](-summaryinformation.md)

 

 



