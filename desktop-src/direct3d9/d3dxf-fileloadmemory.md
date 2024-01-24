---
description: Identifies memory data.
ms.assetid: 0ec0597f-d83a-4c1e-b993-30f0bbd64e6b
title: D3DXF_FILELOADMEMORY structure (D3dx9xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXF_FILELOADMEMORY
api_type: 
- HeaderDef
api_location: 
- d3dx9xof.h
---

# D3DXF\_FILELOADMEMORY structure

Identifies memory data.

## Syntax


```C++
typedef struct D3DXF_FILELOADMEMORY {
  LPCVOID lpMemory;
  SIZE_T  dSize;
} D3DXF_FILELOADMEMORY, *LPD3DXF_FILELOADMEMORY;
```



## Members

<dl> <dt>

**lpMemory**
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

</dd> <dd>

Pointer to a block of memory to be loaded.

</dd> <dt>

**dSize**
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)**

</dd> <dd>

Size of the block of memory to be loaded, in bytes.

</dd> </dl>

## Remarks

This structure identifies data to be loaded from memory when an application uses the [**CreateEnumObject**](id3dxfile--createenumobject.md) method and specifies the D3DXF\_FILELOAD\_FROMMEMORY flag.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9xof.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX X File Structures](dx9-graphics-reference-d3dx-x-file-structures.md)
</dt> </dl>

 

 
