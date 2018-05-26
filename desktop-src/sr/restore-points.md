---
title: Restore Points
description: Restore points are created to allow users a choice of previous system states. Each restore point contains the necessary information needed to restore the system to the chosen state. Restore points are created before key changes are made to the system.
ms.assetid: 5f68b377-4293-493e-afaf-f4414c2af1fb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

 

 




