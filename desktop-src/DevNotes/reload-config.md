---
Description: 'Reloads an IME configuration from the HKCU registry, in Japanese IME only.'
ms.assetid: '171c31ad-c925-4e18-b458-d9abf52dae9a'
title: 'reload\_config function'
---

# reload\_config function

Reloads an IME configuration from the HKCU registry, in Japanese IME only.

## Syntax


```C++
BOOL reload_config(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Remarks

If no registry value is present in HKCU, the **reload\_config** function writes initial data to the registry.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imejpknl.dll; </dt> <dt>Imejp98k.dll</dt> </dl> |



 

 




