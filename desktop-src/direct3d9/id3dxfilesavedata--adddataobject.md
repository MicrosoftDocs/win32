---
description: Adds a data object as a child of the ID3DXFileSaveData file data node.
ms.assetid: 47faad99-3ee8-4ca8-b8d7-413d4cd5b090
title: ID3DXFileSaveData::AddDataObject method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.AddDataObject
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::AddDataObject method

Adds a data object as a child of the [**ID3DXFileSaveData**](id3dxfilesavedata.md) file data node.

## Syntax


```C++
HRESULT AddDataObject(
  [in]               REFGUID           rguidTemplate,
  [in]               LPCSTR            szName,
  [in]         const GUID              *pId,
  [in]               SIZE_T            cbSize,
  [in]               LPCVOID           pvData,
  [in, retval]       ID3DXFileSaveData **ppObj
);
```



## Parameters

<dl> <dt>

*rguidTemplate* \[in\]
</dt> <dd>

Type: **[REFGUID](/openspecs/windows_protocols/ms-oaut/6e7d7108-c213-40bc-8294-ac13fe68fd50)**

GUID representing the data object's template.

</dd> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the name of the data object to add. Specify **NULL** if the object does not have a name.

</dd> <dt>

*pId* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to a GUID representing the data object. The data object must have been registered with [**ID3DXFile::RegisterTemplates**](id3dxfile--registertemplates.md) or [**ID3DXFile::RegisterEnumTemplates**](id3dxfile--registerenumtemplates.md). Specify **NULL** if the object does not have a GUID.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)**

Size of the data object, in bytes.

</dd> <dt>

*pvData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

Pointer to a buffer containing all required data in the data object.

</dd> <dt>

*ppObj* \[in, retval\]
</dt> <dd>

Type: **[**ID3DXFileSaveData**](id3dxfilesavedata.md)\*\***

Address of a pointer to an [**ID3DXFileSaveData**](id3dxfilesavedata.md) interface, representing the file data node to which the data object will be added.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADOBJECT, D3DXFERR\_BADVALUE, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 
