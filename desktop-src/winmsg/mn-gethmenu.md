---
description: Retrieves the menu handle for the current window.
ms.assetid: a2f6e917-39ff-42a3-8ff4-ce01db3ef9ea
title: MN_GETHMENU message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MN\_GETHMENU message

Retrieves the menu handle for the current window.


```C++
#define MN_GETHMENU                     0x01E1
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **HMENU**

If successful, the return value is the **HMENU** for the current window. If it fails, the return value is **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 




