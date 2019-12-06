---
title: Restore points
description: Restore points are created to allow users a choice of previous system states. Each restore point contains the necessary information needed to restore the system to the chosen state. Restore points are created before key changes are made to the system.
ms.assetid: 5f68b377-4293-493e-afaf-f4414c2af1fb
ms.topic: article
ms.date: 12/06/2019
manager: dcscontentpm
ms.custom: CSSTroubleshooting
---

# Restore points

Restore points are created to allow users to select a previous system state. Each restore point contains the information needed to restore the system to the chosen state. Restore points are created before key changes are made to the system.

System Restore automatically manages the disk space that is allocated for restore points. It purges the oldest restore points to make room for new ones. System Restore allocates space based on the size of the hard disk and the version of Windows that the computer runs, as shown in the following table.

|Windows version |Hard&nbsp;disk size |System Restore space |
| --- | --- | --- |
|Windows 7 and later versions | >64 GB |Up to 5 percent of the disk space or a maximum of 10 GB of the disk space, whichever is less |
|  | &le;64 GB |Up to 3 percent of the disk space |
|Windows Vista |  |Up to 15 percent of the total disk space or a maximum of 30 percent of the free disk space, whichever is less |
|Windows XP | >4 GB |Up to 12 percent of the disk space<br />To change the maximum storage limit in Windows XP, use the System application in the Control Panel. |
|  | \<4 GB |Up to 400 MB |

## Event-triggered restore points

System Restore automatically creates a restore point before the following events:

- **Application installation** (provided the application uses an installer that is System Restore-compliant). If installing the application causes system problems, the user can restore the system to a state that precedes the installation.
- **Windows Update or AutoUpdate installation**. Windows Update (previously known as AutoUpdate) automatically downloads and installs Windows updates. Additionally, it provides an easy way for users to manually download and install updates. In any case, before an update installs, System Restore creates a restore point.
- **System restore operation**. System Restore automatically creates a restore point as a backup before any restore operation starts. For example, suppose a user accidentally restores Windows to the wrong restore point. To undo that restoration, the user can restore Windows again and select the pre-restore restore point. After Windows has been restored to its initial state, the user can restore again, this time selecting the correct restore point.

## Scheduled restore points

Users can configure System Restore to create restore points at regular intervals. Users can also manually create and name a restore point at any time from within the System Restore user interface. These restore points are saved and compressed, and are available in the list of restore points.

In Windows 7 and later versions, System Restore creates a scheduled restore point only if no other restore points have been created in the previous seven days. In Windows Vista, System Restore creates a checkpoint every 24 hours if no other restore points were created that day. In Windows XP, System Restore creates a checkpoint every 24 hours of absolute time.

## Known issue: You cannot restore the system to a restore point after you install a Windows 10 update

Consider the following scenario:

1. You install Windows 10 on a clean computer.
1. You turn on system protection, and then create a system restore point that is named "R1."
1. You install one or more Windows 10 updates.
1. After the updates have finished installing, you restore the system to the "R1" restore point.

In this scenario, the system is not restored to the "R1" restore point. Instead, the computer experiences a Stop error (0xc000021a). When you restart the computer, the system cannot return to the Windows desktop.

### Cause

This is a known issue in Windows 10.

During the system restore process, Windows temporarily stages the restoration of files that are in use. It then saves the information in the registry. When the computer restarts, it completes the staged operation.

In this situation, Windows restores the catalog files and stages the driver (.sys) files to be restored when the computer restarts. However, when the computer restarts, Windows loads the existing drivers before it restores the later versions of the drivers. Because the driver versions do not match the versions of the restored catalog files, the restart process stops.

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
