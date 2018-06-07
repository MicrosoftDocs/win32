---
Description: The LookupWordSetString function returns the string corresponding to the requested value from a labeled set.
ms.assetid: e8d158a1-8544-4c10-b8e8-46888c1097e4
title: LookupWordSetString function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LookupWordSetString function

The **LookupWordSetString** function returns the string corresponding to the requested value from a labeled set.

## Syntax


```C++
LPBYTE WINAPI LookupWordSetString(
   LPSET lpSet,
   WORD  Value
);
```



## Parameters

<dl> <dt>

*lpSet* 
</dt> <dd>

Labeled set from which you extract the value's label.

</dd> <dt>

*Value* 
</dt> <dd>

Value of a labeled set.

</dd> </dl>

## Return value

If the function is successful, the return value is a string that corresponds to the requested value.

If the function is unsuccessful, the specified value is not in the set, the return value is **NULL**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




