---
title: Using GDI Functions With WCS
description: There are various functions in the graphics device interface (GDI) that use or operate on color data.
ms.assetid: a19ec8b9-11c9-4fde-a99a-7f4a112b49e7
keywords:
- Windows Color System (WCS),graphics device interface (GDI)
- WCS (Windows Color System),graphics device interface (GDI)
- image color management,graphics device interface (GDI)
- color management,graphics device interface (GDI)
- colors,graphics device interface (GDI)
- graphics device interface (GDI)
- GDI (graphics device interface)
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Using GDI Functions With WCS

There are various functions in the graphics device interface (GDI) that use or operate on color data. Some are enabled for use with WCS and some are not. The following GDI functions are relevant to ICM:

-   [Device Context Functions with WCS](#device-context-functions-with-wcs)
-   [Pen And Brush Functions with WCS](#pen-and-brush-functions-with-wcs)
-   [Text Output Functions with WCS](#text-output-functions-with-wcs)
-   [Bitmap Functions with WCS](#bitmap-functions-with-wcs)

## Device Context Functions with WCS



|                    |                                                                                                                                                                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CreateCompatibleDC | If the device context (DC) that is passed to this function through its hdc parameter is enabled for ICM, then the DC the function creates is also ICM-enabled. The source and destination color spaces are specified in the DC. |
| CreateDC           | ICM can be enabled by setting the dmICMMethod member of the DEVMODE structure pointed to by the pInitData parameter to the appropriate value. For details, see the documentation in the Platform SDK on the DEVMODE structure.  |
| ResetDC            | The color profile of the device context specified by the hdc parameter will be reset based on the information in the DEVMODE structure specified by the lpInitData parameter.                                                   |



 

## Pen And Brush Functions with WCS



|                 |                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Brush Functions | No color management is done at brush creation. However, color management will be performed when the brush is selected into an ICM-enabled DC. |
| CreatePen       | No color management is done at pen creation. However, color management will be performed when the brush is selected into an ICM-enabled DC.   |
| ExtCreatePen    | No color management is done at pen creation. However, color management will be performed when the brush is selected into an ICM-enabled DC.   |
| SelectObject    | If the object being selected is a brush or a pen, color management is performed.                                                              |
| SetDCBrushColor | Color management is performed if WCS is enabled.                                                                                              |
| SetDCPenColor   | Color management is performed if WCS is enabled.                                                                                              |



 

## Text Output Functions with WCS



|              |                                                  |
|--------------|--------------------------------------------------|
| SetBkColor   | Color management is performed if WCS is enabled. |
| SetTextColor | Color management is performed if WCS is enabled. |



 

## Bitmap Functions with WCS



|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BitBlt            | No color management is performed when blits occur.                                                                                                                                                                                                                                                                                                                                                                                             |
| CreateDIBitmap    | The fuUsage parameter specifies that the bmiColors member of the BITMAPINFO structure pointed at by the lpbmi parameter does or does not contain color information. If it does not, no color management is performed for this bitmap. The bitmap must use version 4 or version 5 of the BITMAPINFO structure for color management to be enabled. The contents of the resulting bitmap are not color matched after the bitmap has been created. |
| CreateDIBSection  | If the BITMAPINFO structure passed through the pbmi parameter is not version 4 or version 5, no color management is done. If it is version 4 or 5, color management is enabled, and the specified color space is associated with the bitmap.                                                                                                                                                                                                   |
| MaskBlt           | No color management is performed when blits occur.                                                                                                                                                                                                                                                                                                                                                                                             |
| SelectObject      | If the object is a bitmap created with CreateDIBSection, color management is performed. The bitmap's color space is used as the destination color space.                                                                                                                                                                                                                                                                                       |
| SetDIBits         | Color management is performed. If the specified BITMAPINFO structure is not version 4 or version 5, the color profile of the current DC is used as the source color space profile. If it does not have one, the sRGB space is used. If the specified BITMAPINFO structure is version 4 or version 5, the color space profile specified in the bitmap header is used as the source color space profile.                                         |
| SetDIBitsToDevice | Color management is performed. If the specified BITMAPINFO structure is not version 4 or version 5, the color profile of the current device context is used as the source color space profile. If it doesn't have one, the sRGB color space is used. If the specified BITMAPINFO structure is version 4 or version 5, the color space profile associated with the bitmap is used as the source color space.                                    |
| SetDIBColorTable  | No color management is performed.                                                                                                                                                                                                                                                                                                                                                                                                              |
| StretchBlt        | No color management is performed when blits occur.                                                                                                                                                                                                                                                                                                                                                                                             |
| StretchDIBits     | Color management is performed. If the specified BITMAPINFO structure is not version 4 or version 5, the color profile of the current DC is used as the source color space profile. If it does not have one, the sRGB space is used. If the specified BITMAPINFO structure is version 4 or version 5, the color space profile specified in the bitmap header is used as the source color space profile.                                         |



 

 

 




