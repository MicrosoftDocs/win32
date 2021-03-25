---
description: Initializes the Aux\_klib library.
ms.assetid: 516bb359-d3a3-415b-90af-09e544366a12
title: AuxKlibInitialize function (Aux\_klib.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuxKlibInitialize
api_type: 
- LibDef
api_location: 
- Aux_klib.lib
---

# AuxKlibInitialize function

Initializes the Aux\_klib library. This function must be called before any other function in the library can be called.

## Syntax


```C++
NTSTATUS _stdcall AuxKlibInitialize(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is STATUS\_SUCCESS.

If the function fails, the return value can be one of the status codes defined in Ntstatus.h, which is available in the WDK.

## Remarks

The object library that implements this API can be downloaded from [here](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|----------------------------|------------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Auxiliary API library version 1.0 or later<br/>                            |
| Header<br/>          | <dl> <dt>Aux\_klib.h</dt> </dl>   |
| Library<br/>         | <dl> <dt>Aux\_klib.lib</dt> </dl> |



## See also

<dl> <dt>

[**AuxKlibQueryModuleInformation**](auxklibquerymoduleinformation-func.md)
</dt> </dl>

 

 




