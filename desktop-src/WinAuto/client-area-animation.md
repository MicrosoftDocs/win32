---
title: Client Area Animation
description: The client area animation flag indicates whether the user wants to disable animations in UI elements.
ms.assetid: 4a3ec9da-d5ae-4cd9-8222-f02143895ce4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Client Area Animation

The client area animation flag indicates whether the user wants to disable animations in UI elements. Display features such as flashing, blinking, flickering, and moving content can cause seizures in users with photo-sensitive epilepsy. This flag enables you to enable or disable all such animations.

Applications use the **SPI\_GETCLIENTAREAANIMATION** and **SPI\_SETCLIENTAREAANIMATION** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to turn client area animations on or off.

 

 




