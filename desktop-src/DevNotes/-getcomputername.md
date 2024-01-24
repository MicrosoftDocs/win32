---
description: Gets the computer name.
ms.assetid: 8b6fd61a-dd5a-46b8-920e-cc8a848732b6
title: '_GetComputerName function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _GetComputerName
api_type: 
- DllExport
api_location: 
- Msmdun80.dll
- Sqlunirl.dll
---

# \_GetComputerName function

\[This function is a wrapper over the **GetComputerName** function. This function may be altered or unavailable in the future. Applications should call **GetComputerName** directly.\]

Gets the computer name. See [**GetComputerName**](/windows/win32/api/winbase/nf-winbase-getcomputernamea).

## Syntax


```C++
BOOL _GetComputerName(
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

[**GetComputerName**](/windows/win32/api/winbase/nf-winbase-getcomputernamea)
</dt> </dl>

 

 
