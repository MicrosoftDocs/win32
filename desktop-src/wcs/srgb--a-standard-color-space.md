---
title: sRGB A Standard Color Space
description: As a result of Internet bandwidth considerations, Hewlett-Packard and Microsoft have proposed the adoption of a standard predefined color space known as sRGB (IEC 61966-2-1), so as to allow accurate color mapping with very little data overhead.
ms.assetid: b9017702-7dca-4d79-bed0-936f97cb6109
keywords:
- Windows Color System (WCS),sRGB color space
- WCS (Windows Color System),sRGB color space
- image color management,sRGB color space
- color management,sRGB color space
- colors,sRGB color space
- sRGB color space
- color spaces,sRGB


ms.topic: article
ms.date: 05/31/2018
---

# sRGB: A Standard Color Space

As a result of Internet bandwidth considerations, Hewlett-Packard and Microsoft have proposed the adoption of a standard predefined [color space](c.md) known as *sRGB* (IEC 61966-2-1), so as to allow accurate [color mapping](c.md) with very little data overhead.

A help-file version of a white paper discussing the technical details of sRGB, sRGB.hlp, is available in the \\Help folder of the WCS 1.0 Programmer's Reference.

Different file formats may use or add a flag to specify that the image is in sRGB color space. In the Windows device-independent bitmap (DIB) format, setting the **bV5CSType** member of the [**BITMAPV5HEADER**](using-structures-in-wcs-1-0.md) structure to **LCS\_sRGB** specifies that the DIB colors are in the sRGB color space.

WCS 1.0 provides native support for sRGB. There are two ways to use WCS 1.0 for rendering an image defined in the sRGB color space:

**To render an image inside the device context**

1.  Create a device context (DC) on the display device.
2.  Set color management using the [**SetICMMode**](/windows/desktop/api/Wingdi/nf-wingdi-seticmmode) function.
3.  Use the [**SetDIBitsToDevice**](/windows/win32/api/wingdi/nf-wingdi-setdibitstodevice) function to transfer the DIB into the DC. As long as the **bV5CSMType** member of the DIBs [**BITMAPV5HEADER**](using-structures-in-wcs-1-0.md) structure is set to **LCS\_sRGB**, the system will perform the appropriate color management.

**To render an image outside the device context**

1.  Create a transform using [**CreateColorTransformW**](/windows/win32/api/icm/nf-icm-createcolortransformw). The **lcsCSType** member of the [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure pointed to by the *pLogColorSpace* parameter should be set to **LCS\_sRGB**. The *hDestProfile* parameter indicates the display device's color space.
2.  Use the created color transform to color match the image before displaying it on the device.

## WCS 1.0 Defaults for Input Color Space and Output Profile

When no input color space is specified, by default WCS 1.0 uses the sRGB color space as the input color space for [color mapping](c.md).

When no output profile is specified, but a default device is specified, WCS 1.0 selects a default output profile. If the default device does not have an associated profile, WCS 1.0 uses the sRGB color space as the output profile.

The following table shows the resulting color transforms when a default device is not available.



|  &nbsp;                               | Output Profile Specified                              | Output Profile Not Specified                             |
|---------------------------------|-------------------------------------------------------|----------------------------------------------------------|
| Input Color Space Specified     | Transform uses the specified profiles.                | Transform converts from known input color space to sRGB. |
| Input Color Space Not Specified | Transform converts from sRGB to known output profile. | Transform from sRGB to sRGB is assumed; nothing is done. |



 

## sRGB and Embedded Profiles

Beginning with ICM version 2.0, applications that utilize WCS can embed profiles in images. Embedded profiles assist users' applications in maintaining a consistent color appearance even if images are transmitted across the Internet.

Images that use the sRGB color space do not need an embedded color profile. Because they have no embedded profile, sRGB-based images are smaller and more readily transferable across data channels with limited bandwidth.

Applications should set the **LCS\_sRGB** flag in the image's bitmap header to indicate that the image uses the sRGB color space. For details, see [Windows Bitmap Header Structures](using-structures-in-wcs-1-0.md) and [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea).

 

 
