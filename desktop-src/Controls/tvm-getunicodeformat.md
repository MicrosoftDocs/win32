---
title: TVM_GETUNICODEFORMAT message (Commctrl.h)
description: Retrieves the Unicode character format flag for the control. You can send this message explicitly or use the TreeView\_GetUnicodeFormat macro.
ms.assetid: d95f61b6-9ec1-4471-b24b-efe141428747
keywords:
- TVM_GETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETUNICODEFORMAT message

Retrieves the Unicode character format flag for the control. You can send this message explicitly or use the [**TreeView\_GetUnicodeFormat**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getunicodeformat) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the Unicode format flag for the control. If this value is nonzero, the control is using Unicode characters. If this value is zero, the control is using ANSI characters.

## Remarks

See the remarks for [**CCM\_GETUNICODEFORMAT**](ccm-getunicodeformat.md) for a discussion of this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETUNICODEFORMAT**](tvm-setunicodeformat.md)
</dt> </dl>

 

 





