---
description: A custom action can call functions that are written in VBScript or JScript.
ms.assetid: d859713f-b8b8-4eb0-b678-52b5d880bd20
title: Scripts
ms.topic: article
ms.date: 05/31/2018
---

# Scripts

A custom action can call functions that are written in VBScript or JScript. Windows Installer does not provide the script engine. Authors wishing to make use of a scripting language during installation must therefore ensure that the appropriate scripting engine is available.

The installer does not support JScript version 1.0.

A 64-bit custom action based on scripts must be explicitly marked as a 64-bit custom action by adding the **msidbCustomActionType64BitScript** bit to the custom actions numeric type in the Type column of the [CustomAction](customaction-table.md) table. For information see [64-Bit Custom Actions](64-bit-custom-actions.md).

The following basic custom action types call functions written in script.



| Custom action type                                 | Description                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Custom Action Type 5](custom-action-type-5.md)   | JScript file stored in a Binary table stream.                                                  |
| [Custom Action Type 21](custom-action-type-21.md) | JScript file that is installed with a product.                                                 |
| [Custom Action Type 53](custom-action-type-53.md) | JScript text specified by a property value.                                                    |
| [Custom Action Type 37](custom-action-type-37.md) | JScript text stored in the Target column of the [CustomAction](customaction-table.md) table.  |
| [Custom Action Type 6](custom-action-type-6.md)   | VBScript file stored in a [Binary](binary-table.md) table stream.                             |
| [Custom Action Type 22](custom-action-type-22.md) | VBScript file that is installed with a product.                                                |
| [Custom Action Type 54](custom-action-type-54.md) | VBScript text specified by a property value.                                                   |
| [Custom Action Type 38](custom-action-type-38.md) | VBScript text stored in the Target column of the [CustomAction](customaction-table.md) table. |



 

> [!Note]  
> The installer runs script custom actions directly and does not use the Windows Script Host. The **WScript** object cannot be used inside a script custom action because this object is provided by the Windows Script Host. Objects in the Windows Script Host object model can only be used in custom actions if Windows Script Host is installed on the computer by creating new instances of the object, with a call to CreateObject, and providing the ProgId of the object (for example "WScript.Shell"). Depending on the type of script custom action, access to some objects and methods of the Windows Script Host object model may be denied for security reasons.

 

For more information, see [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md) for a summary of all types of custom actions and how they are encoded into the [CustomAction](customaction-table.md) table.

 

 



