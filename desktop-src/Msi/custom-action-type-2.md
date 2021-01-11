---
description: Developers of Windows Installer packages may choose to use a custom action type 2 when the standard actions are insufficient to execute the installation.
ms.assetid: 79ae0582-c991-4c0a-860b-0f5197ad0c7c
title: Custom Action Type 2
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 2

This custom action calls an executable launched with a command line.

## Source

The executable is generated from a temporary binary stream. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [Binary table](binary-table.md). The Data column in the Binary table contains the stream data. A separate stream is allocated for each row.

New binary data can be inserted from a file by using [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) followed by [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to insert the record into the table. When the custom action is invoked, the stream data is copied to a temporary file, which is then processed depending upon the type of custom action.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                          | Hexadecimal | Decimal |
|--------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeExe** + **msidbCustomActionTypeBinaryData** | 0x002       | 2       |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains the command line string for the executable named in the Source column.

## Return Processing Options

Include optional flag bits in the Type column of the CustomAction table to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the CustomAction table to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the CustomAction table to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

Custom actions that are [executable files](executable-files.md) must return a value of 0 for success. The installer interprets any other return value as failure. To ignore return values, set the **msidbCustomActionTypeContinue** bit flag in the Type field of the CustomAction table.

## Remarks

A custom action that launches an executable takes a command line, which commonly contains properties that are designated dynamically. If this is also a [deferred execution custom action](deferred-execution-custom-actions.md), the installer uses [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) or [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) to create the process when the custom action is invoked from the installation script.

When a database table is exported, each stream is written as a separate file in the subfolder named after the table, using the primary key as the file name (Name column for the Binary table), with a default extension of ".ibd". The name should use the 8.3 format if the file system or version control system does not support long file names. The persistent archive file replaces the stream data with the file name used, so that the data can be located when the table is imported.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Executable Files](executable-files.md)
</dt> </dl>

 

 
