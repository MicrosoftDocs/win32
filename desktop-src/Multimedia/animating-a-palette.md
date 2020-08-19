---
title: Animating a Palette
description: Animating a Palette
ms.assetid: 89493cc3-eca9-407f-99c2-903fba16992c
keywords:
- DrawDib,palettes
- DrawDibRealize function
- DrawDibDraw function
- DrawDibChangePalette function
ms.topic: article
ms.date: 05/31/2018
---

# Animating a Palette

The following example animates a palette by using the [**DrawDibRealize**](/windows/desktop/api/Vfw/nf-vfw-drawdibrealize), [**DrawDibChangePalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibchangepalette), and [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) functions.

You can change the colors of a bitmap by using the [**DrawDibBegin**](/windows/desktop/api/Vfw/nf-vfw-drawdibbegin) function in combination with [**DrawDibChangePalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibchangepalette). First, to allow palette changes, specify the DDF\_ANIMATE flag in the call to **DrawDibBegin**. Second, set the color table values from the palette entries by using **DrawDibChangePalette**.

For example, if *lppe* is an address of the [PALETTEENTRY](/previous-versions//ms532623(v=vs.85)) array containing the new colors, and *lpbi* is the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure used in [**DrawDibBegin**](/windows/desktop/api/Vfw/nf-vfw-drawdibbegin) or [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw), the following fragment updates the DIB color table.


```C++
hdc = GetDC(hwnd); 
DrawDibBegin(hdd, ....., DDF_ANIMATE); 
DrawDibRealize(hdd, hdc, fBackground); 
DrawDibDraw(hdd, hdc, ...., DDF_SAME_DRAW|DDF_SAME_HDC); 
 
// Call to change color. 
DrawDibChangePalette(hDD, iStart, iLen, lppe); 
. 
. 
. 
ReleaseDC(hwnd, hdc); 

```



## Related topics

<dl> <dt>

[Using DrawDib](using-drawdib.md)
</dt> </dl>

 

 