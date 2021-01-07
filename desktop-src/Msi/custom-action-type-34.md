---
description: Developers of Windows Installer packages may choose to use a custom action type 34 when the standard actions are insufficient to execute the installation.
ms.assetid: 4d0e4f01-0530-4202-bc78-b6e52670b8e5
title: Custom Action Type 34
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 34

This custom action calls an executable launched with a command line. For more information, see [Executable Files](executable-files.md).

## Source

The executable is generated from a file. The Source field of the [CustomAction](customaction-table.md) table contains a key into the [Directory](directory-table.md) table. The referenced Directory table entry is used to resolve the full path to a working directory. This is not required to be the path to the directory containing the executable.

## Type Value

Include the following value in the Type column of the [CustomAction](customaction-table.md) table to specify the basic numeric type.



| Constants                                                         | Hexadecimal | Decimal |
|-------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeExe** + **msidbCustomActionTypeDirectory** | 0x022       | 34      |



 

## Target

The Target column of the [CustomAction](customaction-table.md) table contains the full path and name of the executable file followed by optional arguments to the executable. The full path and name to the executable file is required. Quotation marks must be used around long file names or paths. The value is treated as [formatted](formatted.md) text and may contain references to properties, files, directories, or other formatted text attributes.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction](customaction-table.md) table to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction](customaction-table.md) table to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction](customaction-table.md) table to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

Custom actions that are [executable files](executable-files.md) must return a value of 0 for success. The installer interprets any other return value as failure. To ignore return values set the **msidbCustomActionTypeContinue** bit flag in the Type field of the [CustomAction](customaction-table.md) table.

## Remarks

A custom action that launches an executable takes a command line, which commonly contains properties that are designated dynamically. If this is also a [deferred execution custom action](deferred-execution-custom-actions.md), the installer uses [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) or [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) to create the process when the custom action is invoked from the installation script.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 
