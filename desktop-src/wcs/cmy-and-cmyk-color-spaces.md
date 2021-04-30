---
title: CMY and CMYK Color Spaces
description: The CMY and CMYK color spaces are often used in color printing. A CMY color space uses cyan, magenta, and yellow (CMY) as its primary colors. Red, green, and blue are the secondary colors.
ms.assetid: e135b5ef-fa5c-49b7-8537-5dc31cde2418
keywords:
- Windows Color System (WCS),CMY color spaces
- WCS (Windows Color System),CMY color spaces
- image color management,CMY color spaces
- color management,CMY color spaces
- colors,CMY color spaces
- color spaces,CMY
- CMY color spaces
- Windows Color System (WCS),CMYK color spaces
- WCS (Windows Color System),CMYK color spaces
- image color management,CMYK color spaces
- color management,CMYKcolor spaces
- colors,CMYK color spaces
- color spaces,CMYK
- CMYK color spaces
- cyan
- magenta
- yellow
- cyan magenta yellow (CMY)
- CMY (cyan magenta yellow)
- cyan magenta yellow black (CMYK)
- CMYK (cyan magenta yellow black)
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# CMY and CMYK Color Spaces

The CMY and CMYK [color spaces](c.md) are often used in color printing. A CMY color space uses cyan, magenta, and yellow (CMY) as its [primary colors](p.md). Red, green, and blue are the secondary colors.

The following figures are color representations of the CMY color space. The CMY color space is normalized.

![cmy color space cube at maximum values](images/cmyclrs1.png)

![cmy color space cube at minimum values](images/cmyclrs2.png)

The CMY color space is subtractive. Therefore, white is at (0.0, 0.0, 0.0) and black is at (1.0, 1.0, 1.0). If you start with white and subtract no colors, you get white. If you start with white and subtract all colors equally, you get black.

The CMYK color space is a variation on the CMY model. It adds black (Cyan, Magenta, Yellow, and blacK). The CMYK color space closes the gap between theory and practice. In theory, the extra black component is not needed. However, experience with various types of inks and papers has shown that when equal components of cyan, magenta, and yellow inks are mixed, the result is usually a dark brown, not black. Adding black ink to the mix solves this problem.

The CMY and CMYK colors spaces can be device independent, but most often they are used in reference to a specific device.

 

 




