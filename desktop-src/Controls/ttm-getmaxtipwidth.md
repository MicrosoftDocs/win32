---
title: TTM_GETMAXTIPWIDTH message (Commctrl.h)
description: Retrieves the maximum width for a tooltip window.
ms.assetid: 0f0a5403-fe2e-4e5a-96c2-a435827a5fd7
keywords:
- TTM_GETMAXTIPWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- TTM_GETMAXTIPWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_GETMAXTIPWIDTH message

Retrieves the maximum width for a tooltip window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an **INT** value that represents the maximum tooltip width, in pixels. If no maximum width was set previously, the message returns -1.

## Remarks

The maximum tooltip width value does not indicate a tooltip window's actual width. Rather, if a tooltip string exceeds the maximum width, the control breaks the text into multiple lines, using spaces to determine line breaks. If the text cannot be segmented into multiple lines, it will be displayed on a single line. The length of this line may exceed the maximum tooltip width.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TTM\_SETMAXTIPWIDTH**](ttm-setmaxtipwidth.md)
</dt> </dl>

 

 





