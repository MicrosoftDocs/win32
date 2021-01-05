---
description: Loads the Apphelp resource file.
ms.assetid: fca50e00-9324-410a-a572-69441f332593
title: SdbOpenApphelpResourceFile function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbOpenApphelpResourceFile
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbOpenApphelpResourceFile function

Loads the Apphelp resource file.

## Syntax


```C++
HMODULE WINAPI SdbOpenApphelpResourceFile(
  _In_opt_ LPCWSTR pwszACResourceFile
);
```



## Parameters

<dl> <dt>

*pwszACResourceFile* \[in, optional\]
</dt> <dd>

The path to the resource file. If this parameter is **NULL**, the local resource DLL is opened.

</dd> </dl>

## Return value

The function returns a handle to the opened resource file.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




