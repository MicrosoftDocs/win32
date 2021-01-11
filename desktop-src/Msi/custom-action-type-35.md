---
description: Developers of Windows Installer packages may choose to use a custom action type 35 when the standard actions are insufficient to execute the installation.
ms.assetid: b88b5f48-5353-4876-9dda-2eeda288fa4b
title: Custom Action Type 35
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 35

This custom action sets the install directory from a formatted text string. For more information, see [Changing the Target Location for a Directory](changing-the-target-location-for-a-directory.md)

## Source

The Source field of the [CustomAction table](customaction-table.md) contains a key to the [Directory table](directory-table.md). The designated directory is set by the formatted string in the Target field using [**MsiSetTargetPath**](/windows/desktop/api/Msiquery/nf-msiquery-msisettargetpatha). This sets the target path and associated property to the expanded value of the formatted text string in the Target field. Do not attempt to change the location of a target directory during a [maintenance installation](maintenance-installation.md). Do not attempt to change the target directory path if some components using that path are already installed for any user.

## Type Value

Include the following value in the Type column of the [CustomAction table](customaction-table.md) to specify the basic numeric type.



| Constants                                                              | Hexadecimal | Decimal |
|------------------------------------------------------------------------|-------------|---------|
| **msidbCustomActionTypeTextData** + **msidbCustomActionTypeDirectory** | 0x023       | 35      |



 

## Target

The Target column of the [CustomAction table](customaction-table.md) contains a text string formatted using the functionality specified in [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) (without the numeric field specifiers). Parameters to be replaced are enclosed in square brackets \[…\], and may be properties, environment variables (% prefix), file paths (\# prefix), or component directory paths ($ prefix). Note that directory paths always end with a directory separator.

## Return Processing Options

The custom action does not use these options.

## Execution Scheduling Options

Include optional flag bits in the Type column of the [CustomAction table](customaction-table.md) to specify execution scheduling options. These options control the multiple execution of custom actions. For a description of the options, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

The custom action does not use these options.

## Return Values

See [Custom Action Return Values](custom-action-return-values.md).

## Remarks

If you set a [private property](private-properties.md) in the UI sequence by authoring a custom action in one of the user interface sequence tables, that property is not set in the execution sequence. To set the property in the execution sequence you must also put a custom action in an execution sequence table. Alternatively, you can make the property a [public property](public-properties.md) and include it in the [**SecureCustomProperties property**](securecustomproperties.md).

## Related topics

<dl> <dt>

[Custom\_Actions](custom-actions.md)
</dt> <dt>

[Formatted Text Custom Actions](formatted-text-custom-actions.md)
</dt> </dl>

 

 



