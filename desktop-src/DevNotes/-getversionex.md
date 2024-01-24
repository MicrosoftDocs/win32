---
description: Gets information about the operating system version.
ms.assetid: 1af2c320-6e0b-4692-858b-a2c921ed7ce7
title: '_GetVersionEx function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _GetVersionEx
api_type: 
- DllExport
api_location: 
- Msmdun80.dll
- Sqlunirl.dll
---

# \_GetVersionEx function

\[This function is a wrapper over the **GetVersionEx** function. This function may be altered or unavailable in the future. Applications should call **GetVersionEx** directly.\]

Gets information about the operating system version. See [**GetVersionEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa).

## Syntax


```C++
BOOL _GetVersionEx(
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

[**GetVersionEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa)
</dt> </dl>

 

 
