---
description: Developers of Windows Installer packages may choose to use a custom action type 54 when the standard actions are insufficient to execute the installation.
ms.assetid: ab348a8e-f5df-4e03-a1b7-1ab1a7fbcb3b
title: Custom Action Type 54
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 54

This custom action is written in VBScript. See also [Scripts](scripts.md).

## Source

The Source field of the [CustomAction table](customaction-table.md) contains a property name or a key to the [Property table](property-table.md) for a property containing the script text.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of a 32-bit custom action.



| Constants                                                             | Hexadecimal | Decimal |
|-----------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeVBScript** + **msidbCustomActionTypeProperty** | 0x036       | 54      |



 

Windows Installer may use 64-bit custom actions on 64-bit operating systems. A 64-bit custom action based on scripts must include the **msidbCustomActionType64BitScript** bit in its numeric type. For information see [64-bit Custom Actions](64-bit-custom-actions.md). Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type of a 64-bit custom action.



| Constants                                                                                                    | Hexadecimal | Decimal |
|--------------------------------------------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeVBScript** + **msidbCustomActionTypeProperty** + **msidbCustomActionType64BitScript** | 0x0001036   | 4150    |



 

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

A custom action that is written in JScript or VBScript requires the install [**Session**](session-object.md) object. The installer attaches the **Session Object** to the script with the name *Session*. Because the **Session** object may not exist during an installation rollback, a deferred custom action written in script must use one of the methods or properties of the **Session** object described in the section [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md) to retrieve its context.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 



