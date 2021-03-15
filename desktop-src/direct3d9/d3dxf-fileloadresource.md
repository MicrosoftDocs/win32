---
description: Identifies resource data.
ms.assetid: f2ace2ad-228f-4f76-ab31-16e045e09331
title: D3DXF_FILELOADRESOURCE structure (D3dx9xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXF_FILELOADRESOURCE
api_type: 
- HeaderDef
api_location: 
- d3dx9xof.h
---

# D3DXF\_FILELOADRESOURCE structure

Identifies resource data.

## Syntax


```C++
typedef struct D3DXF_FILELOADRESOURCE {
  HMODULE hModule;
  LPCSTR  lpName;
  LPCSTR  lpType;
} D3DXF_FILELOADRESOURCE, *LPD3DXF_FILELOADRESOURCE;
```



## Members

<dl> <dt>

**hModule**
</dt> <dd>

Type: **[**HMODULE**](../winprog/windows-data-types.md)**

</dd> <dd>

Handle of the module containing the resource to be loaded. If this member is **NULL**, the resource must be attached to the executable file that will use it.

</dd> <dt>

**lpName**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Pointer to a string specifying the name of the resource to be loaded. For example, if the resource is a mesh, this member should specify the name of the mesh file.

</dd> <dt>

**lpType**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Pointer to a string specifying the user-defined type identifying the resource.

</dd> </dl>

## Remarks

This structure identifies a resource to be loaded when an application uses the [**CreateEnumObject**](id3dxfile--createenumobject.md) method and specifies the [D3DXF\_FILELOAD\_FROMRESOURCE](d3dxf.md) flag.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9xof.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX X File Structures](dx9-graphics-reference-d3dx-x-file-structures.md)
</dt> </dl>

 

 
