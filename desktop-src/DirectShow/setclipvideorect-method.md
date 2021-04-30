---
description: The SetClipVideoRect method zooms the video display to the specified subrectangle.
ms.assetid: 3940a382-8d53-4ff9-b024-38de1aa00f54
title: SetClipVideoRect Method
ms.topic: reference
ms.date: 05/31/2018
---

# SetClipVideoRect Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SetClipVideoRect` method zooms the video display to the specified subrectangle.

``` syntax
MSWebDVD.SetClipVideoRect(oRect)
```

## Parameters

<dl> <dt>

<span id="oRect"></span><span id="orect"></span><span id="ORECT"></span>*oRect*
</dt> <dd>

Specifies a [DVDRect](dvdrect-object.md) object, which contains the clipping rectangle.

</dd> </dl>

## Return Value

No return value.

## Remarks

When you set a new clipping rectangle, the object enlarges that area to fit within the application's overall display dimensions. This creates the effect zooming in on a particular area of the screen. To specify the rectangle, create a new [DVDRect](dvdrect-object.md) object and fill in its properties.

The most common rectangle for video display is 720 x 540.

## See also

<dl> <dt>

[**GetClipVideoRect**](getclipvideorect-method.md)
</dt> </dl>

 

 



