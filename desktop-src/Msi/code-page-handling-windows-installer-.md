---
description: The Windows Installer stores all database strings in a single shared string pool to reduce the size of the database, and to improve performance. For a list of numeric code pages, see Localizing the Error and ActionText Tables.
ms.assetid: 5d413fb7-99da-49f3-ace3-ec285df2e634
title: Code Page Handling (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Code Page Handling (Windows Installer)

The Windows Installer stores all database strings in a single shared string pool to reduce the size of the database, and to improve performance. For a list of numeric code pages, see [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md).

For more information, [Determining an Installation Database's Code Page](determining-an-installation-database-s-code-page.md).

Windows Installer uses [**IsValidCodePage**](/windows/desktop/api/winnls/nf-winnls-isvalidcodepage) to determine whether the code page is valid.

### Localizing a Windows Installer Package

If you localize a Windows Installer package, it may involve modifying information in database tables, exporting the tables to ANSI text archive files, and then importing the archive files into the database that is being localized. You can also add localization changes to a database by using a database table editor or the [Database Functions](database-functions.md). It is important to set the code page of the database that is being localized before you make any localization changes to the database. Do not set the code page of the database after localizing the database, because this can corrupt extended characters. For more information, see [Setting the Code Page of a Database](setting-the-code-page-of-a-database.md).

The recommended approach for handling code pages is to author a neutral database that only contains characters that can be translated into any code page. For more information, see [Creating a Database with a Neutral Code Page](creating-a-database-with-a-neutral-code-page.md).

If you add localization information with database archive files, you can use [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) to export tables from a database that contains localization changes to ANSI text archive files, and then import these into the database being localized with [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). The code page of an exported archive file is always the same as its parent database. The code pages of an imported file and the database that is receiving the file must be identical, or at least one of the two code pages must be neutral. For more information, see [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md).

If you add localization information with a text editor or the [Database Functions](database-functions.md) be careful to only pass string parameters to the Windows Installer API that uses the code page of the database that is being localized. If a string parameter contains characters not represented by the code page of the database, an error occurs when calling [**MsiDatabaseCommit**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasecommit). For more information, see [Code Page Handling of Parameter Strings](code-page-handling-of-parameter-strings.md).

If one package is used to install multiple language versions of a product, the transform that is used to localize strings can also change the code page of the database.

 

 
