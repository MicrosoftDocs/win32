---
title: TB_CHANGEBITMAP message (Commctrl.h)
description: Changes the bitmap for a button in a toolbar.
ms.assetid: 112b6f4e-6034-4e13-8b2f-b8411a351fbd
keywords:
- TB_CHANGEBITMAP message Windows Controls
topic_type:
- apiref
api_name:
- TB_CHANGEBITMAP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_CHANGEBITMAP message

Changes the bitmap for a button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button that is to receive a new bitmap.

</dd> <dt>

*lParam* 
</dt> <dd>

Zero-based index of an image in the toolbar's image list. The system displays the specified image in the button. Set this parameter to I\_IMAGECALLBACK, and the toolbar will send the [**TBN\_GETDISPINFO**](tbn-getdispinfo.md) notification to retrieve the image index when it is needed.

[Version 5.81](common-control-versions.md). Set this parameter to I\_IMAGENONE to indicate that the button does not have an image. The button layout will not include any space for a bitmap, only text.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





