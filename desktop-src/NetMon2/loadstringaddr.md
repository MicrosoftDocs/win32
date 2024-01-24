---
description: The LoadStringAddr function transforms a string (such as &\#0034;157.54.32.45&\#0034;) and creates a DWORD address.
ms.assetid: 305e0072-b597-4cd5-975e-94103a1680aa
title: LoadStringAddr function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadStringAddr
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadStringAddr function

The **LoadStringAddr** function transforms a string (such as "157.54.32.45") and creates a **DWORD** address.

## Syntax


```C++
BOOL LoadStringAddr(
         DWORD *pAddress,
   const char  *str
);
```



## Parameters

<dl> <dt>

*pAddress* 
</dt> <dd>

Pointer to a **DWORD**.

</dd> <dt>

*str* 
</dt> <dd>

Pointer to a character string with x.x.x.x representation of an IP address (for example,127.0.0.1).

</dd> </dl>

## Return value

If the function is successful (the address name was found); the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




