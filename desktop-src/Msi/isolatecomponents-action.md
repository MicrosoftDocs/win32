---
description: The IsolateComponents action installs a copy of a component (commonly a shared DLL) into a private location for use by a specific application (typically an .exe).
ms.assetid: 3f39ad5d-5539-48cc-8369-bd4d3127fbdd
title: IsolateComponents Action
ms.topic: article
ms.date: 05/31/2018
---

# IsolateComponents Action

The IsolateComponents action installs a copy of a component (commonly a shared DLL) into a private location for use by a specific application (typically an .exe). This isolates the application from other copies of the component that may be installed to a shared location on the computer. For more information, see [Isolated Components](isolated-components.md).

The action refers to each record of the [IsolatedComponent table](isolatedcomponent-table.md) and associates the files of the component listed in the Component\_Shared field with the component listed in the Component\_Application field. The installer installs the files of Component\_Shared into the same directory as Component\_Application. The installer generates a file in this directory, zero bytes in length, having the short filename name of the key file for Component\_Application (typically this is the same file name as the .exe) appended with .local. The IsolatedComponent action does not affect the installation of Component\_Application. Uninstalling Component\_Application also removes the Component\_Shared files and the .local file from the directory.

## Sequence Restrictions

The IsolateComponents action can be used only in the [InstallUISequence table](installuisequence-table.md) and the [InstallExecuteSequence table](installexecutesequence-table.md). This action must come after the [CostInitialize action](costinitialize-action.md) and before the [CostFinalize action](costfinalize-action.md).

## ActionData Messages

There are no ActionData messages.

## Remarks

If the Condition column for the IsolateComponents action evaluates to True, or is left blank, the installer isolates all the components listed in the [IsolatedComponent table](isolatedcomponent-table.md). If the Condition column evaluates to False, the installer ignores the IsolatedComponent table and shares the components usual. The [**RedirectedDllSupport**](redirecteddllsupport.md) property may be used to condition this action. For more information, see [Using a Sequence Table](using-a-sequence-table.md).

 

 



