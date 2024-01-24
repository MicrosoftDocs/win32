---
description: Creates an instance of a DirectXFile object. Deprecated.
ms.assetid: c920d480-2557-491d-87ea-7eea1f470498
title: DirectXFileCreate function (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DirectXFileCreate
api_type: 
- DllExport
api_location: 
- d3dxof.dll
---

# DirectXFileCreate function

Creates an instance of a DirectXFile object. Deprecated.

## Syntax


```C++
HRESULT STDAPICALLTYPE DirectXFileCreate(
   LPDIRECTXFILE *lplpDirectXFile
);
```



## Parameters

<dl> <dt>

*lplpDirectXFile* 
</dt> <dd>

Type: **[**LPDIRECTXFILE**](idirectxfile.md)\***

Address of a pointer to an [**IDirectXFile**](idirectxfile.md) interface, representing the created DirectXFile object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: DXFILEERR\_BADALLOC, DXFILEERR\_BADVALUE.

## Remarks

After using this function, use [**RegisterTemplates**](idirectxfile--registertemplates.md) to register templates, [**CreateEnumObject**](idirectxfile--createenumobject.md) to create an enumerator object, or [**CreateSaveObject**](idirectxfile--createsaveobject.md) to create a save object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dxof.dll</dt> </dl> |



## See also

<dl> <dt>

[X File Functions](dx9-graphics-reference-x-file-functions.md)
</dt> <dt>

[**CreateEnumObject**](idirectxfile--createenumobject.md)
</dt> <dt>

[**CreateSaveObject**](idirectxfile--createsaveobject.md)
</dt> <dt>

[**RegisterTemplates**](idirectxfile--registertemplates.md)
</dt> </dl>

 

 




