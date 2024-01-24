---
description: Use the following option flags to specify that the installer not write the value entered into the Target field of the CustomAction table into the log. To set the option add the value in this table to the value in the Type field of the CustomAction table.
ms.assetid: b0f99851-a774-4804-8c85-f94943c2d2b0
title: Custom Action Hidden Target Option
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Hidden Target Option

Use the following option flags to specify that the installer not write the value entered into the Target field of the [CustomAction table](customaction-table.md) into the log. To set the option add the value in this table to the value in the Type field of the CustomAction table.



| Constant                            | Hexadecimal | Decimal | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------|-------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (none)                              | 0x0000      | 0       | The installer may write the value in the Target column of the CustomAction table into the log file.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **msidbCustomActionTypeHideTarget** | 0x2000      | 8192    | The installer is prevented from writing the value in the Target column of the [CustomAction table](customaction-table.md) into the log file. The CustomActionData property is also not logged when the installer executes the custom action.<br/> Because the installer sets the value of CustomActionData from a property with the same name as the custom action, that property must be listed in the [**MsiHiddenProperties**](msihiddenproperties.md) Property to prevent its value from appearing in the log.<br/> |



 

For more information, see [Preventing Confidential Information from Being Written into the Log File](preventing-confidential-information-from-being-written-into-the-log-file.md)

## Related topics

<dl> <dt>

[Custom Action Reference](custom-action-reference.md)
</dt> <dt>

[About Custom Actions](about-custom-actions.md)
</dt> <dt>

[Using Custom Actions](using-custom-actions.md)
</dt> </dl>

 

 




