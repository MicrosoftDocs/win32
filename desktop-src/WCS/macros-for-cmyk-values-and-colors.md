---
title: Macros for CMYK Values and Colors
description: The following macros are useful in manipulating CMYK values.
ms.assetid: e5d107fb-e010-400b-9ec5-90c2c0381dbe
keywords:
- Windows Color System (WCS),CMYK macros
- WCS (Windows Color System),CMYK macros
- image color management,CMYK macros
- color management,CMYK macros
- colors,CMYK macros
- WCS reference,CMYK macros
- reference for WCS,CMYK macros
- CMYK macros
- cyan magenta yellow black (CMYK)
- CMYK (cyan magenta yellow black)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Macros for CMYK Values and Colors

The following macros are useful in manipulating CMYK values.



| Macro                          | Description                                                                  |
|--------------------------------|------------------------------------------------------------------------------|
| [**CMYK**](/windows/win32/Wingdi/nf-wingdi-cmyk?branch=master)           | Builds a CMYK value from individual cyan, magenta, yellow, and black values. |
| [**GetCValue**](/windows/win32/Wingdi/nf-wingdi-getcvalue?branch=master) | Retrieves the cyan color value from a CMYK color value.                      |
| [**GetKValue**](/windows/win32/Wingdi/nf-wingdi-getkvalue?branch=master) | Retrieves the black color value from a CMYK color value.                     |
| [**GetMValue**](/windows/win32/Wingdi/nf-wingdi-getmvalue?branch=master) | Retrieves the magenta value from a CMYK color value.                         |
| [**GetYValue**](/windows/win32/Wingdi/nf-wingdi-getyvalue?branch=master) | Retrieves the yellow color value from a CMYK color value.                    |



 

The following macros are used with color.



| Macro                                | Description                                                                                                                                           |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetBValue**](https://msdn.microsoft.com/library/windows/desktop/dd144856)       | Gets an RGB blue value.                                                                                                                               |
| [**GetGValue**](https://msdn.microsoft.com/library/windows/desktop/dd144893)       | Gets an RGB green value.                                                                                                                              |
| [**GetRValue**](https://msdn.microsoft.com/library/windows/desktop/dd144923)       | Gets an RGB red value.                                                                                                                                |
| [**PALETTEINDEX**](https://msdn.microsoft.com/library/windows/desktop/dd162770) | Accepts an index to a logical-color palette entry and returns a palette-entry specifier.                                                              |
| [**PALETTERGB**](https://msdn.microsoft.com/library/windows/desktop/dd162771)     | Accepts three values that represent the relative intensities of red, green, and blue and returns a palette-relative red, green, blue (RGB) specifier. |
| [RGB](https://msdn.microsoft.com/library/windows/desktop/dd162937)                       | Selects a red, green, blue (RGB) color based on the arguments supplied and the color capabilities of the output device.                               |



 

 

 




