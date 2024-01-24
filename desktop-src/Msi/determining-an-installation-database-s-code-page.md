---
description: To determine the code page of a database, call MsiDatabaseExport with hDatabase set to the handle of the database and szTableName set to \_ForceCodepage.
ms.assetid: afa3fbd9-9f54-4f72-ab5d-cb0dbbd9946c
title: Determining an Installation Database's Code Page
ms.topic: article
ms.date: 05/31/2018
---

# Determining an Installation Database's Code Page

To determine the code page of a database, call [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) with *hDatabase* set to the handle of the database and *szTableName* set to \_ForceCodepage. This exports a text file with an .idt extension. The first two lines of this file are blank. The third line is the ANSI code page number, followed by a tab, followed by the name \_ForceCodepage. See also [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md).

An example of determining the code page by using the [**Export method**](database-export.md) is provided in the Windows Installer SDK as a part of the utility WiLangId.vbs. For more information about using WiLangId.vbs see the topic: [Manage Language and Codepage](manage-language-and-codepage.md).

 

 



