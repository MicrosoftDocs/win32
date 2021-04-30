---
title: Device-Independent Color Spaces
description: Recognizing the need for standard, device-independent color measurements, the Commission International de l'Eclairage (International Commission on Illumination), or CIE, created a color space based on \ 0034;imaginary \ 0034; primary colors.
ms.assetid: 8597dad3-1eb8-49f9-9843-1f9068a65925
keywords:
- Windows Color System (WCS),device-independent color spaces
- WCS (Windows Color System),device-independent color spaces
- image color management,device-independent color spaces
- color management,device-independent color spaces
- colors,device-independent color spaces
- color spaces,device-independent
- device-independent color spaces
- Commission International de l'Eclairage (CIE)
- International Commission on Illumination (CIE)
- CIE (Commission International de l'Eclairage)
- CIE (International Commission on Illumination)
- CIEXYZ color space
- XYZ color space
- sRGB color space
- color spaces,CIEXYZ
- color spaces,sRGB
- color spaces,XYZ
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Device-Independent Color Spaces

Recognizing the need for standard, device-independent color measurements, the Commission International de l'Eclairage (International Commission on Illumination), or CIE, created a [color space](c.md) based on "imaginary" [primary colors](p.md). No actual device is expected to produce colors in this color space. It is used as a means of converting colors from one color space to another. The primary colors in this color space are the abstract colors X, Y, and Z.

The 1931 CIEXYZ color space is widely used as the basis for color space conversion. With the rise of the Internet, however, bandwidth considerations have made the XYZ color space unwieldy. The exchange of images over the limited bandwidth of the Internet necessitates a more compact [color model](c.md).

As a result, Hewlett-Packard and Microsoft have proposed the adoption of a standard predefined RGB color space known as sRGB, so as to allow accurate color management with very little data overhead. This standard has been approved as a formal international standard by the International Electrotechnical Commission (IEC) as IEC 61966-2-1: Multimedia Systems and EquipmentColour Measurement and ManagementPart 2-1: Colour ManagementDefault RGB Colour Space. It is available directly from the IEC at <https://www.iec.ch/>. Information discussing the technical issues involved in sRGB is available on the Internet at:

[A Standard Default Color Space for the Internet - sRGB](https://www.w3.org/Graphics/Color/sRGB.html)

A help-file version of a white paper discussing the technical issues involved in sRGB, sRGB.HLP, is available in the \\Help folder of the WCS 1.0 Programmer's Reference in the Platform SDK.

Different file formats may use or add a flag to specify that the image is in sRGB color space. In the Windows device-independent bitmap (DIB) format, setting the **bV5CSType** member of the [BITMAPV5HEADER](using-structures-in-wcs-1-0.md) structure to LCS\_sRGB specifies that the DIB colors are in the sRGB color space.

 

 




