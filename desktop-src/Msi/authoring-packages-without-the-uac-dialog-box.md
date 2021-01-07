---
description: When elevated privileges are not required to install a Windows Installer package, the author of the package can suppress the dialog box that User Account Control (UAC) displays to prompt users for administrator authorization.
ms.assetid: cab30f95-cc93-46db-aba5-741b44adb6de
title: Authoring Packages without the UAC Dialog Box
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Packages without the UAC Dialog Box

When elevated privileges are not required to install a Windows Installer package, the author of the package can suppress the dialog box that [*User Account Control*](u-gly.md) (UAC) displays to prompt users for administrator authorization.

To suppress the display of the UAC dialog box when installing the application, the author of the package should do the following:

-   Install the application using Window Installer 4.0 or later on Windows Vista.
-   Do not depend on using elevated system privileges to install the application on the computer.
-   Install the application in the per-user context and make this the default installation context of the package. If the [**ALLUSERS**](allusers.md) property is not set, the installer installs the package in the per-user context. If you do not include the **ALLUSERS** property in the [Property table](property-table.md), the installer does not set this property and so per-user installation becomes the default installation context. You can override this default by setting the **ALLUSERS** property on the command line.
-   Set Bit 3 in the [**Word Count Summary**](word-count-summary.md) property to indicate that elevated privileges are not required to install the application.

 

 



