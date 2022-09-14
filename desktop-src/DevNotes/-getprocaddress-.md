---
description: Gets the address of a function from a DLL.
ms.assetid: e425948c-5588-4a4f-994c-4e608af18439
title: '_GetProcAddress_ function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _GetProcAddress_
api_type: 
- DllExport
api_location: 
- Msmdun80.dll
- Sqlunirl.dll
---

# \_GetProcAddress\_ function

\[This function is a wrapper over the **GetProcAddress** function. This function may be altered or unavailable in the future. Applications should call **GetProcAddress** directly.\]

Gets the address of a function from a DLL. See [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress).

## Syntax


```C++
FARPROC _GetProcAddress_(
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

[**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)
</dt> </dl>

 

 
