---
title: Rendering Intents
description: The International Color Consortium (ICC) has defined four different values called rendering intents.
ms.assetid: c980f3ea-daff-491a-a10a-03ba446d383e
keywords:
- Windows Color System (WCS),rendering intents
- WCS (Windows Color System),rendering intents
- image color management,rendering intents
- color management,rendering intents
- colors,rendering intents
- rendering intents
- International Color Consortium (ICC)
- IIC (International Color Consortium)
- Picture intent
- Graphic intent
- Proof intent
- Match intent
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Rendering Intents

The International Color Consortium (ICC) has defined four different values called *rendering intents*. These represent four different approaches to creating a color rendering. These four intents, and the constants used to refer to them in code are as follows.



| Intent                            | ICC Name              | Description                    |
|-----------------------------------|-----------------------|--------------------------------|
| [Picture](#picture-intent) | Perceptual            | INTENT\_PERCEPTUAL             |
| [Graphic](#graphic-intent) | Saturation            | INTENT\_SATURATION             |
| [Proof](#proof-intent)     | Relative Colorimetric | INTENT\_RELATIVE\_COLORIMETRIC |
| [Match](#match-intent)     | Absolute Colorimetric | INTENT\_ABSOLUTE\_COLORIMETRIC |



 

The ICC Profile Format Specification Version 3.4, which describes these intents, can be downloaded from color.org.

## Picture Intent

Called perceptual intent in the ICC specification clause 4.9, a Picture intent causes the full [gamut](/windows/win32/wcs/g) of the image to be compressed or expanded to fill the gamut of the destination device, so that gray balance is preserved but colorimetric accuracy may not be preserved.

In other words, if certain colors in an image fall outside of the range of colors that the output device can render, the picture intent will cause all the colors in the image to be adjusted so that the every color in the image falls within the range that can be rendered and so that the relationship between colors is preserved as much as possible.

This intent is most suitable for display of photographs and images, and is generally the default intent.

## Graphic Intent

The ICC specification clause 4.12 calls the Graphic intent a [saturation](s.md) intent. It preserves the chroma of colors in the image at the possible expense of [hue](h.md) and [lightness](l.md).

Implementation of this intent remains somewhat problematic, and the ICC is still working on methods to achieve the desired effects.

This intent is most suitable for business graphics such as charts, where it is more important that the colors be vivid and contrast well with each other rather than a specific color.

## Proof Intent

The Proof intent, called the colorimetric intent in the ICC specification, is defined such that any colors that fall outside the range that the output device can render are adjusted to the closest color that can be rendered, while all other colors are left unchanged.

Proof intent does not preserve the [white point](w.md).

For example, the whitest white of a paper is more yellow than the whitest white of a computer monitor. An image converted into the gamut of the printer using relative colorimetric intent would result in all colors becoming more yellow. The white point of the image is moved to match the white point of the printer. All other colors in the image keep their position relative to the white point. This produces an image that more accurately reflects what the printed image will look like. However, the user may find it visually disconcerting.

## Match Intent

In a Match intent, any colors that fall outside the range that the output device can render are adjusted to the closest color that can be rendered, while all other colors are left unchanged. The ICC specification calls the match intent absolute colorimetric intent.

Match intent preserves the white point.

For example, the whitest white of a paper is more yellow than the whitest white of a computer monitor. An image converted into the [gamut](/windows/win32/wcs/g) of the printer using match intent would result in all colors being converted and matched into the gamut of the printer. The white point of the image is not moved to match the white point of the printer. Therefore, the distance of the colors to the white point may change. This produces an image that is less visually disconcerting to the user, but is also a less accurate rendition of printer output.

 

 




