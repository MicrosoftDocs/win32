---
description: The recommended approach for handling code pages is to author a neutral base database that only contains characters that can be translated into any code page.
ms.assetid: 8ded41a6-6e5b-4a39-b783-e2b9f83eaed4
title: Creating a Database with a Neutral Code Page
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Database with a Neutral Code Page

The recommended approach for handling code pages is to author a neutral base database that only contains characters that can be translated into any code page. The database may then be set to the code page of the localization and the localization information can be added as described in [Localizing a Windows Installer Package](localizing-a-windows-installer-package.md).

To author a neutral database, avoid extended characters that do not belong to the ASCII character set and therefore require a special code page. For example, the copyright sign, ©, and the registered trademark sign, , are not ASCII characters, and require a special ANSI code page for proper display. Instead use (c) and (r), because these characters can be translated or transformed to the symbols for the English-language version. This neutral database can then be localized by setting its code page and adding localization information by table editing or by importing text archive files.

 

 



