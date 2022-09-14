---
title: CB_GETDROPPEDSTATE message (Winuser.h)
description: Determines whether the list box of a combo box is dropped down.
ms.assetid: a3f4e352-298d-45ea-a5a7-007f1fc1a387
keywords:
- CB_GETDROPPEDSTATE message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETDROPPEDSTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETDROPPEDSTATE message

Determines whether the list box of a combo box is dropped down.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If the list box is visible, the return value is **TRUE**; otherwise, it is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_SHOWDROPDOWN**](cb-showdropdown.md)
</dt> </dl>

 

 





