---
description: The Zoom method zooms the video display in or out, centered on a given set of screen coordinates.
ms.assetid: 050f1264-8fbe-4322-970c-184275d5b219
title: Zoom Method
ms.topic: reference
ms.date: 05/31/2018
---

# Zoom Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Zoom` method zooms the video display in or out, centered on a given set of screen coordinates.

``` syntax
MSWebDVD.Zoom(iXPos, iYPos, iZoomRatio)
```

## Parameters

<dl> <dt>

<span id="iXPos"></span><span id="ixpos"></span><span id="IXPOS"></span>*iXPos*
</dt> <dd>

Specifies the x-coordinate at the center of the rectangular zoom area as an Integer.

</dd> <dt>

<span id="iYPos"></span><span id="iypos"></span><span id="IYPOS"></span>*iYPos*
</dt> <dd>

Specifies the y-coordinate at the center of the rectangle to be zoomed as an Integer.

</dd> <dt>

<span id="iZoomRatio"></span><span id="izoomratio"></span><span id="IZOOMRATIO"></span>*iZoomRatio*
</dt> <dd>

Specifies the magnification factor applied to the current zoom value as an Integer. The total maximum value depends on what the hardware overlay can support; this is typically a factor of 32 to 64 times the original size.

</dd> </dl>

## Return Value

No return value.

## Remarks

The new zoom ratio stays in effect until it is restored to the original size or changed again. In other words, two calls to this method specifying an *iZoomRatio* of two will result in a zoom ratio four times larger than the original video size. If the user tries to zoom beyond what the hardware can support, this method will succeed but do nothing.

The [**SetClipVideoRect**](setclipvideorect-method.md) method is another way to zoom in; the only difference between the two methods is the way in which the zoom rectangle is specified.

 

 



