---
title: Drawing a Display Context
description: Drawing a Display Context
ms.assetid: c3328375-faa3-4b29-a155-8a25cc62269f
keywords:
- DrawDib,device context (DC)
- DrawDib,drawing DCs
- DrawDibRealize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing a Display Context

The following example prepares a DrawDib DC by using the [**DrawDibRealize**](/windows/win32/Vfw/nf-vfw-drawdibrealize?branch=master) function prior to displaying several images in a bitmap sequence.


```C++
hdc = GetDC(hwnd); 
DrawDibBegin(hdd, hdc, dxDest, dyDest, lpbi, dxSrc, dySrc, NULL); 
DrawDibRealize(hdd, hdc, fBackground); 
DrawDibDraw(hdd, hdc, xDst, yDst, dxDst, dyDst, lpbi, lpBits, 
    xSrc, ySrc, dxSrc, dySrc, DDF_SAME_DRAW|DDF_SAME_HDC); 
DrawDibDraw(hdd, hdc, xDst, yDst, dxDst, dyDst, lpbi, lpBits, 
    xSrc, ySrc, dxSrc, dySrc, DDF_SAME_DRAW|DDF_SAME_HDC); 
DrawDibDraw(hdd, hdc, xDst, yDst, dxDst, dyDst, lpbi, lpBits, 
    xSrc, ySrc, dxSrc, dySrc, DDF_SAME_DRAW|DDF_SAME_HDC); 
ReleaseDC(hwnd, hdc); 

```



## Related topics

<dl> <dt>

[Using DrawDib](using-drawdib.md)
</dt> </dl>

 

 




