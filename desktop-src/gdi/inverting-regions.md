---
Description: An application inverts the colors that appear within a region by calling the InvertRgn function.
ms.assetid: bcd9fe61-0f92-41bc-b953-a66e01e43a75
title: Inverting Regions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Inverting Regions

An application inverts the colors that appear within a region by calling the [**InvertRgn**](/windows/win32/Wingdi/nf-wingdi-invertrgn?branch=master) function. On monochrome displays, **InvertRgn** makes white pixels black and black pixels white. On color screens, this inversion is dependent on the type of technology used to generate the colors for the screen.

 

 



