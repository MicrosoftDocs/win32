---
description: The ID3DXBuffer interface is used as a data buffer, storing vertex, adjacency, and material information during mesh optimization and loading operations.
ms.assetid: 63ee3b2d-c0e6-4ad4-9274-2b1dfd77f89d
title: ID3DXBuffer interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBuffer
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBuffer interface

The ID3DXBuffer interface is used as a data buffer, storing vertex, adjacency, and material information during mesh optimization and loading operations. The buffer object is used to return arbitrary length data. Also, buffer objects are used to return object code and error messages in methods that assemble vertex and pixel shaders.

## Members

The **ID3DXBuffer** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXBuffer** interface has these methods.



| Method                                                    | Description                                                    |
|:----------------------------------------------------------|:---------------------------------------------------------------|
| [**GetBufferPointer**](id3dxbuffer--getbufferpointer.md) | Retrieves a pointer to the data in the buffer.<br/>      |
| [**GetBufferSize**](id3dxbuffer--getbuffersize.md)       | Retrieves the total size of the data in the buffer.<br/> |



 

## Remarks

The **ID3DXBuffer** interface is obtained by calling the [**D3DXCreateBuffer**](d3dxcreatebuffer.md) function.

The LPD3DXBUFFER type is defined as a pointer to the **ID3DXBuffer** interface.


```
typedef interface ID3DXBuffer ID3DXBuffer;
typedef interface ID3DXBuffer *LPD3DXBUFFER;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
