---
description: Contains basic module information.
ms.assetid: 5cdb0b11-8bd3-46d2-b214-85cdb2f274a7
title: AUX_MODULE_BASIC_INFO structure (Aux\_klib.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AUX_MODULE_BASIC_INFO
api_type: 
- HeaderDef
api_location: 
- Aux_klib.h
---

# AUX\_MODULE\_BASIC\_INFO structure

Contains basic module information.

## Syntax


```C++
typedef struct _AUX_MODULE_BASIC_INFO {
  PVOID ImageBase;
} AUX_MODULE_BASIC_INFO, *PAUX_MODULE_BASIC_INFO;
```



## Members

<dl> <dt>

**ImageBase**
</dt> <dd>

The base address of the module within the kernel's address space.

</dd> </dl>

## Remarks

The object library that implements this API can be downloaded from [here](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Auxiliary API library version 1.0 or later<br/>                          |
| Header<br/>          | <dl> <dt>Aux\_klib.h</dt> </dl> |



## See also

<dl> <dt>

[**AuxKlibQueryModuleInformation**](auxklibquerymoduleinformation-func.md)
</dt> </dl>

 

 




