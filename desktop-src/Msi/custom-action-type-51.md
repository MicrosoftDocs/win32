---
description: Developers of Windows Installer packages may choose to use a custom action type 51 when the standard actions are insufficient to execute the installation.
ms.assetid: cdad16ad-426c-4e04-8003-b32c67be7329
title: Custom Action Type 51
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 51

This custom action sets a property from a formatted text string.

To affect a property used in a condition on a component or feature, the custom action must come before the [CostFinalize action](costfinalize-action.md) in the action sequence.

## Source

The Source field of the [CustomAction table](customaction-table.md) can contain either the name of a property or a key to the [Property table](property-table.md). This property is set by the formatted string in the Target field using [**MsiSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisetpropertya).

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                             | Hexadecimal | Decimal |
|-----------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeTextData** + **msidbCustomActionTypeProperty** | 0x033       | 51      |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains a text string formatted using the functionality specified in [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) (without the numeric field specifiers). Parameters to be replaced are enclosed in square brackets, \[…\], and may be properties, environment variables (% prefix), file paths (\# prefix), or component directory paths ($ prefix).

## Return Processing Options

The custom action does not use these options.

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

The custom action does not use these options.

## Return Values

See [Custom Action Return Values](custom-action-return-values.md).

## Remarks

If you set a [private property](private-properties.md) in the UI sequence by authoring a custom action in one of the user interface sequence tables, that property is not set in the execution sequence. To set the property in the execution sequence, you must also put a custom action in an execution sequence table. Alternatively, you can make the property a [public property](public-properties.md) and include it in the [**SecureCustomProperties property**](securecustomproperties.md).

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Formatted Text Custom Actions](formatted-text-custom-actions.md)
</dt> </dl>

 

 



