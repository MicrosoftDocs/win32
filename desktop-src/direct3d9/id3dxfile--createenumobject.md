---
description: Creates an enumerator object that will read a .x file.
ms.assetid: 86d05eab-601c-4beb-9dbe-c23fa524871c
title: ID3DXFile::CreateEnumObject method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFile.CreateEnumObject
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFile::CreateEnumObject method

Creates an enumerator object that will read a .x file.

## Syntax


```C++
HRESULT CreateEnumObject(
  [out] LPCVOID               pvSource,
  [in]  D3DXF_FILELOADOPTIONS loadflags,
  [out] ID3DXFileEnumObject   **ppEnumObj
);
```



## Parameters

<dl> <dt>

*pvSource* \[out\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

The data source. Either:

-   A file name
-   A [**D3DXF\_FILELOADMEMORY**](d3dxf-fileloadmemory.md) structure
-   A [**D3DXF\_FILELOADRESOURCE**](d3dxf-fileloadresource.md) structure

Depending on the value of loadflags.

</dd> <dt>

*loadflags* \[in\]
</dt> <dd>

Type: **[D3DXF\_FILELOADOPTIONS](d3dxf.md)**

Value that specifies the source of the data. This value can be one of the [D3DXF\_FILELOADOPTIONS](d3dxf.md) flags.

</dd> <dt>

*ppEnumObj* \[out\]
</dt> <dd>

Type: **[**ID3DXFileEnumObject**](id3dxfileenumobject.md)\*\***

Address of a pointer to an [**ID3DXFileEnumObject**](id3dxfileenumobject.md) interface, representing the created enumerator object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADVALUE, D3DXFERR\_PARSEERROR.

## Remarks

After using this method, use one of the [**ID3DXFileEnumObject**](id3dxfileenumobject.md) methods to retrieve a data object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFile](id3dxfile.md)
</dt> <dt>

[**ID3DXFileEnumObject**](id3dxfileenumobject.md)
</dt> </dl>

 

 
