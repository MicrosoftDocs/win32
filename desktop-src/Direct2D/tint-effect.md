---
title: Tint effect
description: This effect tints the source image by multiplying the source image by the specified color. It has a single input.
ms.assetid: 8df72105-26ea-2dea-a4de-ef06902b7e0b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tint effect

This effect tints the source image by multiplying the source image by the specified color. It has a single input.

The CLSID for this effect is CLSID\_D2D1Tint.

## Effect Properties



| Display anme and index enumeration                    | Type and default value                              | Descripiton                                                      |
|-------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| ColorD2D1\_TINT\_PROP\_COLOR<br/>               | D2D1\_VECTOR\_4F(1.0f, 1.0f, 1.0f, 1.0f)<br/> | Colors from the source image are multiplied by this value.       |
| ClampOutputD2D1\_TINT\_PROP\_CLAMP\_OUTPUT<br/> | BOOLFALSE<br/>                                | Whether or not to clamp the output values to the range \[0, 1\]. |



 

## Requirements



|                          |                                                   |
|--------------------------|---------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 10 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_2.h                                  |
| Library                  | d2d1.lib, dxguid.lib                              |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/D2d1_1/?branch=master)
</dt> </dl>

 

 





