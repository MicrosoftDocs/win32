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
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Macros for CMYK Values and Colors

The following macros are useful in manipulating CMYK values.



| Macro                          | Description                                                                  |
|--------------------------------|------------------------------------------------------------------------------|
| [**CMYK**](/windows/desktop/api/Wingdi/nf-wingdi-cmyk)           | Builds a CMYK value from individual cyan, magenta, yellow, and black values. |
| [**GetCValue**](/windows/desktop/api/Wingdi/nf-wingdi-getcvalue) | Retrieves the cyan color value from a CMYK color value.                      |
| [**GetKValue**](/windows/desktop/api/Wingdi/nf-wingdi-getkvalue) | Retrieves the black color value from a CMYK color value.                     |
| [**GetMValue**](/windows/desktop/api/Wingdi/nf-wingdi-getmvalue) | Retrieves the magenta value from a CMYK color value.                         |
| [**GetYValue**](/windows/desktop/api/Wingdi/nf-wingdi-getyvalue) | Retrieves the yellow color value from a CMYK color value.                    |



 

The following macros are used with color.



| Macro                                | Description                                                                                                                                           |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetBValue**](/windows/win32/api/wingdi/nf-wingdi-getbvalue)       | Gets an RGB blue value.                                                                                                                               |
| [**GetGValue**](/windows/win32/api/wingdi/nf-wingdi-getgvalue)       | Gets an RGB green value.                                                                                                                              |
| [**GetRValue**](/windows/win32/api/wingdi/nf-wingdi-getrvalue)       | Gets an RGB red value.                                                                                                                                |
| [**PALETTEINDEX**](/previous-versions//dd162770(v=vs.85)) | Accepts an index to a logical-color palette entry and returns a palette-entry specifier.                                                              |
| [**PALETTERGB**](/windows/win32/api/wingdi/nf-wingdi-palettergb)     | Accepts three values that represent the relative intensities of red, green, and blue and returns a palette-relative red, green, blue (RGB) specifier. |
| [RGB](/windows/win32/api/wingdi/nf-wingdi-rgb)                       | Selects a red, green, blue (RGB) color based on the arguments supplied and the color capabilities of the output device.                               |



 

 

 