---
description: Retrieves a child object in this file data object.
ms.assetid: 0c4f1efa-f096-443d-a482-a3c5a9138c3d
title: ID3DXFileData::GetChild method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileData.GetChild
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileData::GetChild method

Retrieves a child object in this file data object.

## Syntax


```C++
HRESULT GetChild(
  [in] SIZE_T        uiChild,
  [in] ID3DXFileData **ppChild
);
```



## Parameters

<dl> <dt>

*uiChild* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)**

ID of the child object to retrieve.

</dd> <dt>

*ppChild* \[in\]
</dt> <dd>

Type: **[**ID3DXFileData**](id3dxfiledata.md)\*\***

Address of a pointer to receive the child object's interface pointer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DXFERR\_BADVALUE, D3DXFERR\_NOMOREOBJECTS.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 
