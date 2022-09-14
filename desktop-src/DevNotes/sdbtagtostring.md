---
description: Retrieves the display name of the specified TAG.
ms.assetid: e382d443-aab2-476c-90dd-7ab38e737f52
title: SdbTagToString function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbTagToString
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbTagToString function

Retrieves the display name of the specified TAG.

## Syntax


```C++
LPCTSTR WINAPI SdbTagToString(
  _In_ TAG tag
);
```



## Parameters

<dl> <dt>

*tag* \[in\]
</dt> <dd>

The TAG.

</dd> </dl>

## Return value

The function returns a pointer to the null-terminated string or "InvalidTag".

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**TAG**](tag.md)
</dt> </dl>

 

 




