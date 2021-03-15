---
description: The ID3DXPRTBuffer interface is used as a data buffer to store vertex and pixel data for use with precomputed radiance transfer (PRT) methods and functions.
ms.assetid: 36c1fd13-0949-4991-93cb-41ace458802d
title: ID3DXPRTBuffer interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPRTBuffer
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer interface

The ID3DXPRTBuffer interface is used as a data buffer to store vertex and pixel data for use with precomputed radiance transfer (PRT) methods and functions.

## Members

The **ID3DXPRTBuffer** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXPRTBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXPRTBuffer** interface has these methods.



| Method                                                   | Description                                                                                                                                                                                   |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddBuffer**](id3dxprtbuffer--addbuffer.md)           | Adds another buffer to the **ID3DXPRTBuffer** and stores the results in **ID3DXPRTBuffer**.<br/>                                                                                        |
| [**AttachGH**](id3dxprtbuffer--attachgh.md)             | Associates an [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object with the **ID3DXPRTBuffer** object.<br/>                                                              |
| [**EvalGH**](id3dxprtbuffer--evalgh.md)                 | Applies stored texture gutter data to an **ID3DXPRTBuffer** texture buffer.<br/>                                                                                                        |
| [**ExtractTexture**](id3dxprtbuffer--extracttexture.md) | Extracts coefficient data from a color channel of the buffer for a specified range of coefficients, and adds the data to an [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) object.<br/> |
| [**ExtractToMesh**](id3dxprtbuffer--extracttomesh.md)   | Extracts coefficient data from a single-channel buffer and adds the data to an [**ID3DXMesh**](id3dxmesh.md) object.<br/>                                                              |
| [**GetHeight**](id3dxprtbuffer--getheight.md)           | Retrieves the height of the texture, in pixels.<br/>                                                                                                                                    |
| [**GetNumChannels**](id3dxprtbuffer--getnumchannels.md) | Retrieves the number of color channels used in memory to store samples.<br/>                                                                                                            |
| [**GetNumCoeffs**](id3dxprtbuffer--getnumcoeffs.md)     | Retrieves the number of scalars per color channel used in memory to store samples.<br/>                                                                                                 |
| [**GetNumSamples**](id3dxprtbuffer--getnumsamples.md)   | Retrieves the number of vertices (or texels) sampled.<br/>                                                                                                                              |
| [**GetWidth**](id3dxprtbuffer--getwidth.md)             | Retrieves the width of the texture, in pixels.<br/>                                                                                                                                     |
| [**IsTexture**](id3dxprtbuffer--istexture.md)           | Indicates whether the buffer contains a texture.<br/>                                                                                                                                   |
| [**LockBuffer**](id3dxprtbuffer--lockbuffer.md)         | Locks a range of vertex or texel sample data and obtains a pointer to the location in buffer memory.<br/>                                                                               |
| [**ReleaseGH**](id3dxprtbuffer--releasegh.md)           | Unassociates an attached [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object with the **ID3DXPRTBuffer** object.<br/>                                                   |
| [**Resize**](id3dxprtbuffer--resize.md)                 | Changes the number of samples contained in the buffer.<br/>                                                                                                                             |
| [**ScaleBuffer**](id3dxprtbuffer--scalebuffer.md)       | Multiplies every value in the buffer by a constant value.<br/>                                                                                                                          |
| [**UnlockBuffer**](id3dxprtbuffer--unlockbuffer.md)     | Ends the lifespan of the ppData pointer returned by [**ID3DXPRTBuffer::LockBuffer**](id3dxprtbuffer--lockbuffer.md).<br/>                                                              |



 

## Remarks

The **ID3DXPRTBuffer** interface is obtained by calling the [**D3DXCreatePRTBuffer**](d3dxcreateprtbuffer.md) or [**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md) functions.

The LPD3DXPRTBUFFER type is defined as a pointer to the **ID3DXPRTBuffer** interface.


```
typedef interface ID3DXPRTBuffer ID3DXPRTBuffer;
typedef interface ID3DXPRTBuffer *LPD3DXPRTBUFFER;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> <dt>

[**D3DXCreatePRTBuffer**](d3dxcreateprtbuffer.md)
</dt> <dt>

[**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md)
</dt> <dt>

[**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md)
</dt> </dl>

 

 
