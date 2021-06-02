---
description: If the msidbCustomActionTypeContinue return processing option is not set, the custom action must return an integer status code as shown in the following table.
ms.assetid: 56c2d639-eef8-47cd-9d47-9a4781b9be36
title: Custom Action Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Return Values

If the **msidbCustomActionTypeContinue** return processing option is not set, the custom action must return an integer status code as shown in the following table.



| Return value                 | Description                           |
|------------------------------|---------------------------------------|
| ERROR\_FUNCTION\_NOT\_CALLED | Action not executed.                  |
| ERROR\_SUCCESS               | Completed actions successfully.       |
| ERROR\_INSTALL\_USEREXIT     | User terminated prematurely.          |
| ERROR\_INSTALL\_FAILURE      | Unrecoverable error occurred.         |
| ERROR\_NO\_MORE\_ITEMS       | Skip remaining actions, not an error. |



 

Note that custom actions that are [executable files](executable-files.md) must return a value of 0 for success. The installer interprets any other return value as failure. To ignore return values, set the **msidbCustomActionTypeContinue** bit flag in the Type field of the [CustomAction table](customaction-table.md).

For more information about the **msidbCustomActionTypeContinue** option and other return processing options, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

Note that Windows Installer translates the return values from all actions when it writes the return value into the log file. For example, if the action return value appears as 1 in the log file, this means that the action returned ERROR\_SUCCESS. For more information about this translation see [Logging of Action Return Values](logging-of-action-return-values.md).

## Related topics

<dl> <dt>

[Error Codes](error-codes.md)
</dt> <dt>

[Logging of Action Return Values](logging-of-action-return-values.md)
</dt> </dl>

 

 



