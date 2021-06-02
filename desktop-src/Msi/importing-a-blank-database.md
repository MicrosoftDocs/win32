---
description: To reproduce the sample you need to copy, or create with a software tool, a Windows Installer database file.
ms.assetid: e239bbe4-3290-40f0-9f28-0e8aa4ed23f8
title: Importing a Blank Database
ms.topic: article
ms.date: 05/31/2018
---

# Importing a Blank Database

To reproduce the sample you need to copy, or create with a software tool, a Windows Installer database file. A totally blank installation database, Schema.msi, is provided with the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The SDK also provides a partially blank database, uisample.msi, that contains the suggested sequence tables and data required for a simple user interface. Make a copy of uisample.msi and move it into the same directory containing the Notepad folder you created in [Planning the Installation](planning-the-installation.md). Rename the file MNP2000.msi. The installation database file and the source files must both be located at the root of the same directory. For example:

C:\\Sample\\MNP2000.msi

C:\\Sample\\Notepad\\

If you do not use Uisample.msi, then you must obtain a blank database, such as Schema.msi, and enter information for the installation using a database editing tool such as Orca, which is provided with the SDK, or another database editor.

[Continue](specifying-directory-structure.md)

 

 



