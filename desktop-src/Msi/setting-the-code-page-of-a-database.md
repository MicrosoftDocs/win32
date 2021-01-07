---
description: Always set the code page of a database prior to adding any localization information.
ms.assetid: 0d8aee30-989a-4093-8718-1bb90029c0fb
title: Setting the Code Page of a Database
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Code Page of a Database

Always set the code page of a database prior to adding any localization information. Attempting to set the code page after entering data into the database is not recommended because this could corrupt extended characters. Localization can be greatly facilitated by starting with a database that is code page neutral. For details, see [Creating a database with a neutral code page](creating-a-database-with-a-neutral-code-page.md). You may determine the current code page of a database as described in [Determining an installation database's code page](determining-an-installation-database-s-code-page.md). See [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md) for a list of numeric code pages.

You may set the code page of a blank database, or a database with a neutral code page, by importing a text archive file having a non-neutral code page with [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). This sets the code page of the database to the imported file's code page. All archive files subsequently imported into the database must then have the same code page as the first file. If a text archive file is exported from a database, the code page of the archive file is the same as the parent database. See [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md).

The code page of any database may be set to a specified numeric code page by using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) to import a text archive file with the following format: Two blank lines; followed by a line containing the numeric code page, a tab delimiter, and the exact string: \_ForceCodepage. Note that with Windows 2000, this translates all of the strings in the database to the code page of \_ForceCodepage. This may be intended when localizing an existing database and translating all non-neutral strings to the new code page. However, this causes an error if the database contains non-neutral strings that are not to be translated.

The utility WiLangId.vbs provides an example of how to set the code page of a package using the [**Import method**](database-import.md). A copy of WiLangId.vbs is provided in the Windows Installer SDK. You can use this utility to determine the language versions that are supported by the database (Package), the language the installer uses for any strings in the user interface that are not authored into the database (Product), or the single ANSI code page for the string pool (Codepage). For information on using WiLangId.vbs see the help page: [Manage Language and Codepage](manage-language-and-codepage.md).

To determine the values of Product, Package, and Codepage, run WiLangId.vbs as follows.

**cscript wilangid.vbs** *\[path to database\]*

To set the Codepage of the package run the following command line.

**cscript wilangid.vbs** *\[path to database\]* **Codepage** *\[value\]*

For example, to set the Codepage of test.msi to the numeric ANSI code page value 1252, run the following command line.

**cscript wilangid.vbs c:\\temp\\test.msi Codepage 1252**

 

 



