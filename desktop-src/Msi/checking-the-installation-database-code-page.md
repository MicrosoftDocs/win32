---
description: A code page is an internal table that the operating system uses to map symbols (letters, numerals, and punctuation characters) to a character number.
ms.assetid: e11193a2-2c72-43a9-8d35-fa524044e306
title: Checking the Installation Database Code Page
ms.topic: article
ms.date: 05/31/2018
---

# Checking the Installation Database Code Page

A *code page* is an internal table that the operating system uses to map symbols (letters, numerals, and punctuation characters) to a character number. Different code pages provide support for the character sets used in different countries or regions. Code pages are referred to by number; for example, code page 932 represents the Japanese character set, and code page 950 represents one of the Chinese character sets. See [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md) for a list of ASCII code pages.

The same ASCII code page, 1252, may be used for English and French. Therefore the code page for the database MNP2000.msi (English) does not need to be reset to change the installation to French.

For more information about setting the code page see [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md).

[Continue](importing-localized-error-and-actiontext-tables.md)

 

 



