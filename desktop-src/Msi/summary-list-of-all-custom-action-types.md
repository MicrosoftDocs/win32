---
description: The following table identifies the basic types of custom actions and shows the values that are in the Type, Source, and Target fields of the CustomAction table for each type.
ms.assetid: 8713451e-c0e7-4bec-bfb6-dfe4125d5a44
title: Custom Action Types
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Types

The following table identifies the basic types of custom actions and shows the values that are in the Type, Source, and Target fields of the [CustomAction](customaction-table.md) table for each type. The basic custom actions can be modified by including optional flag bits in the Type column. For descriptions of the options and the values, see the following:

-   [Custom Action Return Processing Options](custom-action-return-processing-options.md)
-   [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md)
-   [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md)
-   [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md)

Use the links to the Basic Custom Action Type for a description and the options available for each type.



| Basic custom action type                                                                                                                           | Type | Source                                                                                                                              | Target                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Custom Action Type 1](custom-action-type-1.md)DLL file stored in a Binary table stream.<br/>                                               | 1    | Key to [Binary](binary-table.md) table.                                                                                            | DLL entry point.                                                                                                                           |
| [Custom Action Type 2](custom-action-type-2.md)EXE file stored in a Binary table stream.<br/>                                               | 2    | Key to [Binary](binary-table.md) table.                                                                                            | Command-line string.                                                                                                                       |
| [Custom Action Type 5](custom-action-type-5.md)JScript file stored in a Binary table stream.<br/>                                           | 5    | Key to [Binary](binary-table.md) table.                                                                                            | An optional JScript function that can be called.                                                                                           |
| [Custom Action Type 6](custom-action-type-6.md)VBScript file stored in a Binary table stream.<br/>                                          | 6    | Key to [Binary](binary-table.md) table.                                                                                            | An optional VBScript function that can be called.                                                                                          |
| [Custom Action Type 17](custom-action-type-17.md)DLL file that is installed with a product.<br/>                                            | 17   | Key to [File](file-table.md) table.                                                                                                | DLL entry point.                                                                                                                           |
| [Custom Action Type 18](custom-action-type-18.md)EXE file that is installed with a product.<br/>                                            | 18   | Key to [File](file-table.md) table.                                                                                                | Command-line string.                                                                                                                       |
| [Custom Action Type 19](custom-action-type-19.md)Displays a specified error message and returns failure, terminating the installation.<br/> | 19   | Blank                                                                                                                               | [Formatted](formatted.md) text string. The literal message or an index into the [Error](error-table.md) table.                           |
| [Custom Action Type 21](custom-action-type-21.md)JScript file that is installed with a product.<br/>                                        | 21   | Key to [File](file-table.md) table.                                                                                                | An optional JScript function that can be called.                                                                                           |
| [Custom Action Type 22](custom-action-type-22.md)VBScript file that is installed with a product.<br/>                                       | 22   | Key to [File](file-table.md) table.                                                                                                | An optional VBScript function that can be called.                                                                                          |
| [Custom Action Type 34](custom-action-type-34.md)EXE file having a path referencing a directory.<br/>                                       | 34   | Key to [Directory](directory-table.md) table. This is the working directory for execution.                                         | The Target column is [formatted](formatted.md) and contains the full path and name of the executable file followed by optional arguments. |
| [Custom Action Type 35](custom-action-type-35.md)Directory set with formatted text.<br/>                                                    | 35   | A key to the [Directory](directory-table.md) table. The designated directory is set by the formatted string in the Target field.   | A formatted text string.                                                                                                                   |
| [Custom Action Type 37](custom-action-type-37.md)JScript text stored in this sequence table.<br/>                                           | 37   | Null                                                                                                                                | A string of JScript code.                                                                                                                  |
| [Custom Action Type 38](custom-action-type-38.md)VBScript text stored in this sequence table.<br/>                                          | 38   | Null                                                                                                                                | A string of VBScript code.                                                                                                                 |
| [Custom Action Type 50](custom-action-type-50.md)EXE file having a path specified by a property value.<br/>                                 | 50   | Property name or key to [Property](property-table.md) table.                                                                       | Command-line string.                                                                                                                       |
| [Custom Action Type 51](custom-action-type-51.md)Property set with formatted text.<br/>                                                     | 51   | Property name or key to the [Property](property-table.md) table. This property is set by the formatted string in the Target field. | A formatted text string.                                                                                                                   |
| [Custom Action Type 53](custom-action-type-53.md)JScript text specified by a property value.<br/>                                           | 53   | Property name or key to [Property](property-table.md) table.                                                                       | An optional JScript function that can be called.                                                                                           |
| [Custom Action Type 54](custom-action-type-54.md)VBScript text specified by a property value.<br/>                                          | 54   | Property name or key to [Property](property-table.md) table.                                                                       | An optional VBScript function that can be called.                                                                                          |



 

In addition, the following custom action types are used with concurrent installations:

-   [Custom Action Type 7](custom-action-type-7.md)
-   [Custom Action Type 23](custom-action-type-23.md)
-   [Custom Action Type 39](custom-action-type-39.md)

 

 




