---
title: 10Level9 ID3D11DeviceContext Methods
description: This section lists the differences between each 10Level9 feature level and the D3D\_FEATURE\_LEVEL\_11\_0 and higher feature level for the ID3D11DeviceContext methods.
ms.assetid: 84478b56-0306-491a-9545-0849b06d8342
ms.topic: reference
ms.date: 05/31/2018
---

# 10Level9 ID3D11DeviceContext Methods

This section lists the differences between each 10Level9 feature level and the D3D\_FEATURE\_LEVEL\_11\_0 and higher feature level for the [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) methods.

-   [ID3D11DeviceContext::CopySubresourceRegion](#id3d11devicecontextcopysubresourceregion)
-   [ID3D11DeviceContext::CopyResource](#id3d11devicecontextcopyresource)
-   [ID3D11DeviceContext::CopyStructureCount](#id3d11devicecontextcopystructurecount)
-   [ID3D11DeviceContext::ClearUnorderedAccessViewFloat](#id3d11devicecontextclearunorderedaccessviewfloat)
-   [ID3D11DeviceContext::ClearUnorderedAccessViewUint](#id3d11devicecontextclearunorderedaccessviewuint)
-   [ID3D11DeviceContext::ClearRenderTargetView](#id3d11devicecontextclearrendertargetview)
-   [ID3D11DeviceContext::CSSetConstantBuffers](#id3d11devicecontextcssetconstantbuffers)
-   [ID3D11DeviceContext::CSSetSamplers](#id3d11devicecontextcssetsamplers)
-   [ID3D11DeviceContext::CSSetShader](#id3d11devicecontextcssetshader)
-   [ID3D11DeviceContext::CSSetShaderResources](#id3d11devicecontextcssetshaderresources)
-   [ID3D11DeviceContext::CSSetUnorderedAccessViews](#id3d11devicecontextcssetunorderedaccessviews)
-   [ID3D11DeviceContext::Dispatch](#id3d11devicecontextdispatch)
-   [ID3D11DeviceContext::DispatchIndirect](#id3d11devicecontextdispatchindirect)
-   [ID3D11DeviceContext::Draw](#id3d11devicecontextdraw)
-   [ID3D11DeviceContext::DrawAuto](#id3d11devicecontextdrawauto)
-   [ID3D11DeviceContext::DrawIndexed](#id3d11devicecontextdrawindexed)
-   [ID3D11DeviceContext::DrawIndexedInstanced](#id3d11devicecontextdrawindexedinstanced)
-   [ID3D11DeviceContext::DrawIndexedInstancedIndirect](#id3d11devicecontextdrawindexedinstancedindirect)
-   [ID3D11DeviceContext::DrawInstanced](#id3d11devicecontextdrawinstanced)
-   [ID3D11DeviceContext::DrawInstancedIndirect](#id3d11devicecontextdrawinstancedindirect)
-   [ID3D11DeviceContext::DSSetConstantBuffers](#id3d11devicecontextdssetconstantbuffers)
-   [ID3D11DeviceContext::DSSetSamplers](#id3d11devicecontextdssetsamplers)
-   [ID3D11DeviceContext::DSSetShader](#id3d11devicecontextdssetshader)
-   [ID3D11DeviceContext::DSSetShaderResources](#id3d11devicecontextdssetshaderresources)
-   [ID3D11DeviceContext::GSSetConstantBuffers](#id3d11devicecontextgssetconstantbuffers)
-   [ID3D11DeviceContext::GSSetSamplers](#id3d11devicecontextgssetsamplers)
-   [ID3D11DeviceContext::GSSetShader](#id3d11devicecontextgssetshader)
-   [ID3D11DeviceContext::GSSetShaderResources](#id3d11devicecontextgssetshaderresources)
-   [ID3D11DeviceContext::HSSetConstantBuffers](#id3d11devicecontexthssetconstantbuffers)
-   [ID3D11DeviceContext::HSSetSamplers](#id3d11devicecontexthssetsamplers)
-   [ID3D11DeviceContext::HSSetShader](#id3d11devicecontexthssetshader)
-   [ID3D11DeviceContext::HSSetShaderResources](#id3d11devicecontexthssetshaderresources)
-   [ID3D11DeviceContext::IASetIndexBuffer](#id3d11devicecontextiasetindexbuffer)
-   [ID3D11DeviceContext::IASetPrimitiveTopology](#id3d11devicecontextiasetprimitivetopology)
-   [ID3D11DeviceContext::OMSetBlendState](#id3d11devicecontextomsetblendstate)
-   [ID3D11DeviceContext::OMSetRenderTargets](#id3d11devicecontextomsetrendertargets)
-   [ID3D11DeviceContext::OMSetRenderTargetsAndUnorderedAccessViews](#id3d11devicecontextomsetrendertargetsandunorderedaccessviews)
-   [ID3D11DeviceContext::PSSetConstantBuffers](#id3d11devicecontextpssetconstantbuffers)
-   [ID3D11DeviceContext::PSSetSamplers](#id3d11devicecontextpssetsamplers)
-   [ID3D11DeviceContext::PSSetShader](#id3d11devicecontextpssetshader)
-   [ID3D11DeviceContext::PSSetShaderResources](#id3d11devicecontextpssetshaderresources)
-   [ID3D11DeviceContext::RSSetScissorRects](#id3d11devicecontextrssetscissorrects)
-   [ID3D11DeviceContext::RSSetViewports](#id3d11devicecontextrssetviewports)
-   [ID3D11DeviceContext::SetPredication](#id3d11devicecontextsetpredication)
-   [ID3D11DeviceContext::SOSetTargets](#id3d11devicecontextsosettargets)
-   [ID3D11DeviceContext::VSSetConstantBuffers](#id3d11devicecontextvssetconstantbuffers)
-   [ID3D11DeviceContext::VSSetSamplers](#id3d11devicecontextvssetsamplers)
-   [ID3D11DeviceContext::VSSetShader](#id3d11devicecontextvssetshader)
-   [ID3D11DeviceContext::VSSetShaderResources](#id3d11devicecontextvssetshaderresources)
-   [Related topics](#related-topics)

## ID3D11DeviceContext::CopySubresourceRegion




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 |  Only Texture2D and buffers may be copied within GPU-accessible memory.<br /> Texture3D cannot be copied from GPU-accessible memory to CPU-accessible memory.<br /> Any resource that has only D3D10_BIND_SHADER_RESOURCE cannot be copied from GPU-accessible memory to CPU-accessible memory.<br /> You can't copy mipmapped volume textures. <br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CopyResource




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 |  Only Texture2D and buffers may be copied within GPU-accessible memory.<br /> Texture3D cannot be copied from GPU-accessible memory to CPU-accessible memory.<br /> Any resource that has only D3D10_BIND_SHADER_RESOURCE cannot be copied from GPU-accessible memory to CPU-accessible memory.<br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CopyStructureCount




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::ClearUnorderedAccessViewFloat




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::ClearUnorderedAccessViewUint




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::ClearRenderTargetView




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only the first array slice will be cleared. Applications should create a render target view for each face or array slice, then clear each view individually.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::CSSetUnorderedAccessViews




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::Dispatch




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::DispatchIndirect




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::Draw



| Feature Level             | Behavior Differences                                                                                                               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Number of primitives may not exceed 65535.<br/> Textures cannot repeat over one primitive more than 128 times.<br/>    |
| D3D\_FEATURE\_LEVEL\_9\_2 | Number of primitives may not exceed 1048575.<br/> Textures cannot repeat over one primitive more than 2048 times.<br/> |
| D3D\_FEATURE\_LEVEL\_9\_3 | Number of primitives may not exceed 1048575.<br/> Textures cannot repeat over one primitive more than 8192 times.<br/> |



 

## ID3D11DeviceContext::DrawAuto




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::DrawIndexed



| Feature Level             | Behavior Differences                                                                                                                                                                                                            |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_FEATURE\_LEVEL\_9\_1 | Number of primitives may not exceed 65535.<br/> Textures cannot repeat over one primitive more than 128 times.<br/> Index values cannot exceed 65534.<br/> Indexed point lists not supported.<br/>      |
| D3D\_FEATURE\_LEVEL\_9\_2 | Number of primitives may not exceed 1048575.<br/> Textures cannot repeat over one primitive more than 2048 times.<br/> Index values cannot exceed 1048575.<br/> Indexed point lists not supported.<br/> |
| D3D\_FEATURE\_LEVEL\_9\_3 | Number of primitives may not exceed 1048575.<br/> Textures cannot repeat over one primitive more than 8192 times.<br/> Index values cannot exceed 1048575.<br/> Indexed point lists not supported.<br/> |



 

## ID3D11DeviceContext::DrawIndexedInstanced




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | Number of primitives may not exceed 1048575.<br /> Textures cannot repeat over one primitive more than 8192 times.<br /> Index values cannot exceed 1048575.<br /><blockquote>[!Note]<br />When you call the <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-drawindexedinstanced"><strong>DrawIndexedInstanced</strong></a> method with a vertex shader that is bound to the pipeline and that doesn't import any per-instance data, some Direct3D 9 graphics hardware might not draw anything. In particular, if the vertex shader does not use any per-instance data, calling <strong>DrawIndexedInstanced</strong> with 1 instance is not equivalent to calling <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-draw"><strong>Draw</strong></a>.</blockquote><br /> | 




 

## ID3D11DeviceContext::DrawIndexedInstancedIndirect




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::DrawInstanced




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::DrawInstancedIndirect




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::DSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::DSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::DSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::DSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::GSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::GSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::GSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::GSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::HSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::HSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::HSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::HSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* or 10.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 
| D3D_FEATURE_LEVEL_10_0 | 
| D3D_FEATURE_LEVEL_10_1 | 




 

## ID3D11DeviceContext::IASetIndexBuffer




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Format is allowed to be different from that specified at buffer creation, but an expensive translation will be incurred.<br /> Only allows index buffers with the DXGI_FORMAT_R16_UINT format. <br /> | 
| D3D_FEATURE_LEVEL_9_2 |  Format is allowed to be different from that specified at buffer creation, but an expensive translation will be incurred.<br /> Allows index buffers with the DXGI_FORMAT_R16_UINT and DXGI_FORMAT_R32_UINT formats like D3D_FEATURE_LEVEL_10_0 and higher. <br /> ${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::IASetPrimitiveTopology




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Primitive topologies with adjacency are not supported${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::OMSetBlendState




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | SampleMask cannot be zero${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::OMSetRenderTargets




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only one render target supported${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | Only four render targets supported, and all bound resources must have same bit depth. | 




 

## ID3D11DeviceContext::OMSetRenderTargetsAndUnorderedAccessViews




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::PSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | See feature level 10.0, but total number of constants used by shader cannot exceed 32${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::PSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | No more than 16 samplers can be bound${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::PSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only ps_4_0_level_9_1${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | Only ps_4_0_level_9_3 or ps_4_0_level_9_1 | 




 

## ID3D11DeviceContext::PSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | No more than 8 simultaneously bound shader resources${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::RSSetScissorRects




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only the zeroth scissor rect is available${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::RSSetViewports




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only the zeroth viewport is available${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

Even though you specify float values to the members of the [**D3D11\_VIEWPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_viewport) structure for the *pViewports* array in a call to [**ID3D11DeviceContext::RSSetViewports**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-rssetviewports) for [feature levels](overviews-direct3d-11-devices-downlevel-intro.md) 9\_x, **RSSetViewports** uses DWORDs internally. Because of this behavior, when you use a negative top left corner for the viewport, the call to **RSSetViewports** for feature levels 9\_x fails. This failure occurs because **RSSetViewports** for 9\_x casts the floating point values into unsigned integers without validation, which results in integer overflow.

The call to [**ID3D11DeviceContext::RSSetViewports**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-rssetviewports) for [feature levels](overviews-direct3d-11-devices-downlevel-intro.md) 10\_x and 11\_x works as you expect even when you use a negative top left corner for the viewport.

## ID3D11DeviceContext::SetPredication




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::SOSetTargets




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::VSSetConstantBuffers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | See feature level 10.0, but total number of constants used by shader cannot exceed 255${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::VSSetSamplers




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## ID3D11DeviceContext::VSSetShader




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Only vs_4_0_level_9_1${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | Only vs_4_0_level_9_3 or vs_4_0_level_9_1 | 




 

## ID3D11DeviceContext::VSSetShaderResources




| Feature Level | Behavior Differences | 
|---------------|----------------------|
| D3D_FEATURE_LEVEL_9_1 | Not supported on any 9.* feature level.${REMOVE}$<br /> | 
| D3D_FEATURE_LEVEL_9_2 | 
| D3D_FEATURE_LEVEL_9_3 | 




 

## Related topics

<dl> <dt>

[10Level9 Reference](d3d11-graphics-reference-10level9.md)
</dt> </dl>

 

 





