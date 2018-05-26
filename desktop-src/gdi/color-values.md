---
Description: Color is defined as a combination of three primary colors red, green, and blue.
ms.assetid: 6e44935c-2b3b-4062-8273-f1f3e70300d2
title: Color Values
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Color Values

Color is defined as a combination of three primary colors red, green, and blue. the system identifies a color by giving it a color value (sometimes called an RGB triplet), which consists of three 8-bit values specifying the intensities of its color components. Black has the minimum intensity for red, green, and blue, so the color value for black is (0, 0, 0). White has the maximum intensity for red, green, and blue, so its color value is (255, 255, 255).

> [!Note]  
> If image color matching is enabled, the definition of color and the meaning of a color value depends on the type of color space that is currently set for the device context.

 

The system and applications use parameters and variables having the [COLORREF](colorref.md) type to pass and store color values. For example, the [**EnumObjects**](/windows/win32/Wingdi/nf-wingdi-enumobjects?branch=master) function identifies the color of each pen by setting the **lopnColor** member in a [**LOGPEN**](/windows/win32/Wingdi/ns-wingdi-taglogpen?branch=master) structure to a color value. Applications can extract the individual values of the red, green, and blue components from a color value by using the [**GetRValue**](/windows/win32/Wingdi/nf-wingdi-getrvalue?branch=master), [**GetGValue**](/windows/win32/Wingdi/nf-wingdi-getgvalue?branch=master), and [**GetBValue**](/windows/win32/Wingdi/nf-wingdi-getbvalue?branch=master) macros, respectively. Applications can create a color value from individual component values by using the [**RGB**](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master) macro. When creating or examining a logical palette, an application uses the [**RGBQUAD**](/windows/win32/Wingdi/ns-wingdi-tagrgbquad?branch=master) structure to define color values and to examine individual component values.

 

 



