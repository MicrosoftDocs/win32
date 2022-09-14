---
description: For general information about localization, see Globalization Services.
ms.assetid: 734961f6-de0a-4c54-9866-ade994c41c7e
title: Localizing a Windows Installer Package
ms.topic: article
ms.date: 05/31/2018
---

# Localizing a Windows Installer Package

For general information about localization, see [Globalization Services](../intl/globalization-services.md). Localizing a Windows Installer package requires modifying the strings displayed by the user interface and may also require adding or modifying product resources. For example, localization may include the addition of international DLLs and localized files to the product.

**To localize a Windows Installer package**

1.  Prepare for localization when authoring the original installation package. Design the layout of localized files such that different language versions can safely coexist when installed on the user's computer. Organize files requiring localization into separate components and install these files into separate directories. Author a base installation database that has a neutral control page. See [Preparing a Windows Installer package for localization](preparing-a-windows-installer-package-for-localization.md).
2.  Always set the code page of the database being localized prior to adding any localized data. If the code page of the database being localized is neutral, see [Setting the code page of a database](setting-the-code-page-of-a-database.md). To determine the code page see [Determining an installation database's code page](determining-an-installation-database-s-code-page.md).
3.  Import a localized [Error table](error-table.md) and [ActionText table](actiontext-table.md) into the database. For more information, see [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md) for a list of languages supported by the Microsoft Windows Software Development Kit (SDK). You may import these tables using Msidb.exe or [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta).
4.  Modify any of the other localizable columns in the database using a table editor or SQL queries. For the SQL access functions, see [Working with Queries](working-with-queries.md). The topics for the database tables identify which database columns can be localized. For more information, see the list of tables in [Database Tables](database-tables.md).
5.  Set the [**ProductLanguage**](productlanguage.md) property in the [Property table](property-table.md) to the LANGID of the database. When authoring a package as language neutral, set the ProductLanguage property to 0 and use the MS Shell Dlg font as the text style for all authored dialog boxes. Because some fonts do not support all of the character sets, you can ensure that the text is correctly displayed on all localized versions of the operating system by using this font.
6.  Set the language field of the [**Template Summary**](template-summary.md) property to reflect the LANGID of the database.
7.  If the text strings in the [summary information stream](summary-information-stream.md) are localized, set the [**Codepage Summary**](codepage-summary.md) property to the code page.
8.  Set the [**ProductCode**](productcode.md) property in the [Property table](property-table.md) and set the package code in the [**Revision Number Summary**](revision-number-summary.md) property to a new package code. A localized product is considered a different product. For example, the German and English versions of an application are considered two different products and must have different product codes.
9.  Localization may require modifying resources that already exist or the addition of new resources such as files or registry keys. Check to be sure that the component code is changed for every existing component that has had a new resource added. Other modifications may also require changes to a component's code. For more information see [Changing the Component Code](changing-the-component-code.md).
10. Be sure to save localization and other changes to the database by saving the package with the editing tool or by calling [**MsiDatabaseCommit**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasecommit).

For more information, see [A Localization Example](a-localization-example.md).

 

 
