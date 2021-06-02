---
UID: NS:directml.DML_SCALAR_UNION
title: DML_SCALAR_UNION
description: A union of scalar types.
helpviewer_keywords: ["DML_SCALAR_UNION","DML_SCALAR_UNION structure","direct3d12.dml_scalar_union","directml/DML_SCALAR_UNION"]
ms.topic: reference
tech.root: directml
ms.date: 10/30/2020
ms.keywords: DML_SCALAR_UNION, DML_SCALAR_UNION structure, direct3d12.dml_scalar_union, directml/DML_SCALAR_UNION
req.header: directml.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - DML_SCALAR_UNION
 - directml/DML_SCALAR_UNION
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - DirectML.h
api_name:
 - DML_SCALAR_UNION
---

# DML_SCALAR_UNION union (directml.h)
A union of scalar types.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
union DML_SCALAR_UNION {
  BYTE   Bytes[8];
  INT8   Int8;
  UINT8  UInt8;
  INT16  Int16;
  UINT16 UInt16;
  INT32  Int32;
  UINT32 UInt32;
  INT64  Int64;
  UINT64 UInt64;
  FLOAT  Float32;
  DOUBLE Float64;
};
```



## Members

`Bytes`

An 8-byte array.


`Int8`

An 8-bit signed integer.


`UInt8`

An 8-bit unsigned integer.


`Int16`

A 16-bit signed integer.


`UInt16`

A 16-bit unsigned integer.


`Int32`

A 32-bit signed integer.


`UInt32`

A 32-bit unsigned integer.


`Int64`

A 64-bit signed integer.


`UInt64`

A 64-bit unsigned integer.


`Float32`

A single precision floating-point number.


`Float64`

A double precision floating-point number.



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |