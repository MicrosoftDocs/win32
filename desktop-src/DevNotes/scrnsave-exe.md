---
description: HKCU\\Control Panel\\Desktop.
ms.assetid: e18ea3c8-ddac-4214-83be-106c28c3c327
title: SCRNSAVE.EXE
ms.topic: article
ms.date: 05/31/2018
---

# SCRNSAVE.EXE

**HKCU\\Control Panel\\Desktop**



| Data type | Range       | Default value |
|-----------|-------------|---------------|
| REG\_SZ   | *File name* | (None)        |



 

## Description

Specifies the name of the screen saver executable file.

## Change Method

To change the value of this entry, in Control Panel double-click **Display**, click the **Screen Saver** tab, and then select a screen saver from the **Screen saver** list.

You can also change this entry with the application programming interface (API) function **InstallScreenSaver**, which is exported by Desk.cpl. You can access this function with the command line **rundll32.exe desk.cpl,InstallScreenSaver** *file*, where *file* is the name of a screen saver executable file.

## Activation Method

Changes made to this entry become effective the next time the system starts a screen saver. Changes made to this entry while a screen saver is running have no effect on the running screen saver.

## Notes

-   Windows operating systems add this entry to the registry when you use **Display** in Control Panel to select a screen saver. If you disable all screen savers by choosing **(None)** from the screen saver list, then the operating system deletes this entry from the registry and calls the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function with *uiAction* equal to SPI\_SETSCREENSAVEACTIVE and *uiParam* equal to **FALSE**.
-   This entry can be superseded by a Group Policy setting on systems that support Group Policy. While the **Screen saver executable name** Group Policy setting is enabled, the system ignores this entry. The configuration of this policy setting is stored in the **SCRNSAVE.EXE** entry, which is in the **Policies** subkey.

 

 
