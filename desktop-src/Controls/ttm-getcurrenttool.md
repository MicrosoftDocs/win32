---
title: TTM_GETCURRENTTOOL message (Commctrl.h)
description: Retrieves the information for the current tool in a tooltip control.
ms.assetid: acb254cf-064c-4ed8-b488-a3138b648405
keywords:
- TTM_GETCURRENTTOOL message Windows Controls
topic_type:
- apiref
api_name:
- TTM_GETCURRENTTOOL
- TTM_GETCURRENTTOOLA
- TTM_GETCURRENTTOOLW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_GETCURRENTTOOL message

Retrieves the information for the current tool in a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure that receives information about the current tool. If this value is **NULL**, the return value indicates the existence of the current tool without actually retrieving the tool information. If this value is not **NULL**, the **cbSize** member of the **TOOLINFO** structure must be filled in before sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. If *lParam* is **NULL**, returns nonzero if a current tool exists, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_GETCURRENTTOOLW** (Unicode) and **TTM\_GETCURRENTTOOLA** (ANSI)<br/>     |



 

 





