---
description: Insert the ScheduleReboot action into the action sequence to prompt the user for a restart of the system at the end of the installation. Use the ForceReboot action to prompt for a restart during installation.
ms.assetid: 36f24f57-f1f0-4eca-9b6d-1b25fb73fa96
title: ScheduleReboot Action
ms.topic: article
ms.date: 05/31/2018
---

# ScheduleReboot Action

Insert the ScheduleReboot action into the action sequence to prompt the user for a restart of the system at the end of the installation. Use the [ForceReboot action](forcereboot-action.md) to prompt for a restart during installation.

If the installation has a user interface, the installer displays a message box and button at the end of installation asking whether the user wants to restart the system. The user must respond to this prompt before completing installation. If the installation has no user interface, the system automatically restarts at the end.

If the installer determines that a restart is necessary it automatically prompts the user to restart at the end of the installation, whether or not there are any ForceReboot or ScheduleReboot actions in the sequence. For example, the installer automatically prompts for a restart if it needs to replace any files that are in use during installation.

You can suppress certain prompts for restarts by setting the [**REBOOT**](reboot.md) property.

If the Windows Installer encounters the [ForceReboot](forcereboot-action.md) or ScheduleReboot action during a [multiple-package installation](multiple-package-installations.md), the installer will stop and roll back the installation. Other packages belonging to the multiple-package installation, that do not contain a ForceReboot or ScheduleReboot action, can be installed.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages

There are no ActionData messages.

## Remarks

For example, this action can be used to force the installer to prompt for a restart after installing drivers that require a restart. If the installer attempts to replace files that are in use, it automatically prompts the user to restart even if ScheduleReboot has not been used.

The ScheduleReboot action is typically placed at the end of the sequence, but it can be inserted at any point in the sequence.

## Related topics

<dl> <dt>

[System Reboots](system-reboots.md)
</dt> </dl>

 

 



