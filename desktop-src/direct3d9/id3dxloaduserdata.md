---
description: ID3DXLoadUserData interface - This interface is implemented by the application to save any additional user data embedded in .x files.
ms.assetid: 0d656f99-c24c-4326-bc6f-c0e7874c0fb2
title: ID3DXLoadUserData interface (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXLoadUserData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXLoadUserData interface

This interface is implemented by the application to save any additional user data embedded in .x files. An instance of this interface is passed to [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md), and D3DX calls the appropriate method on this interface every time the appropriate data is encountered. For example, for each frame object in the .x file, [**ID3DXLoadUserData::LoadFrameChildData**](id3dxloaduserdata--loadframechilddata.md) is called and passed the child data.

## Members

The **ID3DXLoadUserData** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXLoadUserData** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXLoadUserData** interface has these methods.



| Method                                                              | Description                                      |
|:--------------------------------------------------------------------|:-------------------------------------------------|
| [**LoadFrameChildData**](id3dxloaduserdata--loadframechilddata.md) | Load frame child data from a .x file.<br/> |
| [**LoadMeshChildData**](id3dxloaduserdata--loadmeshchilddata.md)   | Load mesh child data from a .x file.<br/>  |
| [**LoadTopLevelData**](id3dxloaduserdata--loadtopleveldata.md)     | Load top level data from a .x file.<br/>   |



 

## Remarks

The LPD3DXLOADUSERDATA type is defined as a pointer to this interface.


```
typedef interface ID3DXLoadUserData ID3DXLoadUserData;
typedef interface ID3DXLoadUserData *LPD3DXLOADUSERDATA;
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

 

 
