---
Description: Retrieves the device associated with the mesh.
ms.assetid: 16ff5267-0c64-4c3d-925d-6fc10f54c9c4
title: ID3DXBaseMesh::GetDevice method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXBaseMesh.GetDevice
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseMesh::GetDevice method

Retrieves the device associated with the mesh.

## Syntax


```C++
HRESULT GetDevice(
  [out, retval] LPDIRECT3DDEVICE9 *ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx)\***

Address of a pointer to an [**IDirect3DDevice9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx) interface, representing the Direct3D device object associated with the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Calling this method will increase the internal reference count on the [**IDirect3DDevice9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx) interface. Be sure to call [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) when you are done using this **IDirect3DDevice9** interface or you will have a memory leak.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




