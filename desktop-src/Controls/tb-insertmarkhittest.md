---
title: TB_INSERTMARKHITTEST message (Commctrl.h)
description: Retrieves the insertion mark information for a point in a toolbar.
ms.assetid: 65c64fd0-f089-4b1a-84e5-1a3e10aa7f5e
keywords:
- TB_INSERTMARKHITTEST message Windows Controls
topic_type:
- apiref
api_name:
- TB_INSERTMARKHITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_INSERTMARKHITTEST message

Retrieves the insertion mark information for a point in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Pointer to a [**POINT**](/windows/win32/api/windef/ns-windef-point) structure that contains the hit test coordinates, relative to the client area of the toolbar.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBINSERTMARK**](/windows/desktop/api/Commctrl/ns-commctrl-tbinsertmark) structure that receives the insertion mark information.

</dd> </dl>

## Return value

Returns nonzero if the point is an insertion mark, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

