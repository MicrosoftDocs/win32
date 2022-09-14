---
description: Developers of Windows Installer packages may choose to use a custom action type 23 when the standard actions are insufficient to execute the installation.
ms.assetid: 8219f157-585d-4733-8e10-c05813b398ba
title: Custom Action Type 23
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Type 23

The Custom Action Type 23 is used with concurrent installations. Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see [Concurrent Installations](concurrent-installations.md).

This custom action installs another installer package that resides in the application's source tree.

## Source

The location of the concurrent installation package is specified relative to the root of the source location shown in the Source field of the [CustomAction table](customaction-table.md).

## Numeric Type



| Type name                                                      | Value |
|----------------------------------------------------------------|-------|
| msidbCustomActionTypeInstall + msidbCustomActionTypeSourceFile | 23    |



 

## Target

The Target field of the [CustomAction table](customaction-table.md) contains property settings that are to be passed to the concurrent installation. These property settings can specify features.

## Return Processing Options

The concurrent installation session runs as a separate thread in the current process. A concurrent installation cannot run asynchronously.

For more information, see [Custom Action Return Processing Options](custom-action-return-processing-options.md).

## Execution Scheduling Options

Options flags are available to control the potential multiple execution of custom actions. For more information, see [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md).

## In-Script Execution Options

Not used.

## Return Values

The return status of user exit, failure, suspend, or success from a concurrent installation is processed in the same way as any other action. Note however, that Windows Installer translates the return values from all actions when it writes the return value into the log file. For example, if the action return value appears as 1 in the log file, this means that the action returned ERROR\_SUCCESS. For more information, see [Logging of Action Return Values](logging-of-action-return-values.md).

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
</dt> <dt>

[Custom Action Return Values](custom-action-return-values.md)
</dt> </dl>

 

 



