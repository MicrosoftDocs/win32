---
description: The LookupByteSetString function returns the string corresponding to the specified value of a labeled set.
ms.assetid: 295891f9-dc8d-4dbe-aac9-7d0a96993cfa
title: LookupByteSetString function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LookupByteSetString
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LookupByteSetString function

The **LookupByteSetString** function returns the string corresponding to the specified value of a labeled set.

## Syntax


```C++
LPBYTE WINAPI LookupByteSetString(
   LPSET lpSet,
   BYTE  Value
);
```



## Parameters

<dl> <dt>

*lpSet* 
</dt> <dd>

Pointer to a labeled set, from which you can extract the value's label.

</dd> <dt>

*Value* 
</dt> <dd>

Value of a labeled set.

</dd> </dl>

## Return value

If the function is successful, the return value is a string corresponding to the value provided.

If the function is unsuccessful, the return value is **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




