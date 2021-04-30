---
description: Prepares a device for drawing sprites.
ms.assetid: ec9eb069-0a41-4dd5-bbd5-5a31133550b6
title: ID3DXSprite::Begin method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSprite.Begin
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSprite::Begin method

Prepares a device for drawing sprites.

## Syntax


```C++
HRESULT Begin(
  [in] DWORD Flags
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of zero or more flags that describe sprite rendering options. For this method, the valid flags are:

-   D3DXSPRITE\_ALPHABLEND
-   D3DXSPRITE\_\_BILLBOARD
-   D3DXSPRITE\_DONOTMODIFY\_RENDERSTATE
-   D3DXSPRITE\_DONOTSAVESTATE
-   D3DXSPRITE\_OBJECTSPACE
-   D3DXSPRITE\_\_SORT\_DEPTH\_BACKTOFRONT
-   D3DXSPRITE\_\_SORT\_DEPTH\_FRONTTOBACK
-   D3DXSPRITE\_\_SORT\_TEXTURE

For a description of the flags and for information on how to control device state capture and device view transforms, see [D3DXSPRITE](d3dxsprite.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_OUTOFVIDEOMEMORY, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

This method must be called from inside a [**IDirect3DDevice9::BeginScene**](/windows/desktop/api) . . . [**IDirect3DDevice9::EndScene**](/windows/desktop/api) sequence. **ID3DXSprite::Begin** cannot be used as a substitute for either **IDirect3DDevice9::BeginScene** or [**ID3DXRenderToSurface::BeginScene**](id3dxrendertosurface--beginscene.md).

This method will set the following states on the device.

Render States:



| Type ([**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)) | Value                                                                                                             |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| D3DRS\_ALPHABLENDENABLE                                       | TRUE                                                                                                              |
| D3DRS\_ALPHAFUNC                                              | D3DCMP\_GREATER                                                                                                   |
| D3DRS\_ALPHAREF                                               | 0x00                                                                                                              |
| D3DRS\_ALPHATESTENABLE                                        | AlphaCmpCaps                                                                                                      |
| D3DRS\_BLENDOP                                                | D3DBLENDOP\_ADD                                                                                                   |
| D3DRS\_CLIPPING                                               | TRUE                                                                                                              |
| D3DRS\_CLIPPLANEENABLE                                        | FALSE                                                                                                             |
| D3DRS\_COLORWRITEENABLE                                       | D3DCOLORWRITEENABLE\_ALPHA \| D3DCOLORWRITEENABLE\_BLUE \| D3DCOLORWRITEENABLE\_GREEN \| D3DCOLORWRITEENABLE\_RED |
| D3DRS\_CULLMODE                                               | D3DCULL\_NONE                                                                                                     |
| D3DRS\_DESTBLEND                                              | D3DBLEND\_INVSRCALPHA                                                                                             |
| D3DRS\_DIFFUSEMATERIALSOURCE                                  | D3DMCS\_COLOR1                                                                                                    |
| D3DRS\_ENABLEADAPTIVETESSELLATION                             | FALSE                                                                                                             |
| D3DRS\_FILLMODE                                               | D3DFILL\_SOLID                                                                                                    |
| D3DRS\_FOGENABLE                                              | FALSE                                                                                                             |
| D3DRS\_INDEXEDVERTEXBLENDENABLE                               | FALSE                                                                                                             |
| D3DRS\_LIGHTING                                               | FALSE                                                                                                             |
| D3DRS\_RANGEFOGENABLE                                         | FALSE                                                                                                             |
| D3DRS\_SEPARATEALPHABLENDENABLE                               | FALSE                                                                                                             |
| D3DRS\_SHADEMODE                                              | D3DSHADE\_GOURAUD                                                                                                 |
| D3DRS\_SPECULARENABLE                                         | FALSE                                                                                                             |
| D3DRS\_SRCBLEND                                               | D3DBLEND\_SRCALPHA                                                                                                |
| D3DRS\_SRGBWRITEENABLE                                        | FALSE                                                                                                             |
| D3DRS\_STENCILENABLE                                          | FALSE                                                                                                             |
| D3DRS\_VERTEXBLEND                                            | FALSE                                                                                                             |
| D3DRS\_WRAP0                                                  | 0                                                                                                                 |



 

Texture Stage States:



| Stage Identifier | Type ([**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md)) | Value            |
|------------------|---------------------------------------------------------------------------|------------------|
| 0                | D3DTSS\_ALPHAARG1                                                         | D3DTA\_TEXTURE   |
| 0                | D3DTSS\_ALPHAARG2                                                         | D3DTA\_DIFFUSE   |
| 0                | D3DTSS\_ALPHAOP                                                           | D3DTOP\_MODULATE |
| 0                | D3DTSS\_COLORARG1                                                         | D3DTA\_TEXTURE   |
| 0                | D3DTSS\_COLORARG2                                                         | D3DTA\_DIFFUSE   |
| 0                | D3DTSS\_COLOROP                                                           | D3DTOP\_MODULATE |
| 0                | D3DTSS\_TEXCOORDINDEX                                                     | 0                |
| 0                | D3DTSS\_TEXTURETRANSFORMFLAGS                                             | D3DTTFF\_DISABLE |
| 1                | D3DTSS\_ALPHAOP                                                           | D3DTOP\_DISABLE  |
| 1                | D3DTSS\_COLOROP                                                           | D3DTOP\_DISABLE  |



 

Sampler States:



| Sampler Stage Index | Type ([**D3DSAMPLERSTATETYPE**](./d3dsamplerstatetype.md)) | Value                                                                                                          |
|---------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 0                   | D3DSAMP\_ADDRESSU                                               | D3DTADDRESS\_CLAMP                                                                                             |
| 0                   | D3DSAMP\_ADDRESSV                                               | D3DTADDRESS\_CLAMP                                                                                             |
| 0                   | D3DSAMP\_MAGFILTER                                              | D3DTEXF\_ANISOTROPIC if TextureFilterCaps includes D3DPTFILTERCAPS\_MAGFANISOTROPIC; otherwise D3DTEXF\_LINEAR |
| 0                   | D3DSAMP\_MAXMIPLEVEL                                            | 0                                                                                                              |
| 0                   | D3DSAMP\_MAXANISOTROPY                                          | MaxAnisotropy                                                                                                  |
| 0                   | D3DSAMP\_MINFILTER                                              | D3DTEXF\_ANISOTROPIC if TextureFilterCaps includes D3DPTFILTERCAPS\_MINFANISOTROPIC; otherwise D3DTEXF\_LINEAR |
| 0                   | D3DSAMP\_MIPFILTER                                              | D3DTEXF\_LINEAR if TextureFilterCaps includes D3DPTFILTERCAPS\_MIPFLINEAR; otherwise D3DTEXF\_POINT            |
| 0                   | D3DSAMP\_MIPMAPLODBIAS                                          | 0                                                                                                              |
| 0                   | D3DSAMP\_SRGBTEXTURE                                            | 0                                                                                                              |



 

> [!Note]  
> This method disables N-patches.

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> <dt>

[D3DXSPRITE](d3dxsprite.md)
</dt> </dl>

 

 
