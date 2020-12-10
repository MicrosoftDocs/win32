---
title: TB_GETBITMAPFLAGS message (Commctrl.h)
description: Retrieves the flags that describe the type of bitmap to be used.
ms.assetid: 64a66fe6-1446-424c-a0c6-388da6a7b081
keywords:
- TB_GETBITMAPFLAGS message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETBITMAPFLAGS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETBITMAPFLAGS message

Retrieves the flags that describe the type of bitmap to be used.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **DWORD** value that describes the type of bitmap that should be used. If this return value has the TBBF\_LARGE flag set, applications should use large bitmaps (24 x 24); otherwise, applications should use small bitmaps (16 x 16). All other bits are reserved.

## Remarks

The value returned by **TB\_GETBITMAPFLAGS** is only advisory. The toolbar control recommends large or small bitmaps based upon whether the user has chosen large or small fonts.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





