---
description: Working with 16-bit RGB
ms.assetid: 0a245187-4120-4003-9a8f-6b1e8fa40d38
title: Working with 16-bit RGB
ms.topic: article
ms.date: 05/31/2018
---

# Working with 16-bit RGB

Two formats are defined for 16-bit uncompressed RGB:

-   MEDIASUBTYPE\_555 uses five bits each for the red, green, and blue components in a pixel. The most significant bit in the **WORD** is ignored.
-   MEDIASUBTYPE\_565 uses five bits for the red and blue components, and six bits for the green component. This format reflects the fact that human vision is most sensitive to the green portions of the visible spectrum.

**RGB 565**

To extract the color components from an RGB 565 image, treat each pixel as a **WORD** type and use the following bit masks:


```C++
WORD red_mask = 0xF800;
WORD green_mask = 0x7E0;
WORD blue_mask = 0x1F;
```



Get the color components from a pixel as follows:


```C++
BYTE red_value = (pixel & red_mask) >> 11;
BYTE green_value = (pixel & green_mask) >> 5;
BYTE blue_value = (pixel & blue_mask);
```



Remember that the red and blue channels are 5 bits and the green channel is 6 bits. To convert these values to 8-bit components (for 24-bit or 32-bit RGB), you must left-shift the appropriate number of bits:


```C++
// Expand to 8-bit values.
BYTE red   = red_value << 3;
BYTE green = green_value << 2;
BYTE blue  = blue_value << 3;
```



Reverse this process to create an RGB 565 pixel. Assuming the color values have been truncated to the correct number of bits:


```C++
WORD pixel565 = (red_value << 11) | (green_value << 5) | blue_value;
```



**RGB 555**

Working with RGB 555 is essentially the same as RGB 565, except the bit masks and bit shift operations are different. To get the color components from an RGB 555 pixel, do the following:


```C++
WORD red_mask = 0x7C00;
WORD green_mask = 0x3E0;
WORD blue_mask = 0x1F;

BYTE red_value = (pixel & red_mask) >> 10;
BYTE green_value = (pixel & green_mask) >> 5;
BYTE blue_value = (pixel & blue_mask);

// Expand to 8-bit values:
BYTE red   = red_value << 3;
BYTE green = green_value << 3;
BYTE blue  = blue_value << 3;
```



To pack the red, green, and blue color values into an RGB 555 pixel, do the following:


```C++
WORD pixel565 = (red << 10) | (green << 5) | blue;
```



## Related topics

<dl> <dt>

[Uncompressed RGB Video Subtypes](uncompressed-rgb-video-subtypes.md)
</dt> </dl>

 

 



