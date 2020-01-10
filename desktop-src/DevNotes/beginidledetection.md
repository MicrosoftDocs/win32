---
Description: Begins monitoring inactivity.
ms.assetid: fed5e4ae-2c2b-4b00-9230-b71aec9335c8
title: BeginIdleDetection function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BeginIdleDetection
api_type: 
- DllExport
api_location: 
- Msidle.dll
---

# BeginIdleDetection function

\[This function is not supported and may be altered or unavailable in the future. Instead, use the **GetLastInputInfo** function.\]

Begins monitoring inactivity.

## Syntax


```C++
DWORD WINAPI BeginIdleDetection(
   _IDLECALLBACK pfnCallback,
   DWORD         dwIdleMin,
   DWORD         dwReserved
);
```



## Parameters

<dl> <dt>

*pfnCallback* 
</dt> <dd>

The function that is called when the idle state changes. This callback is defined as follows:

``` syntax
typedef void (WINAPI* _IDLECALLBACK) (DWORD dwState);

#define STATE_USER_IDLE_BEGIN       1
#define STATE_USER_IDLE_END         2
```

</dd> <dt>

*dwIdleMin* 
</dt> <dd>

The number of minutes of inactivity before the call is made to the callback function.

</dd> <dt>

*dwReserved* 
</dt> <dd>

This parameter must be set to zero.

</dd> </dl>

## Return value

Returns 0 if the function succeeds; otherwise, it returns an error code. For example, if *dwReserved* is anything other than 0, **ERROR\_INVALID\_DATA** is returned.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/library/ms683212(v=VS.85).aspx) functions. This function is not exported by name; specify ordinal 3 when calling **GetProcAddress**.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msidle.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetLastInputInfo**](https://msdn.microsoft.com/library/ms646302(v=VS.85).aspx)
</dt> </dl>

 

 




