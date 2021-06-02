---
description: Identifies resource data. Deprecated.
ms.assetid: acb379c7-ac80-412f-8891-d5917b3f8da4
title: DXFILELOADRESOURCE structure (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXFILELOADRESOURCE
api_type: 
- HeaderDef
api_location: 
- DXFile.h
---

# DXFILELOADRESOURCE structure

Identifies resource data. Deprecated.

## Syntax


```C++
typedef struct DXFILELOADRESOURCE {
  HMODULE hModule;
  LPCTSTR lpName;
  LPCTSTR lpType;
} DXFILELOADRESOURCE, *LPDXFILELOADRESOURCE;
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

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Pointer to a string specifying the name of the resource to be loaded. For example, if the resource is a mesh, this member should specify the name of the mesh file.

</dd> <dt>

**lpType**
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Pointer to a string specifying the user-defined type identifying the resource.

</dd> </dl>

## Remarks

This structure identifies a resource to be loaded when an application uses the [**CreateEnumObject**](idirectxfile--createenumobject.md) method and specifies DXFILELOAD\_FROMRESOURCE.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DXFile.h</dt> </dl> |



## See also

<dl> <dt>

[X File Structures](dx9-graphics-reference-x-file-structures.md)
</dt> <dt>

[**CreateEnumObject**](idirectxfile--createenumobject.md)
</dt> <dt>

[DXFILE Constants](dxfile.md)
</dt> </dl>

 

 
