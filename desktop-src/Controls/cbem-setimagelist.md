---
title: CBEM_SETIMAGELIST message (Commctrl.h)
description: Sets an image list for a ComboBoxEx control.
ms.assetid: a4a8ed61-a532-4cf8-8291-c157ab0e7f31
keywords:
- CBEM_SETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_SETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_SETIMAGELIST message

Sets an image list for a ComboBoxEx control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the image list to be set for the control.

</dd> </dl>

## Return value

Returns the handle to the image list previously associated with the control, or returns **NULL** if no image list was previously set.

## Remarks

> [!IMPORTANT]
> The height of images in your image list might change the size requirements of the ComboBoxEx control. It is recommended that you resize the control after sending this message to ensure that it is displayed properly.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





