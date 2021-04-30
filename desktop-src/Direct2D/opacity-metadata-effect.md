---
title: Opacity metadata effect
description: You can use this effect to mark an area of an input image as opaque, so internal rendering optimizations to the graph are possible.
ms.assetid: 25B34A31-8533-4339-BBF7-2D7E5488E301
ms.topic: article
ms.date: 05/31/2018
---

# Opacity metadata effect

You can use this effect to mark an area of an input image as opaque, so internal rendering optimizations to the graph are possible.

> [!Note]  
> This effect doesn't modify the image itself to be opaque. It modifies data associated with the image so the renderer assumes the specified region is opaque.

 

The CLSID for this effect is CLSID\_D2D1OpacityMetadata.

## Effect properties



| Display name and index enumeration                                                 | Type and default value                                                             | Description                                                                                       |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| OutputRect<br/> D2D1\_OPACITYMETADATA\_PROP\_INPUT\_OPAQUE\_RECT <br/> | D2D1\_VECTOR\_4F<br/> (-FLT\_MAX, -FLT\_MAX, FLT\_MAX, FLT\_MAX) <br/> | The portion of the source image that is opaque. The default is the entire input image.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects.h                                                                      |
| Library                  | d2d1.lib, dxguid.lib                                                               |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> </dl>

 

