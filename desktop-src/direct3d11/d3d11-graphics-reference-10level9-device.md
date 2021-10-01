---
title: 10Level9 ID3D11Device Methods
description: This section lists the differences between each 10Level9 feature level and the D3D\_FEATURE\_LEVEL\_11\_0 and higher feature level for the ID3D11Device methods.
ms.assetid: c3bc32a9-8d97-430b-be6a-b4935d7ac56c
ms.topic: reference
ms.date: 05/31/2018
---

# 10Level9 ID3D11Device Methods

This section lists the differences between each 10Level9 feature level and the D3D\_FEATURE\_LEVEL\_11\_0 and higher feature level for the [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) methods.

-   [ID3D11Device::CheckCounter](#id3d11devicecheckcounter)
-   [ID3D11Device::CheckFormatSupport](#id3d11devicecheckformatsupport)
-   [ID3D11Device::CheckMultisampleQualityLevels](#id3d11devicecheckmultisamplequalitylevels)
-   [ID3D11Device::CreateBlendState](#id3d11devicecreateblendstate)
-   [ID3D11Device::CreateBlendState1](#id3d11devicecreateblendstate1)
-   [ID3D11Device::CreateBuffer](#id3d11devicecreatebuffer)
-   [ID3D11Device::CreateCounter](#id3d11devicecreatecounter)
-   [ID3D11Device::CreateDepthStencilView](#id3d11devicecreatedepthstencilview)
-   [ID3D11Device::CreateDomainShader](#id3d11devicecreatedomainshader)
-   [ID3D11Device::CreateGeometryShader](#id3d11devicecreategeometryshader)
-   [ID3D11Device::CreateGeometryShaderWithStreamOutput](#id3d11devicecreategeometryshaderwithstreamoutput)
-   [ID3D11Device::CreateHullShader](#id3d11devicecreatehullshader)
-   [ID3D11Device::CreateInputLayout](#id3d11devicecreateinputlayout)
-   [ID3D11Device::CreatePixelShader](#id3d11devicecreatepixelshader)
-   [ID3D11Device::CreatePredicate](#id3d11devicecreatepredicate)
-   [ID3D11Device::CreateQuery](#id3d11devicecreatequery)
-   [ID3D11Device::CreateRasterizerState](#id3d11devicecreaterasterizerstate)
-   [ID3D11Device::CreateRenderTargetView](#id3d11devicecreaterendertargetview)
-   [ID3D11Device::CreateSamplerState](#id3d11devicecreatesamplerstate)
-   [ID3D11Device::CreateShaderResourceView](#id3d11devicecreateshaderresourceview)
-   [ID3D11Device::CreateTexture1D](#id3d11devicecreatetexture1d)
-   [ID3D11Device::CreateTexture2D](#id3d11devicecreatetexture2d)
-   [ID3D11Device::CreateTexture3D](#id3d11devicecreatetexture3d)
-   [ID3D11Device::CreateUnorderedAccessView](#id3d11devicecreateunorderedaccessview)
-   [ID3D11Device::CreateVertexShader](#id3d11devicecreatevertexshader)
-   [ID3D11Device::OpenSharedResource](#id3d11deviceopensharedresource)
-   [Related topics](#related-topics)

## ID3D11Device::CheckCounter




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Device-dependent counters are optionally supported. Use <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkcounterinfo"><strong>ID3D11Device::CheckCounterInfo</strong></a> to determine support.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CheckFormatSupport




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | See format support by <a href="overviews-direct3d-11-devices-downlevel-intro.md">feature level</a>${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CheckMultisampleQualityLevels




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Feature levels make no guarantees concerning MSAA support.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateBlendState



| Feature Level              | Behavior Differences                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1  | AlphaToCoverageEnable must be **FALSE**.<br/> The first four BlendEnables must all have the same value.<br/> D3D11\_BLEND\_SRC\_ALPHASAT not supported.<br/> Dual-source color blend not supported (any SrcBlend or DestBlend with SRC1 in the name)<br/>                                                                                |
| D3D\_FEATURE\_LEVEL\_9\_2  | AlphaToCoverageEnable must be **FALSE**.<br/> The first four BlendEnables must all have the same value.<br/> The first four RenderTargetWriteMasks must all have the same value.<br/> D3D11\_BLEND\_SRC\_ALPHASAT not supported.<br/> Dual-source color blend not supported (any SrcBlend or DestBlend with SRC1 in the name)<br/> |
| D3D\_FEATURE\_LEVEL\_9\_3  | AlphaToCoverageEnable must be **FALSE**.<br/> The first four BlendEnables must all have the same value.<br/> D3D11\_BLEND\_SRC\_ALPHASAT not supported.<br/> Dual-source color blend not supported (any SrcBlend or DestBlend with SRC1 in the name)<br/>                                                                                |
| D3D\_FEATURE\_LEVEL\_10\_0 | Adds alpha-to-coverage                                                                                                                                                                                                                                                                                                                                           |



 

## ID3D11Device::CreateBlendState1



| Feature Level              | Behavior Differences                                                                                                                                                                                                                                                                                                                                         |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1  | Unsupported<br/>                                                                                                                                                                                                                                                                                                                                       |
| D3D\_FEATURE\_LEVEL\_9\_2  | Unsupported<br/>                                                                                                                                                                                                                                                                                                                                       |
| D3D\_FEATURE\_LEVEL\_9\_3  | Unsupported<br/>                                                                                                                                                                                                                                                                                                                                       |
| D3D\_FEATURE\_LEVEL\_10\_0 | The *OutputMergerLogicOp* member has been added to [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options), to determine support for logical operations (bitwise logic operations between pixel shader output and render target contents, refer to [**D3D11\_RENDER\_TARGET\_BLEND\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-d3d11_render_target_blend_desc1)). |



 

## ID3D11Device::CreateBuffer




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Buffers can't have render target views.<br /> Buffers must have exactly one of D3D11_BIND_VERTEX_BUFFER, D3D11_BIND_INDEX_BUFFER, or D3D11_BIND_CONSTANT_BUFFER.<br /> Only allows index buffers with the DXGI_FORMAT_R16_UINT format. <br /> | 
| D3D_FEATURE_LEVEL_9_2 |  Buffers can't have render target views.<br /> Buffers must have exactly one of D3D11_BIND_VERTEX_BUFFER, D3D11_BIND_INDEX_BUFFER, or D3D11_BIND_CONSTANT_BUFFER.<br /> Allows index buffers with the DXGI_FORMAT_R16_UINT and DXGI_FORMAT_R32_UINT formats like D3D_FEATURE_LEVEL_10_0 and higher. <br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateCounter




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateDepthStencilView




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Does not support two-sided stencil.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateDomainShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level. ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11Device::CreateGeometryShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateGeometryShaderWithStreamOutput




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateHullShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11Device::CreateInputLayout



| Feature Level             | Behavior Differences                                                                                              |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Does not support D3D11\_INPUT\_PER\_INSTANCE\_DATA                                                                |
| D3D\_FEATURE\_LEVEL\_9\_2 | Does not support D3D11\_INPUT\_PER\_INSTANCE\_DATA                                                                |
| D3D\_FEATURE\_LEVEL\_9\_3 | Vertex stream zero must have D3D11\_INPUT\_PER\_VERTEX\_DATA, if any streams have D3D11\_INPUT\_PER\_VERTEX\_DATA |



 

See the format support by [feature level chart](overviews-direct3d-11-devices-downlevel-intro.md) for details on what formats can be used for vertex data at each feature level.

## ID3D11Device::CreatePixelShader



| Feature Level             | Behavior Differences                                    |
|---------------------------|---------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Must use ps\_4\_0\_level\_9\_1                          |
| D3D\_FEATURE\_LEVEL\_9\_2 | Must use ps\_4\_0\_level\_9\_1                          |
| D3D\_FEATURE\_LEVEL\_9\_3 | Must use ps\_4\_0\_level\_9\_3 or ps\_4\_0\_level\_9\_1 |



 

## ID3D11Device::CreatePredicate




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateQuery



| Feature Level             | Behavior Differences                                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Event queries are supported. Timestamp queries are optional: call [**CreateQuery**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createquery) to determine support.               |
| D3D\_FEATURE\_LEVEL\_9\_2 | Event and occlusion queries are supported. Timestamp queries are optional: call [**CreateQuery**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createquery) to determine support. |
| D3D\_FEATURE\_LEVEL\_9\_3 | Event and occlusion queries are supported. Timestamp queries are optional: call [**CreateQuery**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createquery) to determine support. |



 

## ID3D11Device::CreateRasterizerState




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | DepthClipEnable must be <strong>TRUE</strong>. DepthBiasClamp must be set to 0.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateRenderTargetView




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Can only support render target views of Texture2D objects.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateSamplerState




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Comparison filter is not supported.<br /> Border color must be within [0,1]<br /> Min LOD cannot be fractional<br /> Max LOD must be FLT_MAX<br /> Maximum anisotropy is 2.<br /> D3D11_TEXTURE_ADDRESS_MIRRORONCE not supported.<br /> | 
| D3D_FEATURE_LEVEL_9_2 |  Comparison filter is not supported.<br /> Border color must be within [0,1]<br /> Min LOD cannot be fractional<br /> Max LOD must be FLT_MAX<br /> Maximum anisotropy is 16.<br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateShaderResourceView



| Feature Level             | MostDetailedMip plus MipLevels must include lowest LOD (smallest subresource | View must include all resource array elements |
|---------------------------|------------------------------------------------------------------------------|-----------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Yes                                                                          | yes                                           |
| D3D\_FEATURE\_LEVEL\_9\_2 | Yes                                                                          | Yes                                           |
| D3D\_FEATURE\_LEVEL\_9\_3 | Yes                                                                          | Yes                                           |



 

## ID3D11Device::CreateTexture1D




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateTexture2D

Texture2D resources have limits on their width and height that differ across [feature levels](overviews-direct3d-11-devices-downlevel-intro.md). In feature levels 9\_3, the following are guaranteed minima, and individual implementations may exceed the requirements.



| Feature Level             | If MipCount > 1, Dimensions must be integral power of two | Minimum supported texture dimension | Cube textures dimensions must be power of two | If MISC\_TEXTURECUBE is set, the ArraySize is: | If MISC\_TEXTURECUBE is not set, the ArraySize is. |
|---------------------------|--------------------------------------------------------------|-------------------------------------|-----------------------------------------------|------------------------------------------------|----------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Yes                                                          | 2048                                | Yes                                           | 6                                              | 1                                                  |
| D3D\_FEATURE\_LEVEL\_9\_2 | Yes                                                          | 2048                                | Yes                                           | 6                                              | 1                                                  |
| D3D\_FEATURE\_LEVEL\_9\_3 | Yes                                                          | 4096                                | Yes                                           | 6                                              | 1                                                  |



 

In the previous table, the full name of **MISC\_TEXTURECUBE** is [**D3D11\_RESOURCE\_MISC\_TEXTURECUBE**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag).

The following are true for all 9\_\* [feature levels](overviews-direct3d-11-devices-downlevel-intro.md):

-   When using D3D11\_USAGE\_DEFAULT or D3D11\_USAGE\_IMMUTABLE, BindFlags cannot be zero.
-   When using D3D11\_BIND\_DEPTH\_STENCIL, MipLevels must be 1.
-   When using D3D11\_BIND\_SHADER\_RESOURCE, SampleDesc.Count must be 1.
-   When using D3D11\_BIND\_PRESENT, resource cannot have D3D11\_BIND\_SHADER\_RESOURCE.
-   When using D3D10\_DDI\_RESOURCE\_MISC\_SHARED, Format cannot be DXGI\_FORMAT\_R8G8B8A8\_UNORM or DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB.

## ID3D11Device::CreateTexture3D



| Feature Level             | Maximum Dimension (any axis) | Dimensions must be power of two |
|---------------------------|------------------------------|---------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | 256                          | Yes                             |
| D3D\_FEATURE\_LEVEL\_9\_2 | 512                          | Yes                             |
| D3D\_FEATURE\_LEVEL\_9\_3 | 512                          | Yes                             |



 

If resource is D3D11\_USAGE\_DEFAULT or D3D11\_USAGE\_IMMUTABLE, BindFlags cannot be zero.

## ID3D11Device::CreateUnorderedAccessView




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11Device::CreateVertexShader



| Feature Level             | Behavior Differences                                    |
|---------------------------|---------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Must use vs\_4\_0\_level\_9\_1                          |
| D3D\_FEATURE\_LEVEL\_9\_2 | Must use vs\_4\_0\_level\_9\_1                          |
| D3D\_FEATURE\_LEVEL\_9\_3 | Must use vs\_4\_0\_level\_9\_3 or vs\_4\_0\_level\_9\_1 |



 

## ID3D11Device::OpenSharedResource




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 |  Use <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport"><strong>ID3D11Device::CheckFeatureSupport</strong></a> with the <a href="/windows/desktop/api/D3D11/ne-d3d11-d3d11_feature"><strong>D3D11_FEATURE_FORMAT_SUPPORT2</strong></a> value and the <a href="/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_format_support2"><strong>D3D11_FEATURE_DATA_FORMAT_SUPPORT2</strong></a> structure to determine if a format can be shared. If the format can be shared, <strong>CheckFeatureSupport</strong> returns the <a href="/windows/desktop/api/D3D11/ne-d3d11-d3d11_format_support2"><strong>D3D11_FORMAT_SUPPORT2_SHAREABLE</strong></a> flag.<br /><blockquote>[!Note]<br />[<strong>DXGI_FORMAT_R8G8B8A8_UNORM</strong>](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) and <strong>DXGI_FORMAT_R8G8B8A8_UNORM_SRGB</strong> are never shareable when using feature level 9, even if the device indicates optional feature support for <strong>D3D11_FORMAT_SUPPORT_SHAREABLE</strong>. Attempting to create shared resources with DXGI formats <strong>DXGI_FORMAT_R8G8B8A8_UNORM</strong> and <strong>DXGI_FORMAT_R8G8B8A8_UNORM_SRGB</strong> will always fail unless the feature level is 10_0 or higher.</blockquote><br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## Related topics

<dl> <dt>

[10Level9 Reference](d3d11-graphics-reference-10level9.md)
</dt> </dl>

 

