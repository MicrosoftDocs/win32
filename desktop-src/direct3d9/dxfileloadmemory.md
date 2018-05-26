---
Description: Identifies memory data. Deprecated.
ms.assetid: fe791e13-d5de-425f-b68f-80db8b332cc6
title: DXFILELOADMEMORY structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DXFILELOADMEMORY structure

Identifies memory data. Deprecated.

## Syntax


```C++
typedef struct DXFILELOADMEMORY {
  LPVOID lpMemory;
  DWORD  dSize;
} DXFILELOADMEMORY, *LPDXFILELOADMEMORY;
```



## Members

<dl> <dt>

**lpMemory**
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

</dd> <dd>

Pointer to a block of memory to be loaded.

</dd> <dt>

**dSize**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Size of the block of memory to be loaded, in bytes.

</dd> </dl>

## Remarks

This structure identifies a resource to be loaded when an application uses the [**CreateEnumObject**](idirectxfile--createenumobject.md) method and specifies DXFILELOAD\_FROMMEMORY.

## Requirements



|                   |                                                                                     |
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

 

 




