---
title: Animating a Palette
description: Animating a Palette
ms.assetid: '89493cc3-eca9-407f-99c2-903fba16992c'
keywords: ["DrawDib,palettes", "DrawDibRealize function", "DrawDibDraw function", "DrawDibChangePalette function"]
---

# Animating a Palette

The following example animates a palette by using the [**DrawDibRealize**](drawdibrealize.md), [**DrawDibChangePalette**](drawdibchangepalette.md), and [**DrawDibDraw**](drawdibdraw.md) functions.

You can change the colors of a bitmap by using the [**DrawDibBegin**](drawdibbegin.md) function in combination with [**DrawDibChangePalette**](drawdibchangepalette.md). First, to allow palette changes, specify the DDF\_ANIMATE flag in the call to **DrawDibBegin**. Second, set the color table values from the palette entries by using **DrawDibChangePalette**.

For example, if *lppe* is an address of the [PALETTEENTRY](http://go.microsoft.com/fwlink/p/?linkid=16938) array containing the new colors, and *lpbi* is the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd318229) structure used in [**DrawDibBegin**](drawdibbegin.md) or [**DrawDibDraw**](drawdibdraw.md), the following fragment updates the DIB color table.


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

 

 




