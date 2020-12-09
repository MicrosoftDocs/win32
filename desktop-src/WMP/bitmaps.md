---
title: Bitmaps (Windows Media Player SDK)
description: Bitmaps
ms.assetid: cd10bc7d-1167-485e-8acf-13c021bc608b
keywords:
- Windows Media Player Mobile skins,bitmaps
- skins,bitmaps
- reference for skins,bitmaps
- bitmaps in skins,about
ms.topic: article
ms.date: 05/31/2018
---

# Bitmaps (Windows Media Player SDK)

You must use one or more images in your skin, and each image must be defined in the skin definition file. If you do not define an image in this section, your skin will not be able to use it.

The term "bitmap" is used throughout the reference in a generic sense, and refers to bitmap images with a .bmp extension, GIF images with a .gif extension, JPEG images with a .jpg extension, and PNG images with a .png extension.

The Bitmaps section of the skin definition file begins with this line:


```C++
[ Bitmaps ]

```



You then must add one or more lines that contain information about each of the images in your skin.

A typical line might be:


```C++
    Background  Background.bmp  0,0

```



You can use the following template for the Bitmaps section of your skin definition file:


```C++
//  <Type>      <Filename>      <X,Y>
//  ------      -----------     -----

```



You must use the following order for bitmap information for each line in the Bitmap section. Each part of the line is required.

1.  [Bitmap Type](bitmap-type.md)
2.  [File Name](file-name.md)
3.  [Coordinates](coordinates.md)

For an example of bitmap code, see [Sample Bitmap Section](sample-bitmap-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




