---
description: Creates an instance of an ID3DXFile object.
ms.assetid: c086cb66-b1dc-4180-b966-e9a3b1f36f22
title: D3DXFileCreate function (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFileCreate
api_type: 
- LibDef
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# D3DXFileCreate function

Creates an instance of an [**ID3DXFile**](id3dxfile.md) object.

## Syntax


```C++
HRESULT STDAPICALLTYPE D3DXFileCreate(
   ID3DXFile **lplpDirectXFile
);
```



## Parameters

<dl> <dt>

*lplpDirectXFile* 
</dt> <dd>

Type: **[**ID3DXFile**](id3dxfile.md)\*\***

Address of a pointer to an [**ID3DXFile**](id3dxfile.md) interface, representing the created .x file object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: E\_POINTER, E\_OUTOFMEMORY.

## Remarks

After using this function, use [**RegisterTemplates**](id3dxfile--registertemplates.md) or [**RegisterEnumTemplates**](id3dxfile--registerenumtemplates.md) to register templates, [**CreateEnumObject**](id3dxfile--createenumobject.md) to create an enumerator object, or [**CreateSaveObject**](id3dxfile--createsaveobject.md) to create a save object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX X File Functions](dx9-graphics-reference-d3dx-x-file-functions.md)
</dt> <dt>

[**CreateEnumObject**](id3dxfile--createenumobject.md)
</dt> <dt>

[**CreateSaveObject**](id3dxfile--createsaveobject.md)
</dt> <dt>

[**RegisterEnumTemplates**](id3dxfile--registerenumtemplates.md)
</dt> <dt>

[**RegisterTemplates**](id3dxfile--registertemplates.md)
</dt> </dl>

 

 




