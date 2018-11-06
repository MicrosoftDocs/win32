---
Description: Reloads an IME configuration from the HKCU registry, in Japanese IME only.
ms.assetid: 171c31ad-c925-4e18-b458-d9abf52dae9a
title: reload_config function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- reload_config
api_type: 
- DllExport
api_location: 
- Imejpknl.dll
- Imejp98k.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imejpknl.dll; </dt> <dt>Imejp98k.dll</dt> </dl> |



 

 




