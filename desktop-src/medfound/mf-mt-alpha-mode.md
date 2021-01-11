---
description: Specifies whether the alpha mode for color media video types is premultiplied or straight.
ms.assetid: A263C3F7-357B-426D-B38C-533F9F6A1262
title: MF_MT_ALPHA_MODE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_ALPHA\_MODE attribute

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Specifies whether the alpha mode for color media video types is premultiplied or straight.

## Data type

**UINT32**

## Remarks

This value can be cast to a [**DXGI\_ALPHA\_MODE**](/windows/win32/api/dxgi1_2/ne-dxgi1_2-dxgi_alpha_mode) value. If this attribute isn’t present, for backward compatibility, the value is **DXGI\_ALPHA\_MODE\_STRAIGHT** for video format supporting alpha channel, such as ARGB32, or **DXGI\_ALPHA\_MODE\_IGNORE** for video format without alpha channel, such as RGB32.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 
