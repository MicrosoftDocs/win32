---
title: EM_SETQUERYCONVERTOLELINKCALLBACK message (Richedit.h)
description: Gives a rich edit control a OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function that queries the application if linked object in OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to IStorage.
keywords:
- EM_SETQUERYCONVERTOLELINKCALLBACK message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETQUERYCONVERTOLELINKCALLBACK
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/03/2023
---

# EM\_SETQUERYCONVERTOLELINKCALLBACK message

Gives a rich edit control a OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function that queries the application if linked object in OLESTREAM contained in the RTF should be disabled or not while converting OLESTREAM to [IStorage](/windows/win32/api/objidl/nn-objidl-istorage).

```C++
#define EM_SETQUERYCONVERTOLELINKCALLBACK	(WM_USER + 403)
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

This message does not return a value.

## Remarks

This message is not defined in a SDK header, so you must specify the value representing the message, `(WM_USER + 403)`, instead.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client| Minimum Supported Client| Windows 10 RTM (with Oct 2023 security update or later) |
| Minimum supported server| Minimum Supported server| Windows Server 2008 (with Oct 2023 security update or later) |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also


 

 





