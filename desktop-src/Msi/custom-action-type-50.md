---
description: Developers of Windows Installer packages may choose to use a custom action type 50 when the standard actions are insufficient to execute the installation.
ms.assetid: fc8a875d-21e3-452a-8455-80835b52b256
title: Custom Action Type 50
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 50

This custom action calls an executable launched with a command line.

See also [Executable Files](executable-files.md).

## Source

The executable is generated from an existing file. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [Property table](property-table.md) for a property that contains the full path to the executable file.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                        | Hexadecimal | Decimal |
|------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeExe** + **msidbCustomActionTypeProperty** | 0x032       | 50      |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains the command line string for the executable identified in the Source column.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

Custom actions that are [executable files](executable-files.md) must return a value of 0 for success. The installer interprets any other return value as failure. To ignore return values set the **msidbCustomActionTypeContinue** bit flag in the Type field of the CustomAction table.

## Remarks

A custom action that launches an executable takes a command line, which commonly contains properties that are designated dynamically. If this is also a [deferred execution custom action](deferred-execution-custom-actions.md), the installer uses CreateProcessAsUser or CreateProcess to create the process when the custom action is invoked from the installation script.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 



