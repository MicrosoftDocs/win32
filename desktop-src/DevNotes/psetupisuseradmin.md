---
Description: 'Indicates whether the current user is an administrator.'
ms.assetid: 'e759a6b9-19c3-4a2e-b8cf-1398037f88ee'
title: pSetupIsUserAdmin function
---

# pSetupIsUserAdmin function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Indicates whether the current user is an administrator.

## Syntax


```C++
BOOL pSetupIsUserAdmin(void);
```



## Parameters

This function has no parameters.

## Return value

**TRUE** if the current user is an administrator, otherwise **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




