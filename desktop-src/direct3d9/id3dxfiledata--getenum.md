---
description: Retrieves the enumeration object in this file data object.
ms.assetid: 383560e2-1888-4e37-9883-2ddbcb101cf6
title: ID3DXFileData::GetEnum method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileData.GetEnum
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileData::GetEnum method

Retrieves the enumeration object in this file data object.

## Syntax


```C++
HRESULT GetEnum(
  [in] ID3DXFileEnumObject **ppObj
);
```



## Parameters

<dl> <dt>

*ppObj* \[in\]
</dt> <dd>

Type: **[**ID3DXFileEnumObject**](id3dxfileenumobject.md)\*\***

Address of a pointer to receive the enumeration object in this file data object.

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

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 




