---
description: If possible, the best way to specify the target location for a directory is to author the Directory Table in your installation package to provide the correct location. For more information, see Using the Directory Table.
ms.assetid: 2d16e036-2d7f-431d-b646-1addf2f65f3f
title: Changing the Target Location for a Directory
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Target Location for a Directory

If possible, the best way to specify the target location for a directory is to author the [Directory Table](directory-table.md) in your installation package to provide the correct location. For more information, see [Using the Directory Table](using-the-directory-table.md).

If you need to change the directory location at the time of the installation, you have the following options:

-   Specify the location of a directory by setting the value of a [Public Property](public-properties.md) on the command line. During the [CostFinalize Action](costfinalize-action.md), the internal directory paths used by the installer are updated to the value of properties listed as keys in the [Directory Table](directory-table.md). For more information, see [Using Properties](using-properties.md) and [Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md).
-   Specify the location of a directory by using a custom action. If the custom action is to run before the [CostFinalize Action](costfinalize-action.md), you can use a [Custom Action Type 51](custom-action-type-51.md) to set the value of a property from a formatted text string. If the custom action runs after the [CostFinalize Action](costfinalize-action.md), you can use a [Custom Action Type 35](custom-action-type-35.md) to set the value of the directory path from a formatted text string. Custom actions that change one of the [System Folder Properties](property-reference.md) should be included in both the execution sequence tables ([InstallExecuteSequence Table](installexecutesequence-table.md) or [AdminExecuteSequence Table](adminexecutesequence-table.md)), and the user interface sequence tables ([InstallUISequence Table](installuisequence-table.md) and [AdminUISequence Table](adminuisequence-table.md)) so that the folder is changed during both [*full UI*](f-gly.md) and [*basic UI*](b-gly.md) installations.
-   If the installation is running a [*full UI*](f-gly.md), you can use [**MsiSetTargetPath**](/windows/desktop/api/Msiquery/nf-msiquery-msisettargetpatha) or the [SetTargetPath ControlEvent](settargetpath-controlevent.md) to set the directory path. Check the [**ProductState**](productstate.md) Property to determine whether the product that contains this component is already installed before calling **MsiSetTargetPath** or the SetTargetPath ControlEvent. Do not attempt to change the target directory path if some components that use that path are already installed for the current user or a different user.

The following restrictions apply to all of the above options:

-   Do not attempt to change the target directory path if some components that use the path are already installed for the current user or for a different user.
-   Do not attempt to change the target directory path during a [Maintenance Installation](maintenance-installation.md).

 

 



