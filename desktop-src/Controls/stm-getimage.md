---
title: STM_GETIMAGE message (Winuser.h)
description: An application sends an STM\_GETIMAGE message to retrieve a handle to the image (icon or bitmap) associated with a static control.
ms.assetid: eb5fe67a-09be-4c13-89c6-0e2f23e8c081
keywords:
- STM_GETIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- STM_GETIMAGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STM\_GETIMAGE message

An application sends an **STM\_GETIMAGE** message to retrieve a handle to the image (icon or bitmap) associated with a static control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the type of image to retrieve. This parameter can be one of the following values:



| Value                                                                                                                                                                     | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="IMAGE_BITMAP"></span><span id="image_bitmap"></span><dl> <dt>**IMAGE\_BITMAP**</dt> </dl>                | Bitmap.<br/>            |
| <span id="IMAGE_CURSOR"></span><span id="image_cursor"></span><dl> <dt>**IMAGE\_CURSOR**</dt> </dl>                | Cursor.<br/>            |
| <span id="IMAGE_ENHMETAFILE"></span><span id="image_enhmetafile"></span><dl> <dt>**IMAGE\_ENHMETAFILE**</dt> </dl> | Enhanced metafile.<br/> |
| <span id="IMAGE_ICON"></span><span id="image_icon"></span><dl> <dt>**IMAGE\_ICON**</dt> </dl>                      | Icon.<br/>              |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is a handle to the image, if any; otherwise, it is **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**STM\_SETIMAGE**](stm-setimage.md)
</dt> </dl>

 

 





