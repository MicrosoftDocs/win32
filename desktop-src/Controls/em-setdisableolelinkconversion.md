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

The context passed to the callback function. May be NULL.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function that queries the application if the linked object in OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to **IStorage**.

</dd> </dl>

## Return value

If the return value is S_OK, the linked object will be converted. If the return value is other than S_OK, the linked object will be disabled.

## Remarks

This message is not defined in a SDK header, so you must specify the value representing the message, `(WM_USER + 404)`, instead.


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client| Minimum Supported Client| Windows 10 RTM (with Oct 2023 security update or later) |
| Minimum supported server| Minimum Supported server| Windows Server 2008 (with Oct 2023 security update or later) |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also


 

 





