---
description: ID3DXSaveUserData interface - This interface is implemented by the application to save any additional user data embedded in .x files.
ms.assetid: 6294f942-9c14-4eed-92a8-af2821fd7e13
title: ID3DXSaveUserData interface (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSaveUserData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSaveUserData interface

This interface is implemented by the application to save any additional user data embedded in .x files. An instance of this interface is passed to [**D3DXSaveMeshHierarchyToFile**](d3dxsavemeshhierarchytofile.md), and D3DX calls the appropriate method on this interface every time the appropriate data is encountered. For example, for each frame object in the .x file, [**ID3DXSaveUserData::AddFrameChildData**](id3dxsaveuserdata--addframechilddata.md) is called and passed the child data.

## Members

The **ID3DXSaveUserData** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXSaveUserData** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXSaveUserData** interface has these methods.



| Method                                                                              | Description                                                        |
|:------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| [**AddFrameChildData**](id3dxsaveuserdata--addframechilddata.md)                   | Add child data to the frame.<br/>                            |
| [**AddMeshChildData**](id3dxsaveuserdata--addmeshchilddata.md)                     | Add child data to the mesh.<br/>                             |
| [**AddTopLevelDataObjectsPost**](id3dxsaveuserdata--addtopleveldataobjectspost.md) | Add a top level object after the frame hierarchy.<br/>       |
| [**AddTopLevelDataObjectsPre**](id3dxsaveuserdata--addtopleveldataobjectspre.md)   | Add a top level object before the frame hierarchy.<br/>      |
| [**RegisterTemplates**](id3dxsaveuserdata--registertemplates.md)                   | A callback for the user to register a .x file template.<br/> |
| [**SaveTemplates**](id3dxsaveuserdata--savetemplates.md)                           | A callback for the user to save a .x file template.<br/>     |



 

## Remarks

The LPD3DXSAVEUSERDATA type is defined as a pointer to this interface.


```
typedef interface ID3DXSaveUserData ID3DXSaveUserData;
typedef interface ID3DXSaveUserData *LPD3DXSAVEUSERDATA;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
