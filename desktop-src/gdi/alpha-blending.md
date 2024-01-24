---
description: Alpha blending is used to display an alpha bitmap, which is a bitmap that has transparent or semi-transparent pixels.
ms.assetid: 52a044cc-a471-4951-adbe-32319b8e3129
title: Alpha Blending (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Blending (Windows GDI)

*Alpha blending* is used to display an alpha bitmap, which is a bitmap that has transparent or semi-transparent pixels. In addition to a red, green, and blue color channel, each pixel in an alpha bitmap has a transparency component known as its *alpha channel*. The alpha channel typically contains as many bits as a color channel. For example, an 8-bit alpha channel can represent 256 levels of transparency, from 0 (the entire bitmap is transparent) to 255 (the entire bitmap is opaque).

Alpha blending mechanisms are invoked by calling [**AlphaBlend**](/windows/desktop/api/WinGdi/nf-wingdi-alphablend), which references the [**BLENDFUNCTION**](/windows/desktop/api/Wingdi/ns-wingdi-blendfunction) structure.

Alpha values per pixel are only supported for 32-bpp BI\_RGB. This formula is defined as:


```C++
typedef struct {
  BYTE   Blue;
  BYTE   Green;
  BYTE   Red;
  BYTE   Alpha;
};
```



This is represented in memory as shown in the following table.

:::row:::
    :::column:::
        31:24
    :::column-end:::
    :::column:::
        23:16
    :::column-end:::
    :::column:::
        15:08
    :::column-end:::
    :::column:::
        07:00
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        Alpha
    :::column-end:::
    :::column:::
        Red
    :::column-end:::
    :::column:::
        Green
    :::column-end:::
    :::column:::
        Blue
    :::column-end:::
:::row-end:::

Bitmaps may also be displayed with a transparency factor applied to the entire bitmap. Any bitmap format can be displayed with a global constant alpha value by setting **SourceConstantAlpha** in the [**BLENDFUNCTION**](/windows/desktop/api/Wingdi/ns-wingdi-blendfunction) structure. The global constant alpha value has 256 levels of transparency, from 0 (entire bitmap is completely transparent) to 255 (entire bitmap is completely opaque). The global constant alpha value is combined with the per-pixel alpha value.

For an example, see [Alpha Blending a Bitmap](alpha-blending-a-bitmap.md).

 

 



