---
Description: The ID3DXPRTCompBuffer interface stores a compressed version of a ID3DXPRTBuffer buffer, for use with principal component analysis (PCA).
ms.assetid: 97f8576c-24d5-4f60-923b-4d8d94382fe9
title: ID3DXPRTCompBuffer interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ID3DXPRTCompBuffer interface

The **ID3DXPRTCompBuffer** interface stores a compressed version of a [**ID3DXPRTBuffer**](id3dxprtbuffer.md) buffer, for use with principal component analysis (PCA).

## Members

The **ID3DXPRTCompBuffer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **ID3DXPRTCompBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXPRTCompBuffer** interface has these methods.



| Method                                                             | Description                                                                                                                                                                                                                        |
|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExtractBasis**](id3dxprtcompbuffer--extractbasis.md)           | Extracts the mean and principal component analysis (PCA) basis vectors for a given cluster from an **ID3DXPRTCompBuffer** compressed data buffer.<br/>                                                                       |
| [**ExtractClusterIDs**](id3dxprtcompbuffer--extractclusterids.md) | Extracts the per-sample cluster IDs from an **ID3DXPRTCompBuffer** compressed data buffer.<br/>                                                                                                                              |
| [**ExtractPCA**](id3dxprtcompbuffer--extractpca.md)               | Extracts the per-sample principal component analysis (PCA) projection coefficients from an **ID3DXPRTCompBuffer** compressed data buffer.<br/>                                                                               |
| [**ExtractTexture**](id3dxprtcompbuffer--extracttexture.md)       | Extracts the per-sample principal component analysis (PCA) projection coefficients from an **ID3DXPRTCompBuffer** compressed data buffer and adds the data to an [**IDirect3DTexture9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dtexture9) object.<br/> |
| [**ExtractToMesh**](id3dxprtcompbuffer--extracttomesh.md)         | Extracts the per-sample principal component analysis (PCA) projection coefficients from an **ID3DXPRTCompBuffer** compressed data buffer and adds the data to an [**ID3DXMesh**](id3dxmesh.md) object.<br/>                 |
| [**GetHeight**](id3dxprtcompbuffer--getheight.md)                 | Retrieves the height of the texture, in pixels.<br/>                                                                                                                                                                         |
| [**GetNumChannels**](id3dxprtcompbuffer--getnumchannels.md)       | Retrieves the number of color channels used in memory to store samples.<br/>                                                                                                                                                 |
| [**GetNumClusters**](id3dxprtcompbuffer--getnumclusters.md)       | Retrieves the number of clusters to use for compression.<br/>                                                                                                                                                                |
| [**GetNumCoeffs**](id3dxprtcompbuffer--getnumcoeffs.md)           | Retrieves the number of scalars per color channel used in memory to store samples.<br/>                                                                                                                                      |
| [**GetNumPCA**](id3dxprtcompbuffer--getnumpca.md)                 | Retrieves the number of principal component analysis (PCA) basis vectors to use in each cluster.<br/>                                                                                                                        |
| [**GetNumSamples**](id3dxprtcompbuffer--getnumsamples.md)         | Retrieves the number of vertices (or texels) sampled.<br/>                                                                                                                                                                   |
| [**GetWidth**](id3dxprtcompbuffer--getwidth.md)                   | Retrieves the width of the texture, in pixels.<br/>                                                                                                                                                                          |
| [**IsTexture**](id3dxprtcompbuffer--istexture.md)                 | Indicates whether the buffer contains a texture.<br/>                                                                                                                                                                        |
| [**NormalizeData**](id3dxprtcompbuffer--normalizedata.md)         | Normalizes all principal component analysis (PCA) weights so that they are between -1 and 1. Basis vectors are modified to reflect this normalization.<br/>                                                                  |



 

## Remarks

The **ID3DXPRTCompBuffer** interface is obtained by calling the [**D3DXCreatePRTCompBuffer**](d3dxcreateprtcompbuffer.md) function.

The LPD3DXPRTCOMPBUFFER type is defined as a pointer to the **ID3DXPRTCompBuffer** interface.


```
typedef interface ID3DXPRTCompBuffer ID3DXPRTCompBuffer;
typedef interface ID3DXPRTCompBuffer *LPD3DXPRTCOMPBUFFER;
```



## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> <dt>

[**D3DXCreatePRTCompBuffer**](d3dxcreateprtcompbuffer.md)
</dt> <dt>

[**ID3DXPRTBuffer**](id3dxprtbuffer.md)
</dt> </dl>

 

 




