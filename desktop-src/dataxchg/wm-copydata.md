---
title: WM_COPYDATA message (Winuser.h)
description: An application sends the WM\_COPYDATA message to pass data to another application.
ms.assetid: d937a260-9fd2-4450-a762-20120f589ab1
keywords:
- WM_COPYDATA message Data Exchange
topic_type:
- apiref
api_name:
- WM_COPYDATA
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_COPYDATA message

An application sends the **WM\_COPYDATA** message to pass data to another application.


```C++
#define WM_COPYDATA                     0x004A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window passing the data.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**COPYDATASTRUCT**](/windows/win32/api/winuser/ns-winuser-copydatastruct) structure that contains the data to be passed.

</dd> </dl>

## Return value

If the receiving application processes this message, it should return **TRUE**; otherwise, it should return **FALSE**.

## Remarks

The data being passed must not contain pointers or other references to objects not accessible to the application receiving the data.

While this message is being sent, the referenced data must not be changed by another thread of the sending process.

The receiving application should consider the data read-only. The *lParam* parameter is valid only during the processing of the message. The receiving application should not free the memory referenced by *lParam*. If the receiving application must access the data after [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) returns, it must copy the data into a local buffer.

## Examples

For an example, see [Using Data Copy](using-data-copy.md).

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

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

[**COPYDATASTRUCT**](/windows/win32/api/winuser/ns-winuser-copydatastruct)
</dt> </dl>

 

