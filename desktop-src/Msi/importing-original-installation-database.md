---
description: Begin authoring the upgrade package by copying the installation package and source directory tree of the of original product.
ms.assetid: 279f0ab6-a6fc-4594-af6c-5a69d6167300
title: Importing Original Installation Database
ms.topic: article
ms.date: 05/31/2018
---

# Importing Original Installation Database

Begin authoring the upgrade package by copying the installation package and source directory tree of the of original product. Instructions for authoring the installation package for MNP2000 are given in [An Installation Example](an-installation-example.md). You should copy the contents of the following folders:

C:\\Sample\\MNP2000.msi

C:\\Sample\\Notepad\\

C:\\Sample\\Binary\\

C:\\Sample\\Icon\\

Update the contents of the Notepad folder so that they match the source described in [Planning a Major Upgrade](planning-a-major-upgrade.md). Remove all obsolete source files, such as Baseball.txt, and replace with the updated files, such as Baseba01.txt. Add the additional new files provided by the upgrade, such as Opera01.txt.

Rename MNP2000.msi to MNP2001.msi. In subsequent steps you will use a table editor to modify this database into the .msi file for the upgrade. Database tables that are not explicitly modified in the subsequent sections are identical to the tables in the original product's database, MNP2000.msi.

[Continue](updating-directory-structure-for-an-upgrade.md)

 

 



