---
Description: Using owner-drawn menus to support speech functionality for the Tablet PC.
ms.assetid: fbe2d420-f667-416b-bff3-0fee9ae22203
title: Using Owner-Drawn Menus
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Owner-Drawn Menus

When using owner-drawn menus, you must make the menu names available to support speech functionality. There are two ways to do this:

-   Expose the menu item name by using the MSAAMENUINFO structure.
-   Provide an option to replace graphic menus with standard text menus when an accessibility aid is active. If the [**SystemParametersInfo**](https://msdn.microsoft.com/9b99465c-e12d-413c-8e69-b46b52f2f11f) function returns **TRUE** with its *uiAction* parameter set to SPI\_GETSCREENREADER, use standard menus.The application should watch for the WM\_SETTINGSCHANGE message and respond by querying the state of this option and adjusting its display appropriately. For example, Microsoft Visual Studio provides an option to use standard menus instead of the custom menus that are displayed by default.

 

 



