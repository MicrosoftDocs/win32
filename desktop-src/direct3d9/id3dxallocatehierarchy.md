---
Description: 'This interface is implemented by the application to allocate or free frame and mesh container objects. Methods on this are called during loading and destroying frame hierarchies.'
ms.assetid: 'b2c4ecb7-3655-4120-b957-724a754e948a'
title: ID3DXAllocateHierarchy interface
---

# ID3DXAllocateHierarchy interface

This interface is implemented by the application to allocate or free frame and mesh container objects. Methods on this are called during loading and destroying frame hierarchies.

## Members

The **ID3DXAllocateHierarchy** interface inherits from the [**IUnknown**](com.iunknown) interface. **ID3DXAllocateHierarchy** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXAllocateHierarchy** interface has these methods.



| Method                                                                       | Description                                                  |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**CreateFrame**](id3dxallocatehierarchy--createframe.md)                   | Requests allocation of a frame object.<br/>            |
| [**CreateMeshContainer**](id3dxallocatehierarchy--createmeshcontainer.md)   | Requests allocation of a mesh container object.<br/>   |
| [**DestroyFrame**](id3dxallocatehierarchy--destroyframe.md)                 | Requests deallocation of a frame object.<br/>          |
| [**DestroyMeshContainer**](id3dxallocatehierarchy--destroymeshcontainer.md) | Requests deallocation of a mesh container object.<br/> |



 

## Remarks

The LPD3DXALLOCATEHIERARCHY type is defined as a pointer to this interface.


```
typedef interface ID3DXAllocateHierarchy ID3DXAllocateHierarchy;
typedef interface ID3DXAllocateHierarchy *LPD3DXALLOCATEHIERARCHY;
```



## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 




