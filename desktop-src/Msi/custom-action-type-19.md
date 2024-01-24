---
description: Developers of Windows Installer packages may choose to use a custom action type 19 when the standard actions are insufficient to execute the installation.
ms.assetid: c6df5462-e20e-4486-8480-8c747193c5d9
title: Custom Action Type 19
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 19

This custom action displays a specified error message, returns failure, and then terminates the installation. The error message displayed can be supplied as a string or as an index into the [Error table](error-table.md).

## Source

Leave the Source column of the [CustomAction table](customaction-table.md) blank.

## Type Value

Include the following value in the Type column of the CustomAction table to specify the basic numeric type.



| Constants                                                               | Hexadecimal | Decimal |
|-------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeTextData** + **msidbCustomActionTypeSourceFile** | 0x013       | 19      |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains a text string formatted using the functionality specified in [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) (without the numeric field specifiers). Parameters to be replaced are enclosed in square brackets, \[…\], and may be properties, environment variables (% prefix), file paths (\# prefix), or component directory paths ($ prefix). If after formatting the string evaluates to an integer, that integer is used as an index into the [Error table](error-table.md) to retrieve the message to display. If after formatting the string contains non-numeric characters, the string itself is displayed as the message.

## Return Processing Options

The custom action does not use any options.

## Execution Scheduling Options

The custom action does not use any options.

## In-Script Execution Options

The custom action does not use any options.

## Return Values

See [Custom Action Return Values](custom-action-return-values.md).

## Remarks

For example, the custom actions CAError1, CAError2, CAError3, and CAError4 return these messages.

[CustomAction Table](customaction-table.md)



| Action   | Type | Source | Target                              |
|----------|------|--------|-------------------------------------|
| CAError1 | 19   |        | \[Prop1\]                           |
| CAError2 | 19   |        | Installation failure due to Error2. |
| CAError3 | 19   |        | 25000                               |
| CAError4 | 19   |        | \[Prop2\]                           |



 

[Property Table](property-table.md)



| Property | Value                                 |
|----------|---------------------------------------|
| Prop1    | "Installation failure due to Error1." |
| Prop2    | "25100"                               |



 

[Error Table](error-table.md)



| Code  | Message                             |
|-------|-------------------------------------|
| 25000 | Installation failure due to Error3. |
| 25100 | Installation failure due to Error4. |



 

These custom actions return the following error messages:



| Custom action | Returned message string             |
|---------------|-------------------------------------|
| CAError1      | Installation failure due to Error1. |
| CAError2      | Installation failure due to Error2. |
| CAError3      | Installation failure due to Error3. |
| CAError4      | Installation failure due to Error4. |



 

Note that because the order of evaluation of launch conditions cannot be guaranteed by authoring the [LaunchCondition table](launchcondition-table.md), you should use Custom Action Type 19 custom actions in your installation to evaluate conditions in a specific order.

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> </dl>

 

 



