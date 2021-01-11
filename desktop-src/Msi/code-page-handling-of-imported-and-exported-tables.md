---
description: You can add localization information to an installation database by importing and exporting ASCII text archive files using MsiDatabaseExport and MsiDatabaseImport.
ms.assetid: dc52313b-38e7-43cc-abfd-86966c836fce
title: Code Page Handling of Imported and Exported Tables
ms.topic: article
ms.date: 05/31/2018
---

# Code Page Handling of Imported and Exported Tables

You can add localization information to an installation database by importing and exporting ASCII text archive files using [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) and [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). Because the database string pool uses an ANSI code page, both the database and exported [Text Archive Files](text-archive-files.md) have code pages.

When a [Text Archive File](text-archive-files.md) is exported from a database, the code page of the archive file is the same as the parent database. For a list of numeric code pages, see [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md).

> [!Note]  
> Exporting a table to a text archive file translates the control characters to avoid conflicts with file delimiters.

 

## ASCII Text Archive Files

The ASCII [Text Archive Files](text-archive-files.md) exported by [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) are explained in the following format:

-   The names of the table columns are written on the first line.
-   The column formats are written on the second line.
-   If the table contains only ASCII data, the third line of the text file is the table name followed by a list of the primary keys.
-   If the table contains non-ASCII data and the database is stamped with a numeric code page, the code page number appears at the beginning of the third line.
-   If the database contains non-ASCII data, but the database is not stamped with the numeric code page, the current system code page number is written at the beginning of the third line.
-   The remaining lines of the text file are the data in the specified code page.
-   If a table contains streams, [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) exports each stream in the table to a separate file.

### Neutral and Non-Neutral Code Pages

You can facilitate localization by starting with a database that has a neutral code page:

-   A blank database has a neutral code page.
-   A database that does not contain extended characters that require a code page to be represented in ASCII has a neutral code page.

For more information, see [Creating a Database with a Neutral Code Page](creating-a-database-with-a-neutral-code-page.md).

Neutral and non-neutral code pages have the following characteristics:

-   If a [Text Archive File](text-archive-files.md) with a non-neutral code page is imported into a database that has a different non-neutral code page, the Installer returns an error when [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) is called.
-   A [Text Archive File](text-archive-files.md) that has a neutral code page can be imported into a database that has any code page.
-   A [Text Archive File](text-archive-files.md) that has any code page can be imported into a database that has a neutral code page.
-   Importing a [Text Archive File](text-archive-files.md) into a database with a neutral code page sets the code page of the database to the archive file code page. All archive files subsequently imported into the database must have the same code page as the first file.

For more information, see [Determining an Installation Database Code Page](determining-an-installation-database-s-code-page.md) and [Setting the Code Page of a Database](setting-the-code-page-of-a-database.md).

The [Text Archive Files](text-archive-files.md) that are exported by [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) can be used with version control systems. Use the [Database Functions](database-functions.md) or a database table editor to edit the database.

You can add localization information to an installation database by using a database table editor or the Windows Installer API. For more information, see [Code Page Handling of Parameter Strings](code-page-handling-of-parameter-strings.md).

 

 



