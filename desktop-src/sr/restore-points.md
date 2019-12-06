---
title: Restore Points
description: Restore points are created to allow users a choice of previous system states. Each restore point contains the necessary information needed to restore the system to the chosen state. Restore points are created before key changes are made to the system.
ms.assetid: 5f68b377-4293-493e-afaf-f4414c2af1fb
ms.topic: article
ms.date: 12/06/2019
manager: dcscontentpm
ms.custom: CSSTroubleshooting
---

# Restore Points

Restore points are created to allow users a choice of previous system states. Each restore point contains the necessary information needed to restore the system to the chosen state. Restore points are created before key changes are made to the system.

System Restore has an automatic restore point space-management feature that purges the oldest restore points to make room for new ones, while still enabling the user to recover from any recent destructive changes.

In Windows 7 on computers with hard drives over 64 GB, System Restore can take up to 5 percent of the disk or a maximum of 10 GB of the disk space, whichever is less. On computers with hard drives of 64 GB or less, System Restore can take at most 3 percent of the disk space.

In Windows Vista, System Restore can take up to 15 percent of the size of the volume or a maximum of 30 percent of the free disk space, whichever is less.

System Restore in Windows XP takes a maximum of 12 percent of the disk space in systems with hard drives over 4 gigabytes (GB), and a maximum of 400 megabytes (MB) for hard drives under 4 GB. To change the maximum storage limit in Windows XP, use the System application in the Control Panel.

The following describes the triggers that cause System Restore to create a restore point.

## Event-triggered restore points

System Restore automatically creates a restore point before the following events:

-   Application installation (provided the application utilizes an installer that is System Restore compliant). If the application install causes system problems, the user can restore the system to a state before the installation of the application.
-   AutoUpdate installation. AutoUpdate provides an easy way for users to download critical Windows updates. After the update is downloaded, the user can install the update on the system. If the user chooses to install the update, System Restore creates a restore point before the installation of the update begins.
-   System restore. For example, if a user accidentally chooses the wrong restore point, the user can undo the restore operation by choosing a restore point before the system restore took place. The user can then choose the correct restore point.

## Scheduled restore points

System Restore can be configured to create restore points at regular intervals. Users can also manually create and name a restore point at any time from within the System Restore user interface. These restore points are saved and compressed, and these choices are available to the user through the System Restore user interface. System Restore in Windows 7 creates a scheduled restore point only if no other restore points have been created in the last 7 days. System Restore in Windows Vista creates a checkpoint every 24 hours if no other restore points were created that day. System Restore in Windows XP creates a checkpoint every 24 hours of absolute time.

## Known issue: You cannot restore the system to a restore point after you install a Windows 10 update

Consider the following scenario:

1. You install Windows 10 on a clean computer.
1. You turn on system protection, and then create a system restore point that is named "R1."
1. You install one or more Windows 10 updates.
1. After the updates have finished installing, you restore the system to the "R1" restore point.

In this scenario, the system is not restored to the "R1" restore point. Instead, the computer experiences a Stop error (0xc000021a). You restart the computer, but the system cannot return to the Windows desktop.

### Cause

This is a known issue in Windows 10.

During the system restore process, Windows temporarily stages the restoration of files that are in use. It then saves the information in the registry. When the computer restarts, it completes the staged operation.

In this situation, Windows restores the catalog files and stages the driver `.sys` files to be restored when the computer restarts. However, when the computer restarts, Windows loads the existing drivers before it restores the later versions of the drivers. Because the driver versions do not match the versions of the restored catalog files, the restart process stops.

### Workaround

**To recover from the failed restart and continue the restore process**

After the failure occurs, restart the computer until it enters the Windows Recovery Environment (WinRE). To do this, you may have to use a hardware restart switch, and you may have to restart multiple times.

In the Windows Recovery Environment:

1. Select **Troubleshoot** > **Advanced options** > **More recovery options** > **Startup settings**, and then select **Restart now**.
1. In the list of startup settings, select **Disable driver signature enforcement**.
   > [!NOTE]  
   > You may have to use the F7 key to select this setting.
1. Allow the startup process to continue. When Windows restarts, the system restore process should resume and finish.

These steps restore the computer to its "R1" state.

**To recover from the failed restart and roll back the restore process**

1. As described in the previous procedure, restart the computer and then enter WinRE.  
1. In the Windows Recovery Environment, select **Troubleshoot** > **Advanced options** > **System restore**, and then select **Undo system restore**.

These steps return the computer to the state that it was in before you started the restore process.

**To restore Windows to a restore point by using WinRE**

To start the System Restore wizard on an affected computer, use WinRE instead of the **Settings** dialog box:

1. Select **Start** > **Settings** > **Update & Security** > **Recovery**.
1. Under **Advanced options**, select **Restart now**.
1. After WinRE starts, select **Troubleshoot** > **Advanced options** > **System restore**.
1. Enter your recovery key as it is shown on the screen, and then follow the instructions in the System Restore wizard.

### References

For information about how to use WinRE, see the following articles:

- [Windows Recovery Environment (Windows RE)](https://docs.microsoft.com/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference)
- [Start your PC in safe mode in Windows 10](https://support.microsoft.com/help/12376) 
