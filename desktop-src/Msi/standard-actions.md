---
description: An action encapsulates a typical function performed during the installation or maintenance of an application. Windows Installer has many built-in standard actions. Developers of installation packages can also author their own custom actions.
ms.assetid: '33651988-e371-4258-96a7-bcd7d6762161'
title: Standard Actions
ms.topic: article
ms.date: 05/31/2018
---

# Standard Actions

An action encapsulates a typical function performed during the installation or maintenance of an application. Windows Installer has many built-in standard actions. Developers of installation packages can also author their own [custom actions](custom-actions.md).

Examples of installer standard actions include:

-   [CreateShortcuts action](createshortcuts-action.md): Manages the creation of shortcuts to files installed with the current application. This action uses the [Shortcut table](shortcut-table.md) for its data.
-   [InstallFiles action](installfiles-action.md): Copies selected files from the source directory to the destination directory. This action uses the [File table](file-table.md) for its data.
-   [WriteRegistryValues action](writeregistryvalues-action.md): Sets up registry information the application requires in the registry. This action uses the [Registry table](registry-table.md) for its data.

The following sections discuss standard actions.

-   [About Standard Actions](about-standard-actions.md)
-   [Using Standard Actions](using-standard-actions.md)
-   [Standard Actions Reference](standard-actions-reference.md)

 

 



