---
title: Unpremultiply effect
description: Use this effect to convert an image from premultiplied alpha to unpremultiplied alpha.
ms.assetid: A4FAF899-81DA-4BDA-98B4-DE63EC1664F5
keywords:
- unpremultiply effect
ms.topic: article
ms.date: 05/31/2018
---

# Unpremultiply effect

Use this effect to convert an image from premultiplied alpha to unpremultiplied alpha. The effect replaces each input pixel `P = {R, G, B, A}` with `P' = {R/A, G/A, B/A, A}` in the output.

This effect has no properties.

The CLSID for this effect is CLSID\_D2D1Unpremultiply.

## Output bitmap

The output bitmap size is the same as the input bitmap size.

## Requirements



| Requirement | Value |
|--------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects.h                                                                      |
| Library                  | d2d1.lib, dxguid.lib                                                               |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> </dl>

 

 
