---
Description: Add a top level object before the frame hierarchy.
ms.assetid: ab4bfc3e-58eb-4de6-b080-8b3392b801bf
title: ID3DXSaveUserData::AddTopLevelDataObjectsPre method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXSaveUserData::AddTopLevelDataObjectsPre method

Add a top level object before the frame hierarchy.

## Syntax


```C++
HRESULT AddTopLevelDataObjectsPre(
  [in] LPD3DXFILESAVEOBJECT pXofSave
);
```



## Parameters

<dl> <dt>

*pXofSave* \[in\]
</dt> <dd>

Type: **[**LPD3DXFILESAVEOBJECT**](id3dxfilesaveobject.md)**

Pointer to a .x file save object. Use this pointer to call [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) to create the data object to be saved. Then call [**IDirectXFileSaveObject::SaveData**](idirectxfilesaveobject--savedata.md) to save the data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxerr.htm), as this will cause [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) to fail also, and return the error.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSaveUserData](id3dxsaveuserdata.md)
</dt> </dl>

 

 




