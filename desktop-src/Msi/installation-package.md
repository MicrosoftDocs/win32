---
description: An installation package contains all of the information that the Windows Installer requires to install or uninstall an application or product and to run the setup user interface.
ms.assetid: 532b3492-919f-4999-b86c-e3c210876141
title: Installation Package
ms.topic: article
ms.date: 05/31/2018
---

# Installation Package

An installation package contains all of the information that the Windows Installer requires to install or uninstall an application or product and to run the setup user interface. Each installation package includes an .msi file, containing an installation database, a summary information stream, and data streams for various parts of the installation. The .msi file can also contain one or more transforms, internal source files, and external source files or cabinet files required by the installation.

Application developers must author an installation to use the installer. Because the installer organizes installations around the concept of [components and features](components-and-features.md), and stores all information about the installation in a relational database, the process of authoring an installation package broadly entails the following steps:

-   Identify the features to be presented to users.
-   Organize the application into components.
-   Populate the installation database with information.
-   Validate the installation package.

The next section discusses installer components and features. For more information, see [Components and Features](components-and-features.md). The choice of features is commonly determined by the application's functionality from the user's perspective.

It is recommended that developers use a standard procedure for choosing components. For more information, see [Organizing Applications into Components](organizing-applications-into-components.md).

Package authors can use third-party package creation tools, or a table editor and the Windows Installer SDK, to populate the installation database. All installation packages need to be validated for internal consistency. For more information, see [Package Validation](package-validation.md).

 

 



