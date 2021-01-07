---
description: You can add localization information to an installation database by using a database table editor such as Orca that is provided with the Windows Installer SDK, or by calling the Database Functions from an application.
ms.assetid: cc1eb336-5dec-40cc-8aa5-564cd167855d
title: Code Page Handling of Parameter Strings
ms.topic: article
ms.date: 05/31/2018
---

# Code Page Handling of Parameter Strings

You can add localization information to an installation database by using a database table editor such as Orca that is provided with the Windows Installer SDK, or by calling the [Database Functions](database-functions.md) from an application. Be careful to only pass string parameters that use the code page of the database that is being localized. If a string parameter contains characters that cannot be represented by the code page of the database, the Installer returns an error when calling [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). For a list of numeric code pages, see [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md).

For more information, see [Determining an Installation Database's Code Page](determining-an-installation-database-s-code-page.md).

## Adding Localization Information to a Database

When you add localization information to a database, the code page of the database must be supported by the operating system. It does not have to be the current code page of the system. [**IsValidCodePage**](/windows/desktop/api/winnls/nf-winnls-isvalidcodepage) must return **TRUE** for the database code page. Because the system converts ANSI strings to Unicode, there is an error if the current user code page is not the same as the database code page.

Calling the ANSI version of the Windows Installer API converts the localized string to Unicode by using the current system code page. When the database is committed, the Unicode string is converted to ANSI using the code page of the database. If the current system code page differs from the code page of the localized string, the result can be a loss of data and incorrect string conversion.

The following procedure shows you how to store the localization data.

**To store localization data**

1.  Set the code page of the database to the code page of the localized string.
2.  Convert the ANSI string to Unicode by using the [**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar) function, and specify the code page of the localized data.
3.  Call the Unicode version of the Windows Installer API by using the Unicode string to add the localized data.
4.  Commit the localization changes to the database by using [**MsiDatabaseCommit**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasecommit).

You can also add localization information to an installation database by importing and exporting ASCII text archive files. For more information, see [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md).

 

 
