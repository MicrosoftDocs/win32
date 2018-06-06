---
Description: Creates a compressed precomputed radiance transfer (PRT) buffer from an uncompressed ID3DXPRTBuffer object. This function should be used with per-vertex or volume buffers.
ms.assetid: 1464d2dd-05db-4d9a-84ac-39d57b6fff4f
title: D3DXCreatePRTCompBuffer function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXCreatePRTCompBuffer function

Creates a compressed precomputed radiance transfer (PRT) buffer from an uncompressed [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object. This function should be used with per-vertex or volume buffers.

## Syntax


```C++
HRESULT D3DXCreatePRTCompBuffer(
  _In_    D3DXSHCOMPRESSQUALITYTYPE Quality,
  _In_    UINT                      NumClusters,
  _In_    UINT                      NumPCA,
  _In_    LPD3DXSHPRTSIMCB          pCB,
  _In_    LPVOID                    lpUserContext,
  _In_    LPD3DXPRTBUFFER           pBuffer,
  _Inout_ LPD3DXPRTCOMPBUFFER       *ppBuffer
);
```



## Parameters

<dl> <dt>

*Quality* \[in\]
</dt> <dd>

Type: **[**D3DXSHCOMPRESSQUALITYTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxshcompressqualitytype.htm)**

Quality of spherical harmonic (SH) compression. See [**D3DXSHCOMPRESSQUALITYTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxshcompressqualitytype.htm).

</dd> <dt>

*NumClusters* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of clusters to use for compression.

</dd> <dt>

*NumPCA* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of principal component analysis (PCA) basis vectors to use in each cluster.

</dd> <dt>

*pCB* \[in\]
</dt> <dd>

Type: **[LPD3DXSHPRTSIMCB](lpd3dxshprtsimcb.md)**

Optional pointer to the [LPD3DXSHPRTSIMCB](lpd3dxshprtsimcb.md) callback function that is used to compute the percentage of PRT compression computations completed. The callback function must be implemented to return S\_OK to keep running the compression routine. Any other value will halt compression. May be **NULL**.

</dd> <dt>

*lpUserContext* \[in\]
</dt> <dd>

Type: **[**LPVOID**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Optional pointer to a user-defined value passed to the [LPD3DXSHPRTSIMCB](lpd3dxshprtsimcb.md) callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function. May be **NULL**.

</dd> <dt>

*pBuffer* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Address of a pointer to the uncompressed [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that will be compressed.

</dd> <dt>

*ppBuffer* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTCOMPBUFFER**](id3dxprtcompbuffer.md)\***

Address of a pointer to the output [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> <dt>

[**D3DXCreatePRTBuffer**](d3dxcreateprtbuffer.md)
</dt> <dt>

[**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md)
</dt> </dl>

 

 




