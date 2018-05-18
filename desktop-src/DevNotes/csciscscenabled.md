---
Description: 'Determines whether Offline Files is enabled.'
ms.assetid: 'c7d3173d-ed51-4de6-ad07-4c5e6906b0f4'
title: CSCIsCSCEnabled function
---

# CSCIsCSCEnabled function

\[This function is not supported and should not be used.\]

Determines whether Offline Files is enabled.

## Syntax


```C++
BOOL WINAPI CSCIsCSCEnabled(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **TRUE** if Offline Files is enabled and **FALSE** otherwise.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



## See also

<dl> <dt>

[**CSCQueryDatabaseStatus**](cscquerydatabasestatus.md)
</dt> </dl>

 

 




