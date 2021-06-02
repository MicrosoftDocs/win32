---
title: Device-Dependent Color Spaces
description: Most color spaces are device dependent.
ms.assetid: 657ec64b-8605-4d05-a7d6-9f8bb71e6a71
keywords:
- Windows Color System (WCS),device-dependent color spaces
- WCS (Windows Color System),device-dependent color spaces
- image color management,device-dependent color spaces
- color management,device-dependent color spaces
- colors,device-dependent color spaces
- color spaces,device-dependent
- device-dependent color spaces
- white point
- colorants
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Device-Dependent Color Spaces

Most [color spaces](c.md) are device dependent. Even though a particular device, such as a printer, may use the CMYK color space, the colors it renders for specific CMYK values are often slightly different than all other types of printers.. It is precisely for this reason that the WCS 1.0 color management system is so useful.

All color spaces have a*white point*, which is defined as the whitest white that can be produced in that color space. Since devices can differ from one another, their white points can also differ. All colors that a device can produce are relative to its white point. Therefore, a color management system must be able to map the white point of one color space into another and preserve the relative locations of all colors. It must also be able to map a color in one color space to its closest match in another color space regardless of the differences in the white points. WCS 1.0 is able to accomplish both of these tasks.

The RGB color space is often used on computer monitors. As such, it is device dependent. Printers typically use CMYK [colorants](c.md). Each printer implements its own version of the CMYK color space. Digital images may not actually store colors in them. They may store index numbers into a palette of colors. The result is that it is very hard for individual application developers to use or provide a standardized method of moving color images from one device to another. Imaging professionals commonly experience the frustration of creating a graphic image on a computer screen and having it turn out very differently when it is printed. WCS 1.0 addresses these imaging needs.

 

 




