---
description: Load mesh child data from a .x file.
ms.assetid: 5ed338f9-48a6-44e6-95da-1bed9ecd6ebf
title: ID3DXLoadUserData::LoadMeshChildData method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXLoadUserData.LoadMeshChildData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXLoadUserData::LoadMeshChildData method

Load mesh child data from a .x file.

## Syntax


```C++
HRESULT LoadMeshChildData(
  [in] LPD3DXMESHCONTAINER pMeshContainer,
  [in] LPD3DXFILEDATA      pXofChildData
);
```



## Parameters

<dl> <dt>

*pMeshContainer* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESHCONTAINER**](d3dxmeshcontainer.md)**

Pointer to a mesh container. See [**D3DXMESHCONTAINER**](d3dxmeshcontainer.md).

</dd> <dt>

*pXofChildData* \[in\]
</dt> <dd>

Type: **[**LPD3DXFILEDATA**](id3dxfiledata.md)**

Pointer to a .x file data structure. This is defined in Dxfile.h.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from D3DERR or D3DXERR, as this will cause [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) to fail also, and return the error.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLoadUserData](id3dxloaduserdata.md)
</dt> </dl>

 

 




