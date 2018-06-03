---
Description: Reloads an IME configuration from the HKCU registry, in Japanese IME only.
ms.assetid: 171c31ad-c925-4e18-b458-d9abf52dae9a
title: reload\_config function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imejpknl.dll; </dt> <dt>Imejp98k.dll</dt> </dl> |



 

 




