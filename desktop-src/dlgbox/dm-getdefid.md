---
title: DM_GETDEFID message (Winuser.h)
description: Retrieves the identifier of the default push button control for a dialog box.
ms.assetid: 9f00a494-f5a2-4c4e-a9fc-2220d9326eb9
keywords:
- DM_GETDEFID message Dialog Boxes
topic_type:
- apiref
api_name:
- DM_GETDEFID
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DM\_GETDEFID message

Retrieves the identifier of the default push button control for a dialog box.


```C++
#define WM_USER              0x0400
#define DM_GETDEFID         (WM_USER+0)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

If a default push button exists, the high-order word of the return value contains the value **DC\_HASDEFID** and the low-order word contains the control identifier. Otherwise, the return value is zero.

## Remarks

The [**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw) function processes this message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw)
</dt> <dt>

[**DM\_SETDEFID**](dm-setdefid.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> </dl>

 

 





