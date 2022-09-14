---
title: TVM_SETUNICODEFORMAT message (Commctrl.h)
description: TVM_SETUNICODEFORMAT message - Sets the Unicode character format flag for the control.
ms.assetid: e4b58ae5-6217-4a2e-80e5-3ba9e578859a
keywords:
- TVM_SETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETUNICODEFORMAT message

Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. You can send this message explicitly or use the [**TreeView\_SetUnicodeFormat**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setunicodeformat) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Determines the character set that is used by the control. If this value is nonzero, the control will use Unicode characters. If this value is zero, the control will use ANSI characters.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous Unicode format flag for the control.

## Remarks

See the remarks for [**CCM\_SETUNICODEFORMAT**](ccm-setunicodeformat.md) for a discussion of this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETUNICODEFORMAT**](tvm-getunicodeformat.md)
</dt> </dl>

 

 





