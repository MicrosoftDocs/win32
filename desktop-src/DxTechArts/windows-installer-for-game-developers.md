---
title: Windows Installer for Game Developers
description: This article gives an overview of Windows Installer, specifically targeted to game developers. For detailed documentation on the features and APIs mentioned in this article, please refer to the Windows Platform SDK.
ms.assetid: 07401792-b34b-71c9-18f8-a11c916c7d81
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer for Game Developers

Shows how Windows Installer can be used to install games on end-user machines. Windows Installer offers full support for a customized user interface, as well as for patching.

Microsoft Windows Installer is the preferred API for installing software on Windows-based computers. While many of the features of Windows Installer are designed to support deployment of business applications in a corporate environment, Windows Installer is also completely suitable for installing games on end-user machines. The primary advantages of using Windows Installer for game installation are:

-   Reliable uninstall
-   Ability to install content on demand
-   Support for completely custom user interface
-   Efficient patching

This article gives an overview of Windows Installer, specifically targeted to game developers. For detailed documentation on the features and APIs mentioned in this article, please refer to the Windows Platform SDK.

-   [Overview](#overview)
-   [Key Windows Installer Concepts](#key-windows-installer-concepts)
    -   [Components](#components)
    -   [Features](#features)
-   [Install States](#install-states)
-   [Install on Demand](#install-on-demand)
-   [Custom User Interface](#custom-user-interface)
-   [Patching](#patching)
-   [Other Resources](#other-resources)

## Overview

All Windows Installer-based setups use an installation database file called an MSI file to describe how the application is to be installed. The MSI file contains information on what files, registry keys, desktop shortcuts, file associations, and other application elements are to be installed. The actual files to be installed can be compressed within the MSI file itself, bundled and compressed into separate "cabinet files", or stored elsewhere on the installation media as individual uncompressed files. The MSI file can also reference externally implemented custom actions, in order to allow for actions for which the MSI file does not natively allow.

An MSI file can optionally contain a user interface to guide the user through the installation process. This UI is adequate for most applications. However, it has the look and feel of a regular Windows application, and many game developers prefer to have their setup application maintain the look and feel of the game itself, in order to provide a more consistent end-user experience. To support this fully custom UI scenario, a setup application can turn off Windows Installer's built-in UI, and handle the entire user interface itself. The Windows Installer API exposes a callback mechanism to allow a custom setup UI to be notified of the progress of the installation, as well as important events such as disk change requests.

Windows Installer is not an end-to-end solution for creating setups. It is only an API that can be used by a setup program to do the actual installation of files, registry keys, desktop shortcuts, and other elements of the application. Recent versions of all of the major commercial setup tools (for example, InstallShield, WISE, and Microsoft Visual Studio) support Windows Installer. These tools provide convenient user interfaces for creating the setup for a game, but they rely on the Windows Installer API to do much of the actual installation. These tools can also be used just to build an MSI database containing the setup package, which can then be installed from a custom-written setup UI. As an alternative to third-party tools, the Windows Installer API provides all of the functions necessary for creating and manipulating an MSI database programmatically, and the Windows Platform SDK includes a bare-bones MSI database-editing tool called Orca.

## Key Windows Installer Concepts

Here are the Windows Installer components and features.

### Components

An application is made up of one or more components, identified by a GUID component ID. A component is an atomic unit; it is either entirely installed or not installed at all. A component can consist of a single file, multiple files, registry keys, desktop shortcuts, or some combination thereof. The resources (files, and so on) within a component must be unique to that component-no two components can contain the same resource. A component is never installed explicitly; it is only installed as part of a feature (see following).

### Features

A feature is a group of components, identified by a GUID feature ID. Unlike components, multiple features may contain the same component. A component shared between multiple features will be installed if any of those features is installed, and removed only when all features that reference the component have been uninstalled. Installation of a feature can be done automatically as part of the installation of a product, or it can be done manually using the [**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea) API.

Although few games have multiple "features" that can be installed independently, the Windows Installer concept of a feature is still useful. Since a Windows Installer feature is nothing more than a collection of components that can be installed together, games can use features to group together all of the content needed for a particular stage of the game. For example, a level-oriented game could define one feature per level, consisting of all of the content required for that level. This would allow the game to install the content one level at a time from within the game itself, rather than installing all of the content for all of the levels during the initial installation.

## Install States

Each component or feature has an associated install state, which determines whether the component or feature is available, and if so, where the files for the component or feature are installed. The possible install states for a feature are:

<dl> <dt>

<span id="Absent"></span><span id="absent"></span><span id="ABSENT"></span>Absent
</dt> <dd>

The feature is not installed and is therefore inaccessible.

</dd> <dt>

<span id="Local"></span><span id="local"></span><span id="LOCAL"></span>Local
</dt> <dd>

The feature is available and is installed to run from the local hard drive.

</dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>Source
</dt> <dd>

The feature is available and is installed to run from the original source media (usually a CD or DVD).

</dd> <dt>

<span id="Advertised"></span><span id="advertised"></span><span id="ADVERTISED"></span>Advertised
</dt> <dd>

The feature is not installed, but can be installed on demand using the [**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea) API. When the feature is actually installed, it can be installed either to the Local or Source state.

</dd> </dl>

A component can have any of the above states except for "Advertised." If a component is part of an advertised feature, the component will appear as "Absent" until the feature is installed.

## Install on Demand

Windows Installer allows an application to mark features as Advertised, meaning that the feature is not yet installed, but is available to install at runtime if it is needed. Installing features at runtime is known as "Install on Demand." Games can use Install on Demand to drastically reduce the time required for the initial game setup by deferring the installation of game content until it is needed at runtime. The delay required to install the content at runtime can often be partially or completely hidden by doing the on-demand installation in a background thread, while the user is otherwise occupied with the game.

## Custom User Interface

Although Windows Installer provides a default user interface that guides the user through the installation of the application, this interface looks like that of a standard Windows application. Many game developers prefer that their installation UI have the same look and feel as the game itself, to provide the user with a taste of the game's ambiance. To support this, Windows Installer allows its built-in user interface to be completely disabled, allowing the developer to provide a completely custom UI.

The custom setup program first disables Windows Installer's built-in user interface using the [**MsiSetInternalUI**](/windows/desktop/api/msi/nf-msi-msisetinternalui) API to set the UI level to INSTALLUILEVEL\_NONE. It then calls the [**MsiSetExternalUI**](/windows/desktop/api/msi/nf-msi-msisetexternaluia) API to specify a callback function that will be called during the installation process to notify the setup program of key events during the installation.

The actual installation process is then started by calling the [**MsiInstallProduct**](/windows/desktop/api/msi/nf-msi-msiinstallproducta) API. This API accepts a parameter string that allows the caller to specify values for named properties. These properties can be used within the installation database itself to customize how the application is to be installed. These properties can be used to specify:

-   The directory to which the application is to be installed
-   Which features are to be installed locally and which are to be installed to run from the CD/DVD (for example, to enable choosing between a minimal install and a full install)
-   Whether the application should be installed for all users of the machine, or for only the current user

During the course of the installation, the setup program uses the notification messages sent to its callback function to determine when to update its progress indicator UI, when to prompt the user to insert the next CD, or when to notify the user about an error in the installation process.

## Patching

Windows Installer allows installed applications to be patched by applying a patch file. A patch file contains the new files to be added by the patch, the files that are modified by the patch, and a list of changes to make to the installation database. To conserve space, instead of storing the complete contents of a file changed by the patch, the patch file actually contains only the differences between the original version of the file and the new version of the file.

In order to create a patch, you need the setup image for each of the versions of the application that you wish the patch to upgrade from, as well as the setup image for the new, upgraded version of the application. A setup image consists of the MSI database and all of the actual data files for the application. The best way to create a setup image for a new version of the application is to copy the setup image from the previous version of the application, and then make any changes necessary to update that copy to the patched version.

Once you have all of the necessary setup images, you can create the patches using Msimsp.exe, which is a patch creation tool available as part of the Platform SDK. The tool will ask for the locations of each of the setup images, and then determine how to efficiently represent the differences between the successive versions. The output of the tool is the final patch file (identified by the extension MSP). In order to install the patch programmatically, call the [**MsiApplyPatch**](/windows/desktop/api/msi/nf-msi-msiapplypatcha) API. The user can also install the patch manually by double-clicking on the MSP file in Explorer.

## Other Resources

-   For detailed info on the Windows Installer API, see [Windows Installer](/windows/desktop/Msi/windows-installer-portal).
-   For info on best practices for game installation, see [Installation and Maintenance of Games](/windows/desktop/DxTechArts/installation-and-maintenance-of-games).

 

 