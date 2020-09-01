---
title: Windows 7 Backup and Restore deprecated
description: Windows 7 Backup and Restore deprecated
ms.assetid: 89FB9C1B-FEE8-4508-9501-EA139F3706F7
ms.topic: article
ms.date: 05/31/2018
---

# Windows 7 Backup and Restore deprecated

## Platform

**Clients** – Windows 8 


## Description

While there is no behavioral change to Backup and Restore, this function is being deprecated and will not be updated. It was rarely used and its functionality has been replaced by the new File History feature. It will ship in Windows 8 and enthusiasts who upgraded from Windows 7 to Windows 8 or depend on Backup and Restore or disk image backup will be still able to use it. However, all access points to Backup and Restore, with the exception of the Control Panel, have been removed. The Control Panel applet used by Backup and Restore was renamed to Windows 7 File Recovery.

OEMs that were setting the registry key to disable backup notification in their images will no longer need to do that.

We do not recommend using both features at the same time. File History checks if Backup schedule exists and is active and if it finds one, it will not let users to turn it on. In this case, users who want to use File History will have to delete the Windows Backup schedule.

## Manifestation

Workflows may be interrupted and documentation that refers to the previous method for accessing the Windows Backup and Restore feature will need to be updated to reflect these changes.

## Mitigation

Apps that might trigger Backup and Restore should be rewritten to check if File History is on and let users choose their preferred method.

 

 




