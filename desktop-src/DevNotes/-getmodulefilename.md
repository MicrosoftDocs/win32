---
description: Gets the module path.
ms.assetid: ff632357-8d4a-4de4-a69a-0be9e380639d
title: '_GetModuleFileName function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _GetModuleFileName
api_type: 
- DllExport
api_location: 
- Msmdun80.dll
- Sqlunirl.dll
---

# \_GetModuleFileName function

\[This function is a wrapper over the **GetModuleFileName** function. This function may be altered or unavailable in the future. Applications should call **GetModuleFileName** directly.\]

Gets the module path. See [**GetModuleFileName**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea).

## Syntax


```C++
DWORD _GetModuleFileName(
    ...
);
```



## Parameters

<dl> <dt>

*...* 
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msmdun80.dll; </dt> <dt>Sqlunirl.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetModuleFileName**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea)
</dt> </dl>

 

 
