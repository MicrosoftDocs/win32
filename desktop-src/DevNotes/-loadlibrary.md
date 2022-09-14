---
description: Loads a library.
ms.assetid: 191fcbd8-4542-4cad-955e-6951f3005fc5
title: '_LoadLibrary function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _LoadLibrary
api_type: 
- DllExport
api_location: 
- Msmdun80.dll
- Sqlunirl.dll
---

# \_LoadLibrary function

\[This function is a wrapper over the **LoadLibrary** function. This function may be altered or unavailable in the future. Applications should call **LoadLibrary** directly.\]

Loads a library. See [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya).

## Syntax


```C++
HMODULE _LoadLibrary(
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

[**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> </dl>

 

 
