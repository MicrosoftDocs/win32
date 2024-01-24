---
description: Developers of Windows Installer packages may choose to use a custom action type 39 when the standard actions are insufficient to execute the installation.
ms.assetid: edf96cc6-ef32-4660-b4ee-50c130626e15
title: Custom Action Type 39
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 39

The Custom Action Type 39 is used with concurrent installations. Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see [Concurrent Installations](concurrent-installations.md).

Type 39 custom action installs an application that is advertised or already installed. This custom action type may be used to reinstall or remove a product that has been installed as a concurrent installation by the current product's installation package. The Type 39 custom action cannot be used to reinstall or remove any product previously installed by any other means. For example, if the secondary product is installed using a Type 39, Type 23, or Type 7 custom action during the installation of the primary product, a Type 39 custom action may be used to remove the secondary product when the primary product is uninstalled.

## Source

The Source field of the [CustomAction table](customaction-table.md) contains the product code for the application.

## Numeric Type



| Type name                                                     | Value |
|---------------------------------------------------------------|-------|
| msidbCustomActionTypeInstall + msidbCustomActionTypeDirectory | 39    |



 

## Target

The Target field of the [CustomAction table](customaction-table.md) contains property settings that are to be passed to the concurrent installation. These property settings can specify features.

## Return Processing Options

The custom action type 39 fails if the application is not advertised or installed. To avoid this failure, you must set the **msidbCustomActionTypeContinueflag**.

A concurrent install cannot run asynchronously.

See [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Options flags are available to control the potential multiple execution of custom actions. See [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

The custom action does not use this option.

## Return Values

The return status of user exit, failure, suspend, or success from a concurrent installation is processed in the same way as any other action. Note however that Windows Installer translates the return values from all actions when it writes the return value into the log file. For example, if the action return value appears as 1 in the log file, this means that the action returned ERROR\_SUCCESS. For more information, see [Logging of Action Return Values](logging-of-action-return-values.md).

Note that if a concurrent installation has **msidbCustomActionTypeContinue** set, then a return of ERROR\_INSTALL\_USEREXIT, ERROR\_INSTALL\_REBOOT, ERROR\_INSTALL\_REBOOT\_NOW, or ERROR\_SUCCESS\_REBOOT\_REQUIRED is treated as ERROR\_SUCCESS. This means that if you set **msidbCustomActionTypeContinue** and your concurrent installation requires a restart, the requirement for the restart will be ignored. Additionally, the error code from the concurrent installation custom action will be ignored.

If **msidbCustomActionTypeContinue** is not set, the following return codes plus ERROR\_SUCCESS are treated as success and have the following meanings. Other return codes are treated as failure.



| Message                          | Meaning                                                                                              |
|----------------------------------|------------------------------------------------------------------------------------------------------|
| ERROR\_INSTALL\_REBOOT           | The restart flag will be set to restart at end of the installation.                                  |
| ERROR\_INSTALL\_REBOOT\_NOW      | A restart is required before completing the installation. The restart will be processed immediately. |
| ERROR\_SUCCESS\_REBOOT\_REQUIRED | A restart was required, but was suppressed.                                                          |



 

## Remarks

A conditional expression is required to enable the concurrent installation at either installation or removal of the associated component or feature.

## Related topics

<dl> <dt>

[Concurrent Installations](concurrent-installations.md)
</dt> <dt>

[Custom Action Reference](custom-action-reference.md)
</dt> <dt>

[About Custom Actions](about-custom-actions.md)
</dt> <dt>

[Using Custom Actions](using-custom-actions.md)
</dt> </dl>

 

 



