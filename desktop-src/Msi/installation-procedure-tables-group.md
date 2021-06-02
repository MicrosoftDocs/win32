---
description: The tables in the Installation Procedure group control tasks performed during the installation by standard actions and custom actions.
ms.assetid: dff7cf4a-89a2-47b0-9038-93b79c0d915a
title: Installation Procedure Tables Group
ms.topic: article
ms.date: 05/31/2018
---

# Installation Procedure Tables Group

The tables in the Installation Procedure group control tasks performed during the installation by [standard actions](standard-actions.md) and [custom actions](custom-actions.md).

Some of the tables in this group control a high level action by providing a sequence of actions. Each of the following sequence tables controls a portion of a high level action.

-   [InstallUISequence table](installuisequence-table.md)
-   [InstallExecuteSequence table](installexecutesequence-table.md)
-   [AdminUISequence table](adminuisequence-table.md)
-   [AdminExecuteSequence table](adminexecutesequence-table.md)
-   [AdvtUISequence table](advtuisequence-table.md)
-   [AdvtExecuteSequence table](advtexecutesequence-table.md)

There may be situations in which an installation needs to do something that is not possible using only [standard actions](standard-actions.md). To provide the greatest degree of flexibility, the installer provides setup authors the ability to create their own custom actions. If you have any custom actions, you should register them with the installer by populating the CustomAction Table.

The [CustomAction table](customaction-table.md) provides the means of integrating custom code and data into the installation process. The code that is executed can be a stream contained within the database, a recently installed file, or an existing executable.

The following tables extend the installer's capabilities to manipulate files and folders during the installation.

-   The [RemoveFile table](removefile-table.md) contains a list of files that are removed during the installation.
-   The [RemoveIniFile table](removeinifile-table.md) contains the information an application needs to remove from .ini files.
-   The [RemoveRegistry table](removeregistry-table.md) contains the information which is deleted from the system registry when the corresponding component is selected to be installed.
-   The [CreateFolder table](createfolder-table.md) lists the folders that must be created during the installation. Although the installer creates folders as they are needed, these are removed as soon as they are empty. Folders list in the CreateFolder table are not deleted until the component is uninstalled.
-   The [MoveFile table](movefile-table.md) contains a list of files to be moved or copied from a specified source directory on the user's computer to a destination directory. It is not necessary to use the MoveFile table to describe the files associated with the components you are installing.

To set up necessary conditions that must be met to initiate the installation, populate the LaunchCondition table.

The [LaunchCondition table](launchcondition-table.md) contains a list of conditions, all of which must be satisfied for the action to succeed.

 

 



