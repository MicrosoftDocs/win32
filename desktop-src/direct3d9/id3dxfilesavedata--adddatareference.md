---
description: Adds a data reference as a child of this ID3DXFileSaveData file data node. The data reference points to a file data object.
ms.assetid: 75bfe91e-15ea-41f3-b1f7-071fb7f0093f
title: ID3DXFileSaveData::AddDataReference method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.AddDataReference
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::AddDataReference method

Adds a data reference as a child of this [**ID3DXFileSaveData**](id3dxfilesavedata.md) file data node. The data reference points to a file data object.

## Syntax


```C++
HRESULT AddDataReference(
  [in]       LPCSTR szName,
  [in] const GUID   *pId
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the name of the data object to add by reference. Specify **NULL** if the data object does not have a name.

</dd> <dt>

*pId* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to a GUID representing the data object to add by reference. If **NULL**, a reference will be added that points to the data object with the name given by szName.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADOBJECT, D3DXFERR\_BADVALUE, E\_OUTOFMEMORY.

## Remarks

The file data object being referenced must have either a name or a GUID. The file data object must also derive from a different parent [**ID3DXFileSaveData**](id3dxfilesavedata.md) object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 
