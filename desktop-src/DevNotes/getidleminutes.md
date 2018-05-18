---
Description: 'Gets the length of time, in minutes, since the user''s last activity.'
ms.assetid: '2d1e68ad-6f65-4e64-afbf-505b2c9d3423'
title: GetIdleMinutes function
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions. This function is not exported by name; specify ordinal 8 when calling **GetProcAddress**.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msidle.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetLastInputInfo**](_win32_getlastinputinfo_cpp)
</dt> </dl>

 

 




