---
description: Developers of Windows Installer packages may choose to use a custom action type 18 when the standard actions are insufficient to execute the installation.
ms.assetid: 8a7311a6-41c6-431e-982d-60bacf06454e
title: Custom Action Type 18
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 18

This custom action calls an executable launched with a command line.

## Source

The executable is generated from a file installed with the application. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [File table](file-table.md). The location of the custom action code is determined by the resolution of the target path for this file; therefore this custom action must be called after the file has been installed and before it is removed.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                          | Hexadecimal | Decimal |
|--------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeExe** + **msidbCustomActionTypeSourceFile** | 0x012       | 18      |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains the command line string for the executable identified in the Source column.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

Custom actions that are [executable files](executable-files.md) must return a value of 0 for success. The installer interprets any other return value as failure. To ignore return values, set the **msidbCustomActionTypeContinue** bit flag in the Type field of the CustomAction table.

## Remarks

A custom action that launches an executable takes a command line, which commonly contains properties that are designated dynamically. If this is also a [deferred execution custom action](deferred-execution-custom-actions.md), the installer uses [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) or [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) to create the process when the custom action is invoked from the installation script.

Custom actions that reference an installed file as their source, such as Custom Action Type 18 (EXE), must adhere to the following sequencing restrictions:

-   The custom action must be sequenced after the [CostFinalize action](costfinalize-action.md). This is so that the custom action can resolve the path needed to locate the EXE.
-   If the source file is not already installed on the computer, deferred (in-script) custom actions of this type must be sequenced after the [InstallFiles action](installfiles-action.md).
-   If the source file is not already installed on the computer, non-deferred custom actions of this type must be sequenced after the [InstallFinalize action](installfinalize-action.md).

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Executable Files](executable-files.md)
</dt> </dl>

 

 
