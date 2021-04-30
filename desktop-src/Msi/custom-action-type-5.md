---
description: Developers of Windows Installer packages may choose to use a custom action type 5 when the standard actions are insufficient to execute the installation.
ms.assetid: 32b10271-44b1-4c5d-9c8b-eed1b4cd31e2
title: Custom Action Type 5
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 5

This custom action is written in JScript, such as ECMA 262. Windows Installer does not support JScript 1.0. For more information, see [Scripts](scripts.md).

## Source

The script is generated from a temporary binary stream. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [Binary table](binary-table.md). The Data column in the Binary table contains the stream data. A separate stream is allocated for each row.

New binary data can be inserted from a file by using [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) followed by [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to insert the record into the table. When the custom action is invoked, the stream data is copied to a temporary file, which is then processed according to the type of custom action.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of 32-bit custom action.



| Constants                                                              | Hexadecimal | Decimal |
|------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeJScript** + **msidbCustomActionTypeBinaryData** | 0x05        | 5       |



 

Windows Installer may use 64-bit custom actions on 64-bit operating systems. A 64-bit custom action based on scripts must include the **msidbCustomActionType64BitScript** bit in its numeric type. For information see [64-bit Custom Actions](64-bit-custom-actions.md). Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of a 64-bit custom action.



| Constants                                                                                                     | Hexadecimal | Decimal |
|---------------------------------------------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeJScript** + **msidbCustomActionTypeBinaryData** + **msidbCustomActionType64BitScript** | 0x0001005   | 4101    |



 

## Target

The Target field of the [CustomAction table](customaction-table.md) contains an optional script function. Processing first sends the script for parsing and then calls the optional script function.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

Optional functions written in script must return one of the values described in [Return Values of JScript and VBScript Custom Actions](return-values-of-jscript-and-vbscript-custom-actions.md).

## Remarks

A custom action that is written in JScript or VBScript requires the installation of [**Session Object**](session-object.md). The installer attaches the **Session** object to the script with the name *Session*. Because the **Session** object may not exist during an installation rollback, a deferred custom action written in script must use one of the methods or properties of the **Session** object described in the section [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md) to retrieve its context.

When a database table is exported, each stream is written as a separate file in the subfolder named after the table, using the primary key as the file name (Name column for the Binary table), with a default extension of ".ibd". The name should use the 8.3 file name format if the file system or version control system does not support long file names. The persistent archive file replaces the stream data with the file name used, so that the data can be located when the table is imported.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 



