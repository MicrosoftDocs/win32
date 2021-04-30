---
description: Reloads an IME configuration from the HKCU registry, in Japanese IME only.
ms.assetid: 171c31ad-c925-4e18-b458-d9abf52dae9a
title: reload_config function
ms.topic: reference
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imejpknl.dll; </dt> <dt>Imejp98k.dll</dt> </dl> |



 

 
