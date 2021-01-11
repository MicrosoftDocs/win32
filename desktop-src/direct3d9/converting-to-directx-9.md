---
description: The following features were changed in Microsoft Direct3D 9. If you are using these features, see the changes listed below to help you port your application to Direct3D 9.
ms.assetid: 6f5b2cc1-5415-4af8-a964-051a5af42680
title: Converting to Direct3D 9
ms.topic: article
ms.date: 05/31/2018
---

# Converting to Direct3D 9

The following features were changed in Microsoft Direct3D 9. If you are using these features, see the changes listed below to help you port your application to Direct3D 9.

-   [BaseVertexIndex Changes](#basevertexindex-changes)
-   [CreateImageSurface Changes](#createimagesurface-changes)
-   [D3DENUM\_NO\_WHQL\_LEVEL Changes](/windows)
-   [Create Resource Changes](#create-resource-changes)
-   [EnumAdapterModes Changes](#enumadaptermodes-changes)
-   [Get/SetStreamSource\_Changes](#getsetstreamsource-changes)
-   [Multisampling Quality Changes](#multisampling-quality-changes)
-   [ResourceManagerDiscardBytes Changes](#resourcemanagerdiscardbytes-changes)
-   [SetSoftwareVertexProcessing Changes](#setsoftwarevertexprocessing-changes)
-   [Texture Sampler Changes](#texture-sampler-changes)
-   [Vertex Declaration Changes](#vertex-declaration-changes)
-   [Intervals,\_and\_SwapEffects\_Changes](#intervals-and-swapeffects-changes)

## BaseVertexIndex Changes

In DirectX 8.x, IDirect3DDevice8::SetIndices required a pointer to the index buffer and a BaseVertexIndex for the starting position in the vertex buffer. An application batching different objects into the vertex buffer had to switch the index buffer (or make a call to IDirect3DDevice8::SetIndices) before calling IDirect3DDevice8::DrawIndexedPrimitive.

In Direct3D 9, the starting position in the vertex buffer, *BaseVertexIndex*, has been moved to IDirect3DDevice9::DrawIndexedPrimitive, and its data type changed from a DWORD to an INT.


```
HRESULT IDirect3DDevice9::DrawIndexedPrimitive( 
    D3DPRIMITIVETYPE PrimType, 
    INT BaseVertexIndex, 
    UINT minIndex, 
    UINT NumVertices, 
    UINT startIndex, 
    UINT primCount); 

HRESULT SetIndices(IDirect3DIndexBuffer9* pIndexData); 
```



## CreateImageSurface Changes

IDirect3DDevice8::CreateImageSurface was renamed [**CreateOffscreenPlainSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createoffscreenplainsurface). An additional parameter that takes a D3DPOOL type was added. D3DPOOL\_SCRATCH will return a surface that has identical characteristics to a surface created by IDirect3DDevice8::CreateImageSurface. D3DPOOL\_DEFAULT is the appropriate pool for use with [**StretchRect**](/windows/desktop/api) and [**ColorFill**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-colorfill).

## D3DENUM\_NO\_WHQL\_LEVEL Changes

Applications now have to explicitly ask for the Microsoft Windows Hardware Quality Labs (WHQL) because the response takes relatively long (a few seconds). D3DENUM\_NO\_WHQL\_LEVEL has been removed and D3DENUM\_WHQL\_LEVEL has been added.

## Create Resource Changes

A handle has been added to several methods and should be set to **NULL**. The methods affected include:

-   [**CreateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createtexture)
-   [**CreateVolumeTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvolumetexture)
-   [**CreateCubeTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createcubetexture)
-   [**CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer)
-   [**CreateIndexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createindexbuffer)
-   [**CreateRenderTarget**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createrendertarget)
-   [**CreateDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createdepthstencilsurface)
-   [**CreateOffscreenPlainSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createoffscreenplainsurface)

## EnumAdapterModes Changes

The [**EnumAdapterModes**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-enumadaptermodes) now takes a D3DFORMAT.


```
HRESULT IDirect3D9::EnumAdapterModes( 
       UINT Adapter, 
       D3DFORMAT Format, 
       UINT Mode, 
       D3DDISPLAYMODE *pMode); 
```



The format supports an expanding set of display modes. To protect applications from enumerating formats that were not invented when the application shipped, the application must tell Direct3D the format for the display modes that should be enumerated. The resulting array of display modes will differ only by width, height, and refresh rate.

The application specifies a pixel format and the enumeration is restricted to those display modes that exactly match the format. The following is a list of the allowed formats:

-   D3DFMT\_A1R5G5B5
-   D3DFMT\_A2B10G10R10
-   D3DFMT\_A8R8G8B8
-   D3DFMT\_R5G6B5
-   D3DFMT\_X1R5G5B5
-   D3DFMT\_X8R8G8B8

Enumeration is equivalent for alpha and nonalpha versions of the same format. The returned Format will always be filled with the same format supplied by the application.

This method treats 565 and 555 as equivalent, and returns the correct version in the Format. The difference comes into play only when the application locks the back buffer, and there is an explicit flag that the application must set in order to accomplish this.

## Get/SetStreamSource Changes

One parameter has been added to the [**GetStreamSource**](/windows/desktop/api) and [**SetStreamSource**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsource) methods. The offset is the number of bytes between the beginning of the stream and the beginning of the vertex data. It is measured in bytes. This enables the pipeline to support stream offsets. To find out if the device supports stream offsets, see D3DDEVCAPS2\_STREAMOFFSET.


```
HRESULT GetStreamSource(
    UINT StreamNumber,
    IDirect3DVertexBuffer9 **ppStreamData,
    UINT *pOffsetInBytes,
    UINT *pStride);
```



## Multisampling Quality Changes

Previously, there was only the D3DMULTISAMPLE\_TYPE enumeration. Direct3D 9 retains this enumeration and adds the idea of a quality level for each element of the enumeration. The quality level indicates a trade-off between visual quality and performance by indicating the number of maskable samples (in the sense of D3DRS\_MULTISAMPLEMASK).

An application should choose how many maskable samples it requires, and then consult pQualityLevels. If nonzero, this value indicates the number of quality levels the application can pass to the various creation functions through MultiSampleQuality. Because drivers expose all their multisample schemes as quality levels at D3DMULTISAMPLE\_NONMASKABLE, you can enumerate all available multisampling schemes through this one type if your application does not need to mask samples.

The D3DPRASTERCAPS\_STRETCHBLTMULTISAMPLE caps bit has been retired. This bit used to mean that the multisampling method did not support write masks, and could not be toggled on and off between [**BeginScene**](/windows/desktop/api) and [**EndScene**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-endscene). Such nonmaskable methods are now exposed through D3DMULTISAMPLE\_NONMASKABLE.


```
HRESULT CheckDeviceMultiSampleType( 
       UINT Adapter, 
       D3DDEVTYPE DeviceType, 
       D3DFORMAT SurfaceFormat, 
       BOOL Windowed, 
       D3DMULTISAMPLE_TYPE MultiSampleType, 
       DWORD * pQualityLevels); 
```



There is a different maximum for each number of maskable samples. For example, D3DMULTISAMPLE\_4\_SAMPLES might have three levels of quality, while D3DMULTISAMPLE\_2\_SAMPLES might have only one. There are at most eight levels of quality for each number of maskable samples (the driver is not allowed to express more). The quality ranges from zero to (\*pQualityLevels - 1).

## ResourceManagerDiscardBytes Changes

ResourceManagerDiscardBytes has been replaced by IDirect3DDevice9::EvictManagedResources. It can evict all resources, both Direct3D and driver resources.

The resource manager is now consulted when a resource (whether managed or nonmanaged) fails creation because there is insufficient video memory. The manager will automatically be asked to free enough resources for the creation to succeed. In DirectX 8.0, this was not an automated process.

## SetSoftwareVertexProcessing Changes

An application can create a mixed-mode device to use software and hardware vertex processing.

To switch between the two vertex processing modes in DirectX 8.x, call IDirect3DDevice8::SetRenderState. This has been replaced with [**SetSoftwareVertexProcessing**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsoftwarevertexprocessing) to ease problems caused by state blocks. This new method is not recorded by state blocks.

## Texture Sampler Changes

Direct3D 9 supports up to sixteen texture surfaces in one pass using the pixel shader 2\_0 model; however, the number of texture coordinates remains limited to eight. Texture stage state is associated with surfaces, coordinate sets, vertex processing, and pixel processing. To manage these differences at compile time, [**SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate) has been broken into two methods:

-   IDirect3DDevice9::SetTextureStageState will still be used for texture coordinate state, such as wrap modes and texture coordinate generation.
-   [**SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) has been added and will now be used for filtering, tiling, clamping, MIPLOD, and so forth. This will work for up to sixteen samplers.

### SetTextureStageState Changes

IDirect3DDevice9::SetTextureStageState now sets the following states:

-   Fixed function vertex processing state. This state controls the manipulation of texture coordinates D3DTSS\_TEXTURETRANSFORMFLAGS and D3DTSS\_TEXCOORDINDEX. Up to eight of each can be set (because eight texture coordinates are always supported). D3DTSS\_TEXCOORDINDEX is a fixed function vertex processing state. If a programmable vertex shader is used, this state is ignored.
-   Fixed function pixel shader state (the legacy TextureStageState).

    -   D3DTSS\_ALPHAARG0
    -   D3DTSS\_ALPHAARG1
    -   D3DTSS\_ALPHAARG2
    -   D3DTSS\_ALPHAOP
    -   D3DTSS\_BUMPENVLOFFSET
    -   D3DTSS\_BUMPENVLSCALE
    -   D3DTSS\_BUMPENVMAT00
    -   D3DTSS\_BUMPENVMAT01
    -   D3DTSS\_BUMPENVMAT10
    -   D3DTSS\_BUMPENVMAT11
    -   D3DTSS\_COLORARG0
    -   D3DTSS\_COLORARG1
    -   D3DTSS\_COLORARG2
    -   D3DTSS\_COLOROP
    -   D3DTSS\_RESULTARG

    The number of fixed function pixel shader states that can be set is less than or equal to the number represented by MaxTextureBlendStages.

The number of texture samplers available to the application is determined by the pixel shader version, as indicated in the following table.



| Name                    | Number                                                         |
|-------------------------|----------------------------------------------------------------|
| ps\_1\_1 to ps\_1\_3    | 4 texture samplers                                             |
| ps\_1\_4                | 6 texture samplers                                             |
| ps\_2\_0                | 16 texture samplers                                            |
| fixed function pipeline | MaxTextureBlendStages/MaxSimultaneousTextures texture samplers |



 

Devices that support displacement mapping in Direct3D 9 will support an additional sampler (D3DDMAPSAMPLER), which samples the displacement maps in the tessellator unit.

### SetSamplerState Changes

IDirect3DDevice9::SetSamplerState sets the sampler state (including the one used in the tessellator unit to sample displacement maps). These have been renamed with a D3DSAMP\_ prefix to enable compile-time error detection when porting from DirectX 8.x. The states include:

-   D3DSAMP\_ADDRESSU
-   D3DSAMP\_ADDRESSV
-   D3DSAMP\_ADDRESSW
-   D3DSAMP\_BORDERCOLOR
-   D3DSAMP\_MAGFILTER
-   D3DSAMP\_MAXANISOTROPY
-   D3DSAMP\_MAXMIPLEVEL
-   D3DSAMP\_MINFILTER
-   D3DSAMP\_MIPFILTER
-   D3DSAMP\_MIPMAPLODBIAS

## Vertex Declaration Changes

Vertex declarations are now decoupled from vertex shader creation. Vertex declarations now use a Component Object Model (COM) interface.

For DirectX 8.x, vertex declarations are tied to vertex shaders.

-   For the fixed function pipeline, call [**SetVertexShader**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshader) with the flexible vertex format (FVF) code of the vertex buffer.
-   For vertex shaders, call IDirect3DDevice9::SetVertexShader with a handle to a previously create vertex shader. The shader includes a vertex declaration.

For Direct3D 9, vertex declarations are decoupled from vertex shaders and they can be used with either the fixed function pipeline or with shaders.

-   For the fixed function pipeline, there is no need to call IDirect3DDevice9::SetVertexShader. If, however, you want to switch to the fixed function pipeline and have previously used a vertex shader, call IDirect3DDevice9::SetVertexShader(**NULL**). When this is done, you will still need to call [**SetFVF**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setfvf) to declare the FVF code.
-   When using vertex shaders, call IDirect3DDevice9::SetVertexShader with the vertex shader object. Additionally, call IDirect3DDevice9::SetFVF to set up a vertex declaration. This uses the information implicit in the FVF. [**SetVertexDeclaration**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexdeclaration) can be called in place of IDirect3DDevice9::SetFVF because it supports vertex declarations that cannot be expressed with an FVF.

## Intervals, and SwapEffects Changes

Several changes were made to give the user more control over monitor refresh rate, presentation rate, and front-buffer versus back-buffer drawing. They are as follows:

-   Removed one swap effect, D3DSWAPEFFECT\_COPY\_VSYNC, and one presentation rate, D3DPRESENT\_RATE\_UNLIMITED.
-   Renamed D3DPRESENT\_PARAMETERS.FullScreen\_PresentationInterval to PresentationIntervals.
-   Added D3DPRESENT\_INTERVAL\_IMMEDIATE, which means that the presentation is not synchronized with the vertical sync. As in DirectX 8.x, D3DPRESENT\_INTERVAL\_DEFAULT is defined as zero and is equivalent to D3DPRESENT\_INTERVAL\_ONE. D3DPRESENT\_INTERVAL\_DEFAULT is a convenience for initializing D3DPRESENT\_PARAMETERS to zero.

For a detailed explanation of the modes and the intervals that are supported, see D3DPRESENT.

## Related topics

<dl> <dt>

[Direct3D 9 Graphics](dx9-graphics.md)
</dt> </dl>

 

 
