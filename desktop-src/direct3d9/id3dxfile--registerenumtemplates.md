---
description: Registers custom templates, given an ID3DXFileEnumObject enumeration object.
ms.assetid: 1b0c71db-639b-4836-8a65-7d0a2ed3ba4f
title: ID3DXFile::RegisterEnumTemplates method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFile.RegisterEnumTemplates
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFile::RegisterEnumTemplates method

Registers custom templates, given an [**ID3DXFileEnumObject**](id3dxfileenumobject.md) enumeration object.

## Syntax


```C++
HRESULT RegisterEnumTemplates(
  [in] ID3DXFileEnumObject *pEnum
);
```



## Parameters

<dl> <dt>

*pEnum* \[in\]
</dt> <dd>

Type: **[**ID3DXFileEnumObject**](id3dxfileenumobject.md)\***

Pointer to an [**ID3DXFileEnumObject**](id3dxfileenumobject.md) enumeration object that contains templates.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK .

If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Remarks

When this method is called, it copies templates stored with the ID3DXFileEnumObject, representing the file, to the local template store of the [**ID3DXFile**](id3dxfile.md) object.

If an [**ID3DXFileEnumObject**](id3dxfileenumobject.md) pointer is not available, call the [**RegisterTemplates**](id3dxfile--registertemplates.md) method instead.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFile](id3dxfile.md)
</dt> <dt>

[**RegisterTemplates**](id3dxfile--registertemplates.md)
</dt> </dl>

 

 




