---
description: Gets the length of time, in minutes, since the user's last activity.
ms.assetid: 2d1e68ad-6f65-4e64-afbf-505b2c9d3423
title: GetIdleMinutes function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetIdleMinutes
api_type: 
- DllExport
api_location: 
- Msidle.dll
---

# GetIdleMinutes function

\[This function is not supported and may be altered or unavailable in the future. Instead, use the **GetLastInputInfo** function.\]

Gets the length of time, in minutes, since the user's last activity.

## Syntax


```C++
DWORD WINAPI GetIdleMinutes(
   DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*dwReserved* 
</dt> <dd>

This parameter must be set to zero.

</dd> </dl>

## Return value

Returns the number of minutes since the user's last activity.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. This function is not exported by name; specify ordinal 8 when calling **GetProcAddress**.

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msidle.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetLastInputInfo**](/windows/win32/api/winuser/nf-winuser-getlastinputinfo)
</dt> </dl>

 

 
