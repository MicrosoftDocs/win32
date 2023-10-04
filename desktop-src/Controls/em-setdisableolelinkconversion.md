---
title: EM_SETDISABLEOLELINKCONVERSION message (Richedit.h)
description: Tells a rich edit control if the linked object in the OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to IStorage.
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

Tells a rich edit control if the linked object in the OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to [IStorage](/windows/win32/api/objidl/nn-objidl-istorage).

```C++
#define EM_SETDISABLEOLELINKCONVERSION		(WM_USER + 404)
```

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The context the passed to the callback function. May be NULL.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function that queries the application if the linked object in OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to **IStorage**.

</dd> </dl>

## Return value

If the operation succeeds, the return value is a nonzero value.
If the operation fails, the return value is zero.


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | TBD                                            |
| Minimum supported server<br/> | TBD |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also


 

 





