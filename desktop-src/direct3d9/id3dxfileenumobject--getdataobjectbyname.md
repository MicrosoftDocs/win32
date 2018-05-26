---
Description: Retrieves the data object that has the specified name.
ms.assetid: ed53d871-24e8-4c51-8897-1055ef8a9af1
title: ID3DXFileEnumObjectGetDataObjectByName method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXFileEnumObject::GetDataObjectByName method

Retrieves the data object that has the specified name.

## Syntax


```C++
HRESULT GetDataObjectByName(
  [in]  LPCSTR        szName,
  [out] ID3DXFileData **ppObj
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to the requested name.

</dd> <dt>

*ppObj* \[out\]
</dt> <dd>

Type: **[**ID3DXFileData**](id3dxfiledata.md)\*\***

Address of a pointer to an [**ID3DXFileData**](id3dxfiledata.md) interface, representing the returned file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following:DXFILEERR\_BADVALUE, DXFILEERR\_NOTFOUND.

## Remarks

Obtain the name szName of the current file data object with the [**ID3DXFileData::GetName**](id3dxfiledata--getname.md) method.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileEnumObject](id3dxfileenumobject.md)
</dt> </dl>

 

 




