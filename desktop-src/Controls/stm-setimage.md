---
title: STM_SETIMAGE message (Winuser.h)
description: An application sends an STM\_SETIMAGE message to associate a new image with a static control.
ms.assetid: d3e7c5d4-f621-40f6-9558-7fb699e8b489
keywords:
- STM_SETIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- STM_SETIMAGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STM\_SETIMAGE message

An application sends an **STM\_SETIMAGE** message to associate a new image with a static control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the type of image to associate with the static control. This parameter can be one of the following values:



| Value                                                                                                                                                                     | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="IMAGE_BITMAP"></span><span id="image_bitmap"></span><dl> <dt>**IMAGE\_BITMAP**</dt> </dl>                | Bitmap.<br/>            |
| <span id="IMAGE_CURSOR"></span><span id="image_cursor"></span><dl> <dt>**IMAGE\_CURSOR**</dt> </dl>                | Cursor.<br/>            |
| <span id="IMAGE_ENHMETAFILE"></span><span id="image_enhmetafile"></span><dl> <dt>**IMAGE\_ENHMETAFILE**</dt> </dl> | Enhanced metafile.<br/> |
| <span id="IMAGE_ICON"></span><span id="image_icon"></span><dl> <dt>**IMAGE\_ICON**</dt> </dl>                      | Icon.<br/>              |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the image to associate with the static control.

</dd> </dl>

## Return value

The return value is a handle to the image previously associated with the static control, if any; otherwise, it is **NULL**.

## Remarks

To associate an image with a static control, the control must have the proper style. The following table shows the style needed for each image type.



| Image type         | Static control style |
|--------------------|----------------------|
| IMAGE\_BITMAP      | SS\_BITMAP           |
| IMAGE\_CURSOR      | SS\_ICON             |
| IMAGE\_ENHMETAFILE | SS\_ENHMETAFILE      |
| IMAGE\_ICON        | SS\_ICON             |



 

> [!IMPORTANT]
>
> In version 6 of the Microsoft Win32 controls, a bitmap passed to a static control using the **STM\_SETIMAGE** message was the same bitmap returned by a subsequent **STM\_SETIMAGE** message. The client is responsible to delete any bitmap sent to a static control.
>
> With Windows XP, if the bitmap passed in the **STM\_SETIMAGE** message contains pixels with nonzero alpha, the static control takes a copy of the bitmap. This copied bitmap is returned by the next **STM\_SETIMAGE** message. The client code may independently track the bitmaps passed to the static control, but if it does not check and release the bitmaps returned from **STM\_SETIMAGE** messages, the bitmaps are leaked.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**STM\_GETIMAGE**](stm-getimage.md)
</dt> </dl>

 

 





