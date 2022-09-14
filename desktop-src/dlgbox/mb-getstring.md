---
title: MB_GetString function (User.h)
description: Returns strings for standard message box buttons.
ms.assetid: D2AF238D-F5A8-477D-BF47-0F5D4D68B27E
keywords:
- MB_GetString function Dialog Boxes
topic_type:
- apiref
api_name:
- MB_GetString
api_location:
- user32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MB\_GetString function

Returns strings for standard message box buttons.

## Syntax


```C++
LPCWSTR WINAPI MB_GetString(
   UINT wBtn
);
```



## Parameters

<dl> <dt>

*wBtn* 
</dt> <dd>

The id of the string to return. These are identified by the Dialog Box Command ID values listed in winuser.h.

</dd> </dl>

## Return value

The string, or NULL if not found.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>User.h</dt> </dl>     |
| Library<br/> | <dl> <dt>User32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>User32.dll</dt> </dl> |



 

 





