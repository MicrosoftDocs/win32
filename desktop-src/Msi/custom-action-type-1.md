---
description: Developers of Windows Installer packages may choose to use a custom action type 1 when the standard actions are insufficient to execute the installation.
ms.assetid: 277b875f-37f1-4f4d-98ae-7a18131de4f0
title: Custom Action Type 1
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 1

This custom action calls a dynamic link library (DLL) written in C or C++.

## Source

The DLL is generated from a temporary binary stream. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [Binary table](binary-table.md).

The Data column in the Binary table contains the stream data. A separate stream is allocated for each row. New binary data can be inserted from a file by using [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) followed by [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to insert the record into the table. When the custom action is invoked, the stream data is copied to a temporary file, which is then processed depending upon the type of custom action.

## Type Value

Include the following flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                          | Hexadecimal | Decimal |
|--------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeDll** + **msidbCustomActionTypeBinaryData** | 0x001       | 1       |



 

## Target

The DLL is called through the entry point named in the Target field of the [CustomAction table](customaction-table.md), passing a single argument that is the handle to the current install session. The entry point name specified in the table must match that exported from the DLL. Note that if the entry function is not specified by a .DEF file or by a /EXPORT: linker specification, the name may have a leading underscore and a "@4" suffix. The called function must specify the \_\_stdcall calling convention.

## Return Processing Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify return processing options. For a description of the options and the values, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify an in-script execution option. These options copy the action code into the execution, rollback, or commit script. For a description of the options, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

## Return Values

See [Custom Action Return Values](custom-action-return-values.md).

## Remarks

A custom action that calls a dynamic-link library (DLL) requires a handle to the installation session. If this is also a deferred execution custom action, the session may no longer exist during execution of the installation script. For information on how a custom action of this type can obtain context information, see [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

When a database table is exported, each stream is written as a separate file in the subfolder named after the table, using the primary key as the file name (Name column for the Binary table), with a default extension of ".ibd". The name should use the 8.3 format if the file system or version control system does not support long file names. The persistent archive file replaces the stream data with the file name used, so that the data can be located when the table is imported.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Dynamic-Link Libraries](dynamic-link-libraries.md)
</dt> <dt>

[Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md)
</dt> </dl>

 

 



