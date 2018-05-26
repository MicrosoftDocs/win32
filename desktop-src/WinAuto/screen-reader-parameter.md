---
title: Screen Reader Parameter
description: The screen reader parameter indicates whether an application should provide textual information in situations where it would otherwise present the information graphically.
ms.assetid: ac79c389-511c-4403-a8d5-75b2eba2b39f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Screen Reader Parameter

The screen reader parameter indicates whether an application should provide textual information in situations where it would otherwise present the information graphically.

This parameter is typically set by accessibility aids such as screen readers. Applications use the **SPI\_GETSCREENREADER** and **SPI\_SETSCREENREADER** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to get and set the screen reader parameter.

> [!Note]  
> Narrator, the screen reader that is included with Windows, does not set the **SPI\_SETSCREENREADER** or **SPI\_GETSCREENREADER** flags.

 

 

 




