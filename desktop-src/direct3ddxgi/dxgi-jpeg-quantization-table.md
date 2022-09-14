---
description: Describes a JPEG quantization table.
ms.assetid: DE1AAB15-B0B8-4594-BBCE-5F8EE5CE0AF7
title: DXGI_JPEG_QUANTIZATION_TABLE structure (Dxgitype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXGI_JPEG_QUANTIZATION_TABLE
api_type: 
- HeaderDef
api_location: 
- dxgitype.h
---

# DXGI\_JPEG\_QUANTIZATION\_TABLE structure

Describes a JPEG quantization table.

## Syntax


```C++
typedef struct DXGI_JPEG_QUANTIZATION_TABLE {
  BYTE Elements[64];
} DXGI_JPEG_QUANTIZATION_TABLE;
```



## Members

<dl> <dt>

**Elements**
</dt> <dd>

An array of bytes containing the elements of the quantization table.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dxgitype.h</dt> </dl> |



## See also

<dl> <dt>

[DXGI Structures](d3d10-graphics-reference-dxgi-structures.md)
</dt> </dl>

 

 




