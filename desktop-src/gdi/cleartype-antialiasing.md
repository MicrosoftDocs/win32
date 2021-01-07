---
description: Microsoft ClearType antialiasing is a smoothing method that improves font display resolution over traditional antialiasing.
ms.assetid: b9896934-1e4f-4ae1-922a-ef30e0edf94f
title: ClearType Antialiasing
ms.topic: article
ms.date: 05/31/2018
---

# ClearType Antialiasing

Microsoft ClearType antialiasing is a smoothing method that improves font display resolution over traditional antialiasing. It dramatically improves readability on color LCD monitors with a digital interface, such as those in laptops and high-quality flat desktop displays. Readability on CRT screens is also somewhat improved.

However, ClearType is dependent on the orientation and ordering of the LCD stripes. Currently, ClearType is implemented only for LCDs with vertical stripes that are ordered RGB. In particular, this affects tablet PCs, where the display can be oriented in any direction, and those screens that can be turned from landscape to portrait.

ClearType antialiasing is allowed:

-   For 16-, 24-, and 32-bit color (disabled for 256 colors or less)
-   For screen DC and memory DC (not for printer DC)
-   For TrueType fonts and OpenType fonts with TrueType outlines

ClearType antialiasing is disabled:

-   Under terminal server client
-   For bitmap fonts, vector fonts, device fonts, Type 1 fonts, or Postscript OpenType fonts without TrueType outlines
-   If the font has tuned embedded bitmaps, only for those font sizes that contain the embedded bitmaps

To activate ClearType antialiasing, call [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) once to turn on font smoothing and then a second time to set the smoothing type to FE\_FONTSMOOTHINGCLEARTYPE, as shown in the following code sample:


```C++
SystemParametersInfo(SPI_SETFONTSMOOTHING,
                     TRUE,
                     0,
                     SPIF_UPDATEINIFILE | SPIF_SENDCHANGE);
SystemParametersInfo(SPI_SETFONTSMOOTHINGTYPE,
                     0,
                     (PVOID)FE_FONTSMOOTHINGCLEARTYPE,
                     SPIF_UPDATEINIFILE | SPIF_SENDCHANGE); 
```



You can adjust the appearance of text by changing the contrast value used in the ClearType algorithm. The default is 1,400, but it can be any value from 1,000 to 2,200. Depending on the display device and the user's sensitivity to colors, a higher or lower contrast value may improve readability. To change the contrast, call [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) with SPI\_SETFONTSMOOTHINGCONTRAST. The following code sets the contrast value to 1,600.


```C++
SystemParametersInfo(SPI_SETFONTSMOOTHINGCONTRAST,
                     0,
                     (PVOID)1600,
                     SPIF_UPDATEINIFILE | SPIF_SENDCHANGE); 
```



You should consider the following details for application compatibility:

-   Text rendering with ClearType is slightly slower than with standard antialiasing.
-   Applications should not use XOR to display selected text. Applications should set the background color and redisplay the selected text.
-   Applications should not paint the same text on top of itself in transparent mode. If this occurs, the edge pixels that are antialiased will color merge with themselves instead of with the background color. This results in darkened and colorful edges.
-   Applications should not paint text by painting the characters individually when in opaque mode because the edge of a character may be clipped by the following character. This occurs because a character that is smoothed with ClearType may have a negative A or C width where the regular character has a positive A or C width. Only the B width of the character is guaranteed to be the same. Likewise, applications should be careful if smoothed text is next to unsmoothed text.
-   If an application renders text and then manipulates the bitmap, font smoothing should be turned off by setting the **lfQuality** member of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure to NONANTIALIASED\_QUALITY. For example, a game may add a bitmap shadow effect, or text rendered into a bitmap may be scaled to produce a thumbview.
-   If the user is running in portrait mode (that is, monitor striping is horizontal) ClearType antialiasing should be disabled.

The *fdwQuality* parameter in [**CreateFont**](/windows/desktop/api/Wingdi/nf-wingdi-createfonta) and the **lfQuality** member of [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) accept the CLEARTYPE\_QUALITY flag. Rasterization of fonts created with this flag will use the ClearType rasterizer. This flag has no effect on previous versions of the operating system.

 

 
