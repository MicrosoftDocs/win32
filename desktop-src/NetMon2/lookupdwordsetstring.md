---
description: The LookupDwordSetString function returns the string corresponding to the specified value of a labeled set.
ms.assetid: ee2b1b7a-6b64-4c8c-a71d-de970b66d46e
title: LookupDwordSetString function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LookupDwordSetString
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LookupDwordSetString function

The **LookupDwordSetString** function returns the string corresponding to the specified value of a labeled set.

## Syntax


```C++
LPBYTE WINAPI LookupDwordSetString(
   LPSET lpSet,
   DWORD Value
);
```



## Parameters

<dl> <dt>

*lpSet* 
</dt> <dd>

Labeled set, from which you can extract the value's label.

</dd> <dt>

*Value* 
</dt> <dd>

Value of a labeled set.

</dd> </dl>

## Return value

If the function is successful, the return value is the string that corresponds to the specified value.

If the function is unsuccessful, the specified value is not in the set, the return value is **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




