---
title: EM_DISPLAYBAND message (Richedit.h)
description: Displays a portion of the contents of a rich edit control, as previously formatted for a device using the EM\_FORMATRANGE message.
ms.assetid: 845513d0-f32b-418c-8255-a5caf2d56215
keywords:
- EM_DISPLAYBAND message Windows Controls
topic_type:
- apiref
api_name:
- EM_DISPLAYBAND
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_DISPLAYBAND message

Displays a portion of the contents of a rich edit control, as previously formatted for a device using the [**EM\_FORMATRANGE**](em-formatrange.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure specifying the display area of the device.

</dd> </dl>

## Return value

If the operation succeeds, the return value is **TRUE**.

If the operation fails, the return value is **FALSE**.

## Remarks

Text and Component Object Model (COM) objects are clipped by the rectangle. The application does not need to set the clipping region.

Banding is the process by which a single page of output is generated using one or more separate rectangles, or bands. When all bands are placed on the page, a complete image results. This approach is often used by raster printers that do not have sufficient memory or ability to image a full page at one time. Banding devices include most dot matrix printers as well as some laser printers.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[Printing Rich Edit Controls](printing-rich-edit-controls.md)
</dt> </dl>

 

