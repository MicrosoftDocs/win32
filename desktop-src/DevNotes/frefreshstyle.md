---
description: Reloads color settings from registry.
ms.assetid: 1F2EE08A-4193-4F0C-BE4F-0551FA71CFA8
title: FRefreshStyle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FRefreshStyle
api_type: 
- DllExport
api_location: 
- Imeshare.dll
---

# FRefreshStyle function

Reloads color settings from registry.

## Syntax


```C++
BOOL __cdecl FRefreshStyle(void);
```



## Parameters

This function has no parameters.

## Return value

Returns TRUE on success; otherwise, FALSE.

## Remarks

This function is not associated with an import library or header file; it must be called using the [**LoadLibrary**](-loadlibrary.md) and [**GetProcAddress**](-getprocaddress-.md) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetProcAddress**](-getprocaddress-.md)
</dt> <dt>

[**LoadLibrary**](-loadlibrary.md)
</dt> </dl>

 

 




