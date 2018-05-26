---
Description: A callback for the user to register a .x file template.
ms.assetid: 60568556-704c-4be3-bbde-04887583cf70
title: ID3DXSaveUserDataRegisterTemplates method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSaveUserData::RegisterTemplates method

A callback for the user to register a .x file template.

## Syntax


```C++
HRESULT RegisterTemplates(
  [in] LPD3DXFILE pXFileApi
);
```



## Parameters

<dl> <dt>

*pXFileApi* \[in\]
</dt> <dd>

Type: **[**LPD3DXFILE**](id3dxfile.md)**

Use this pointer to register user-defined .x file templates. See [**ID3DXFile**](id3dxfile.md). Do not use this parameter to add data objects.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](direct3d9.d3dxerr), as this will cause [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) to fail also, and return the error.

## Remarks

**ID3DXSaveUserData::RegisterTemplates** and [**ID3DXSaveUserData::SaveTemplates**](id3dxsaveuserdata--savetemplates.md) provide a mechanism for adding a template to a .x file for saving user data.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSaveUserData](id3dxsaveuserdata.md)
</dt> </dl>

 

 




