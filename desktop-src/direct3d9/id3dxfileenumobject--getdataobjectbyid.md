---
Description: 'Retrieves the data object that has the specified GUID.'
ms.assetid: 'c3d598bd-0646-4f99-8517-4475ef7cd8c9'
title: 'ID3DXFileEnumObject::GetDataObjectById method'
---

# ID3DXFileEnumObject::GetDataObjectById method

Retrieves the data object that has the specified GUID.

## Syntax


```C++
HRESULT GetDataObjectById(
  [in]  REFGUID        rguid,
  [out] LPD3DXFILEDATA *ppDataObj
);
```



## Parameters

<dl> <dt>

*rguid* \[in\]
</dt> <dd>

Type: **[REFGUID](http://go.microsoft.com/?linkid=9742306)**

Reference to the requested GUID.

</dd> <dt>

*ppDataObj* \[out\]
</dt> <dd>

Type: **[**LPD3DXFILEDATA**](id3dxfiledata.md)\***

Address of a pointer to an [**ID3DXFileData**](id3dxfiledata.md) interface, representing the returned file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following:DXFILEERR\_BADVALUE, DXFILEERR\_NOTFOUND.

## Remarks

Obtain the GUID rguid of the current file data object with the [**ID3DXFileData::GetId**](id3dxfiledata--getid.md) method.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileEnumObject](id3dxfileenumobject.md)
</dt> </dl>

 

 




