---
description: Use Merge Module Registry tables according to the type of registry information.
ms.assetid: 091429ff-a8f4-4e1b-929f-1559cd173c3d
title: Authoring Merge Module Registry Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module Registry Tables

Use Merge Module Registry tables according to the type of registry information.

## TypeLib, Class, AppId, ProgId, Extension, Verb, or MIME Tables

For type libraries, classes, extensions, and verbs, author registry information into the merge module's [TypeLib](typelib-table.md), [Class](class-table.md), [AppId](appid-table.md), [ProgId](progid-table.md), [Extension](extension-table.md), [Verb](verb-table.md), or [MIME](mime-table.md) tables. If you use the [Registry table](registry-table.md) to add this information, Windows 2000 cannot provide system-wide advertisement for these components.

Merge module authors may decide not to register using the Class table for the following reasons:

-   To be registered by the Class table, the file has to be the KeyPath of its component. This may require an unacceptable change in the organization of components.
-   A COM call may trigger an installer attempt to reinstall an advertised class. Authors may decide not to register a class using the Class table in order to avoid triggering a reinstallation when the client computer does not support a user interface.

## Registry Table

Use the Registry table to add registry information that cannot be authored into the TypeLib, Class, AppId, ProgId, Extension, Verb, or MIME tables. Windows 2000 cannot provide system-wide advertisement for components that use the Registry table.

When authoring the Registry table, refer to file paths using the \[\#File\] or \[!File\] format rather than as \[Directory\]Filename. The latter format does not support run-from-source installation. The former format also makes missing files and faulty components easier to detect.

Care is needed when using formatted text in the Key column of the Registry table. Because Windows Installer does not reinstall components that are already installed, using formatted text in this field may cause registry keys to be left behind on application removal.

## SelfReg Table

Using the SelfReg table is not recommended. For a list of reasons for not using self-registration, see [SelfReg table](selfreg-table.md). You should use the TypeLib, Class, AppId, ProgId, Extension, Verb, and MIME tables where possible instead and the Registry table in all other cases.

 

 



