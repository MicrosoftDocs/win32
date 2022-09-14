---
title: Configuring Blending Functionality
description: Blending operations are performed on every pixel shader output (RGBA value) before the output value is written to a render target. If multisampling is enabled, blending is done on each multisample; otherwise, blending is performed on each pixel.
ms.assetid: f5c79baf-7bd3-4f58-abe7-8e96cd6be9d3
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Blending Functionality

Blending operations are performed on every pixel shader output (RGBA value) before the output value is written to a render target. If multisampling is enabled, blending is done on each multisample; otherwise, blending is performed on each pixel.

-   [Create the Blend State](#create-the-blend-state)
-   [Bind the Blend State](#bind-the-blend-state)
-   [Advanced Blending Topics](#advanced-blending-topics)
    -   [Alpha-To-Coverage](#alpha-to-coverage)
    -   [Blending Pixel Shader Outputs](#blending-pixel-shader-outputs)
-   [Related topics](#related-topics)

## Create the Blend State

The blend state is a collection of states used to control blending. These states (defined in [**D3D11\_BLEND\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_blend_desc1)) are used to create the blend state object by calling [**ID3D11Device1::CreateBlendState1**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11device1-createblendstate1).

For instance, here is a very simple example of blend-state creation that disables alpha blending and uses no per-component pixel masking.


```
ID3D11BlendState1* g_pBlendStateNoBlend = NULL;

D3D11_BLEND_DESC1 BlendState;
ZeroMemory(&BlendState, sizeof(D3D11_BLEND_DESC1));
BlendState.RenderTarget[0].BlendEnable = FALSE;
BlendState.RenderTarget[0].RenderTargetWriteMask = D3D11_COLOR_WRITE_ENABLE_ALL;
pd3dDevice->CreateBlendState1(&BlendState, &g_pBlendStateNoBlend);
```



This example is similar to the [HLSLWithoutFX10 Sample](https://msdn.microsoft.com/library/Ee416414(v=VS.85).aspx).

## Bind the Blend State

After you create the blend-state object, bind the blend-state object to the output-merger stage by calling [**ID3D11DeviceContext::OMSetBlendState**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetblendstate).


```
float blendFactor[4] = { 0.0f, 0.0f, 0.0f, 0.0f };
UINT sampleMask   = 0xffffffff;

pd3dDevice->OMSetBlendState(g_pBlendStateNoBlend, blendFactor, sampleMask);
```



This API takes three parameters: the blend-state object, a four-component blend factor, and a sample mask. You can pass in **NULL** for the blend-state object to specify the default blend state or pass in a blend-state object. If you created the blend-state object with [**D3D11\_BLEND\_BLEND\_FACTOR**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_blend) or [**D3D11\_BLEND\_INV\_BLEND\_FACTOR**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_blend), you can pass a blend factor to modulate values for the pixel shader, render target, or both. If you didn't create the blend-state object with **D3D11\_BLEND\_BLEND\_FACTOR** or **D3D11\_BLEND\_INV\_BLEND\_FACTOR**, you can still pass a non-NULL blend factor, but the blending stage does not use the blend factor; the runtime stores the blend factor, and you can later call [**ID3D11DeviceContext::OMGetBlendState**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omgetblendstate) to retrieve the blend factor. If you pass **NULL**, the runtime uses or stores a blend factor equal to { 1, 1, 1, 1 }. The sample mask is a user-defined mask that determines how to sample the existing render target before updating it. The default sampling mask is 0xffffffff which designates point sampling.

In most depth buffering schemes, the pixel closest to the camera is the one that gets drawn. When [setting up the depth stencil state](d3d10-graphics-programming-guide-depth-stencil.md), the **DepthFunc** member of [**D3D11\_DEPTH\_STENCIL\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencil_desc) can be any [**D3D11\_COMPARISON\_FUNC**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_comparison_func). Normally, you would want **DepthFunc** to be **D3D11\_COMPARISON\_LESS**, so that the pixels closest to the camera will overwrite the pixels behind them. However, depending on the needs of your application, any of the other comparison functions may be used to do the depth test.

## Advanced Blending Topics

-   [Alpha-To-Coverage](#alpha-to-coverage)
-   [Blending Pixel Shader Outputs](#blending-pixel-shader-outputs)

### Alpha-To-Coverage

Alpha-to-coverage is a multisampling technique that is most useful for situations such as dense foliage where there are several overlapping polygons that use alpha transparency to define edges within the surface.

You can use the **AlphaToCoverageEnable** member of [**D3D11\_BLEND\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_blend_desc1) or [**D3D11\_BLEND\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_blend_desc) to toggle whether the runtime converts the .a component (alpha) of output register [SV\_Target](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics)0 from the pixel shader to an n-step coverage mask (given an n-sample **RenderTarget**). The runtime performs an **AND** operation of this mask with the typical sample coverage for the pixel in the primitive (in addition to the sample mask) to determine which samples to update in all the active **RenderTarget**s.

If the pixel shader outputs [SV\_Coverage](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics), the runtime disables alpha-to-coverage.

> [!Note]  
> In multisampling, the runtime shares only one coverage for all **RenderTarget**s. The fact that the runtime reads and converts .a from output [SV\_Target](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics)0 to coverage when **AlphaToCoverageEnable** is TRUE does not change the .a value that goes to the blender at **RenderTarget** 0 (if a **RenderTarget** happens to be set there). In general, if you enable alpha-to-coverage, you don't affect how all color outputs from pixel shaders interact with **RenderTarget**s through the [output-merger stage](d3d10-graphics-programming-guide-output-merger-stage.md) except that the runtime performs an **AND** operation of the coverage mask with the alpha-to-coverage mask. Alpha-to-coverage works independently to whether the runtime can blend **RenderTarget** or whether you use blending on **RenderTarget**.

 

Graphics hardware doesn't precisely specify exactly how it converts pixel shader [SV\_Target](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics)0.a (alpha) to a coverage mask, except that alpha of 0 (or less) must map to no coverage and alpha of 1 (or greater) must map to full coverage (before the runtime performs an **AND** operation with actual primitive coverage). As alpha goes from 0 to 1, the resulting coverage should generally increase monotonically. However, hardware might perform area dithering to provide some better quantization of alpha values at the cost of spatial resolution and noise. An alpha value of NaN (Not a Number) results in a no coverage (zero) mask.

Alpha-to-coverage is also traditionally used for screen-door transparency or defining detailed silhouettes for otherwise opaque sprites.

### Blending Pixel Shader Outputs

This feature enables the output merger to use both the pixel shader outputs simultaneously as input sources to a blending operation with the single render target at slot 0.

This example takes two results and combines them in a single pass, blending one into the destination with a multiply and the other with an add:


```
SrcBlend = D3D11_BLEND_ONE;
DestBlend = D3D11_BLEND_SRC1_COLOR;
```



This example configures the first pixel shader output as the source color and the second output as a per-color component blend factor.


```
SrcBlend = D3D11_BLEND_SRC1_COLOR;
DestBlend = D3D11_BLEND_INV_SRC1_COLOR;
```



This example illustrates how the blend factors must match the shader swizzles:


```
SrcFactor = D3D11_BLEND_SRC1_ALPHA;
DestFactor = D3D11_BLEND_SRC_COLOR;
OutputWriteMask[0] = .ra; // pseudocode for setting the mask at
                          // RenderTarget slot 0 to .ra
```



Together, the blend factors and the shader code imply that the pixel shader is required to output at least o0.r and o1.a. Extra output components can be output by the shader but would be ignored, fewer components would produce undefined results.

## Related topics

<dl> <dt>

[Output-Merger Stage](d3d10-graphics-programming-guide-output-merger-stage.md)
</dt> <dt>

[Pipeline Stages (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-pipeline-stages)
</dt> </dl>

 

 