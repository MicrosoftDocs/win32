---
Description: 'Initializes IME Share.'
ms.assetid: '7f58564e-d660-4936-b74c-af4eb93e2442'
title: FInitIMEShare function
---

# FInitIMEShare function

Initializes IME Share.

## Syntax


```C++
BOOL __cdecl FInitIMEShare(void);
```



## Parameters

This function has no parameters.

## Return value

The function returns **TRUE** on success or **FALSE** otherwise.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

This function should be called before any other IME Share functions are called.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**EndIMEShare**](endimeshare.md)
</dt> </dl>

 

 




