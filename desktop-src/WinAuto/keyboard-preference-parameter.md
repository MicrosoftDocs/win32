---
title: Keyboard Preference Parameter
description: The keyboard preference parameter indicates that the user relies on the keyboard instead of the mouse, so applications should display keyboard interfaces that would otherwise be hidden.
ms.assetid: dc3c02d2-a350-4a86-a0b0-9dbb83880029
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Keyboard Preference Parameter

The keyboard preference parameter indicates that the user relies on the keyboard instead of the mouse, so applications should display keyboard interfaces that would otherwise be hidden.

The user controls the setting of the keyboard preference parameter by using the Ease of Access Center in Control Panel, or another application for customizing the environment. Applications use the **SPI\_GETKEYBOARDPREF** and **SPI\_SETKEYBOARDPREF** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to get and set the keyboard preference parameter.

Additionally, on Windows 2000, users can set a parameter that indicates whether menu access keys are always underlined. Applications use the **SPI\_GETMENUUNDERLINES** and **SPI\_SETMENUUNDERLINES** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to get and set the menu underlines parameter.

When an application receives a [**WM\_SETTINGCHANGE**](https://msdn.microsoft.com/library/windows/desktop/ms725497) message for either the keyboard preference or menu underline parameter, it is recommended that the application call [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) to update the information for both parameters.

Note that **SPI\_GETMENUUNDERLINES** is the same as **SPI\_GETKEYBOARDCUES**, and **SPI\_SETMENUUNDERLINES** is the same as **SPI\_SETKEYBOARDCUES**.

 

 




