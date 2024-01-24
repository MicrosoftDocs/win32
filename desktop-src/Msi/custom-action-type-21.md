---
description: Developers of Windows Installer packages may choose to use a custom action type 21 when the standard actions are insufficient to execute the installation.
ms.assetid: 0b28ad22-4e3a-49f2-8eed-2341a91eb67c
title: Custom Action Type 21
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 21

This custom action is written in JScript, such as ECMA 262. Windows Installer does not support JScript 1.0. For more information, see [Scripts](scripts.md).

## Source

The script is installed with the application during the current session. The Source field of the [CustomAction table](customaction-table.md) contains a key to the [File table](file-table.md). The location of the custom action code is determined by the resolution of the target path for this file; therefore this custom action must be called after the file has been installed and before it is removed.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of a 32-bit custom action.



| Constants                                                              | Hexadecimal | Decimal |
|------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeJScript** + **msidbCustomActionTypeSourceFile** | 0x015       | 21      |



 

Windows Installer may use [64-bit Custom Actions](64-bit-custom-actions.md) on 64-bit operating systems. A 64-bit custom action based on scripts must include the **msidbCustomActionType64BitScript** bit in its numeric type. For information see 64-bit Custom Actions. Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of a 64-bit custom action.



| Constants                                                                                                     | Hexadecimal | Decimal |
|---------------------------------------------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeJScript** + **msidbCustomActionTypeSourceFile** + **msidbCustomActionType64BitScript** | 0x0001015   | 4117    |



 

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

A custom action that is written in JScript or VBScript requires the installation [**Session**](session-object.md) object. The installer attaches the **Session Object** to the script with the name "Session". Because the **Session** object may not exist during an installation rollback, a deferred custom action written in script must use one of the methods or properties of the **Session** object described in the section [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md) to retrieve its context.

Custom actions that reference an installed file as their source, such as Custom Action Type 21 (JScript), must adhere to the following sequencing restrictions:

-   The custom action must be sequenced after the [CostFinalize action](costfinalize-action.md). This is so that the custom action can resolve the path needed to locate the source file containing the JScript.
-   If the source file is not already installed on the computer, deferred (in-script) custom actions of this type must be sequenced after the [InstallFiles action](installfiles-action.md).
-   If the source file is not already installed on the computer, non-deferred custom actions of this type must be sequenced after the [InstallFinalize action](installfinalize-action.md).

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 



