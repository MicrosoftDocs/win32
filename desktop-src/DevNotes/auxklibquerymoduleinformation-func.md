---
description: Retrieves information about the currently loaded set of modules for the system.
ms.assetid: d3dc57e3-2c42-46cb-9af0-5f06bff60ad9
title: AuxKlibQueryModuleInformation function (Aux\_klib.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuxKlibQueryModuleInformation
api_type: 
- LibDef
api_location: 
- Aux_klib.lib
---

# AuxKlibQueryModuleInformation function

Retrieves information about the currently loaded set of modules for the system.

## Syntax


```C++
NTSTATUS _stdcall AuxKlibQueryModuleInformation(
  _Inout_   PULONG BufferSize,
  _In_      ULONG  ElementSize,
  _Out_opt_ PVOID  QueryInfo
);
```



## Parameters

<dl> <dt>

*BufferSize* \[in, out\]
</dt> <dd>

On input, the size of the *QueryInfo* buffer, in bytes. On output, receives the actual required size. Because the system module list can change between calls, this value can also change between calls.

</dd> <dt>

*ElementSize* \[in\]
</dt> <dd>

The size, in bytes, of an array element. This size determines the format of the output.

</dd> <dt>

*QueryInfo* \[out, optional\]
</dt> <dd>

A pointer to a buffer that receives the module information. This information is returned in an array whose elements are one of the following structures: [**AUX\_MODULE\_BASIC\_INFO**](aux-module-basic-info-struct.md) or [**AUX\_MODULE\_EXTENDED\_INFO**](aux-module-extended-info-struct.md). The specific structure used depends on the specified element size.

If this parameter is **NULL**, the function returns the required buffer size.

</dd> </dl>

## Return value

If the function succeeds, the return value is STATUS\_SUCCESS.

If the function fails, the return value can be one of the status codes defined in Ntstatus.h, which is available in the WDK.

## Remarks

You must call the [**AuxKlibInitialize**](auxklibinitialize-func.md) function before calling this function.

The object library that implements this API can be downloaded from [here](https://www.microsoft.com/?ref=go).

## Requirements



| Requirement | Value |
|----------------------------|------------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Auxiliary API library version 1.0 or later<br/>                            |
| Header<br/>          | <dl> <dt>Aux\_klib.h</dt> </dl>   |
| Library<br/>         | <dl> <dt>Aux\_klib.lib</dt> </dl> |



## See also

<dl> <dt>

[**AuxKlibInitialize**](auxklibinitialize-func.md)
</dt> <dt>

[**AUX\_MODULE\_BASIC\_INFO**](aux-module-basic-info-struct.md)
</dt> <dt>

[**AUX\_MODULE\_EXTENDED\_INFO**](aux-module-extended-info-struct.md)
</dt> </dl>

 

 




