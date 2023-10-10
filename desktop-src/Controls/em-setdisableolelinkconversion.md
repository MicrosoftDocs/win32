---
title: EM_SETDISABLEOLELINKCONVERSION message (Richedit.h)
description: Tells a rich edit control if the linked objects in the OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to IStorage.
keywords:
- EM_SETDISABLEOLELINKCONVERSION message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETDISABLEOLELINKCONVERSION
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/03/2023
---

# EM\_SETDISABLEOLELINKCONVERSION message

Tells a rich edit control if the linked objects in the OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to [IStorage](/windows/win32/api/objidl/nn-objidl-istorage).

```C++
#define EM_SETDISABLEOLELINKCONVERSION		(WM_USER + 404)
```

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A value of 1 indicates that the linked object in the OLESTREAM contained in the RTF should be disabled while converting OLESTREAM to IStorage. A value of 0 resets to the default behavior.

</dd> </dl>

## Return value

If the operation succeeds, the return value is a nonzero value.

If the operation fails, the return value is zero.



## Remarks

This message is not defined in a SDK header, so you must specify the value representing the message, `(WM_USER + 404)`, instead.


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client| Windows 10 RTM (with Oct 2023 security update or later) |
| Minimum supported server|  Windows Server 2008 (with Oct 2023 security update or later) |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also


 

 





