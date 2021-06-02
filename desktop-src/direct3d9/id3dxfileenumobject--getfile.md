---
description: Retrieves the ID3DXFile object.
ms.assetid: 832878c6-73a4-400a-af30-57112b172977
title: ID3DXFileEnumObject::GetFile method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileEnumObject.GetFile
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileEnumObject::GetFile method

Retrieves the [**ID3DXFile**](id3dxfile.md) object.

## Syntax


```C++
HRESULT GetFile(
  [out] ID3DXFile **ppFile
);
```



## Parameters

<dl> <dt>

*ppFile* \[out\]
</dt> <dd>

Type: **[**ID3DXFile**](id3dxfile.md)\*\***

Address of a pointer to an [**ID3DXFile**](id3dxfile.md) interface, representing the returned object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileEnumObject](id3dxfileenumobject.md)
</dt> </dl>

 

 




