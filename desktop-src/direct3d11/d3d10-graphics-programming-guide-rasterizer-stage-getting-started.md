---
title: Getting Started with the Rasterizer Stage
description: This section describes setting the viewport, the scissors rectangle, the rasterizer state, and multi-sampling.
ms.assetid: d78c3845-76fd-4bd7-a603-bb1d8c66ac49
keywords:
- multisampling, rasterizer state (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with the Rasterizer Stage

This section describes setting the viewport, the scissors rectangle, the rasterizer state, and multi-sampling.

## Set the Viewport

A viewport maps vertex positions (in clip space) into render target positions. This step scales the 3D positions into 2D space. A render target is oriented with the Y axes pointing down; this requires that the Y coordinates get flipped during the viewport scale. In addition, the x and y extents (range of the x and y values) are scaled to fit the viewport size according to the following formulas:


```
X = (X + 1) * Viewport.Width * 0.5 + Viewport.TopLeftX
Y = (1 - Y) * Viewport.Height * 0.5 + Viewport.TopLeftY
Z = Viewport.MinDepth + Z * (Viewport.MaxDepth - Viewport.MinDepth) 
```



Tutorial 1 creates a 640 × 480 viewport using [**D3D11\_VIEWPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_viewport) and by calling [**ID3D11DeviceContext::RSSetViewports**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-rssetviewports).


```
    D3D11_VIEWPORT vp[1];
    vp[0].Width = 640.0f;
    vp[0].Height = 480.0f;
    vp[0].MinDepth = 0;
    vp[0].MaxDepth = 1;
    vp[0].TopLeftX = 0;
    vp[0].TopLeftY = 0;
    g_pd3dContext->RSSetViewports( 1, vp );
```



The viewport description specifies the size of the viewport, the range to map depth to (using *MinDepth* and *MaxDepth*), and the placement of the top left of the viewport. *MinDepth* must be less than or equal to *MaxDepth*; the range for both *MinDepth* and *MaxDepth* is between 0.0 and 1.0, inclusive. It is common for the viewport to map to a render target but it is not necessary; additionally, the viewport does not have to have the same size or position as the render target.

You can create an array of viewports, but only one can be applied to a primitive output from the geometry shader. Only one viewport can be set active at a time. The pipeline uses a default viewport (and scissor rectangle, discussed in the next section) during rasterization. The default is always the first viewport (or scissor rectangle) in the array. To perform a per-primitive selection of the viewport in the geometry shader, specify the ViewportArrayIndex semantic on the appropriate GS output component in the GS output signature declaration.

The maximum number of viewports (and scissor rectangles) that can be bound to the rasterizer stage at any one time is 16 (specified by **D3D11\_VIEWPORT\_AND\_SCISSORRECT\_OBJECT\_COUNT\_PER\_PIPELINE**).

## Set the Scissor Rectangle

A scissor rectangle gives you another opportunity to reduce the number of pixels that will be sent to the output merger stage. Pixels outside of the scissor rectangle are discarded. The size of the scissor rectangle is specified in integers. Only one scissor rectangle (based on *ViewportArrayIndex* in [system value semantics](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics)) can be applied to a triangle during rasterization.

To enable the scissor rectangle, use the *ScissorEnable* member (in [**D3D11\_RASTERIZER\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1)). The default scissor rectangle is an empty rectangle; that is, all rect values are 0. In other words, if you do not set up the scissor rectangle and scissor is enabled, you will not send any pixels to the output-merger stage. The most common setup is to initialize the scissor rectangle to the size of the viewport.

To set an array of scissor rectangles to the device, call [**ID3D11DeviceContext::RSSetScissorRects**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-rssetscissorrects) with [**D3D11\_RECT**](d3d11-rect.md).


```
D3D11_RECT rects[1];
  rects[0].left = 0;
  rects[0].right = 640;
  rects[0].top = 0;
  rects[0].bottom = 480;

  D3DDevice->RSSetScissorRects( 1, rects );
```



This method takes two parameters: (1) the number of rectangles in the array and (2) an array of rectangles.

The pipeline uses a default scissor rectangle index during rasterization (the default is a zero-size rectangle with clipping disabled). To override this, specify the SV\_ViewportArrayIndex semantic to a GS output component in the GS output signature declaration. This will cause the GS stage to mark this GS output component as a system-generated component with this semantic. The rasterizer stage recognizes this semantic and will use the parameter it is attached to as the scissor rectangle index to access the array of scissor rectangles. Don't forget to tell the rasterizer stage to use the scissor rectangle that you define by enabling the *ScissorEnable* value in the rasterizer description before creating the rasterizer object.

## Set Rasterizer State

Beginning with Direct3D 10, rasterizer state is encapsulated in a rasterizer state object. You may create up to 4096 rasterizer state objects which can then be set to the device by passing a handle to the state object.

Use [**ID3D11Device1::CreateRasterizerState1**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11device1-createrasterizerstate1) to create a rasterizer state object from a rasterizer description (see [**D3D11\_RASTERIZER\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1)).


```
    ID3D11RasterizerState1 * g_pRasterState;

    D3D11_RASTERIZER_DESC1 rasterizerState;
    rasterizerState.FillMode = D3D11_FILL_SOLID;
    rasterizerState.CullMode = D3D11_CULL_FRONT;
    rasterizerState.FrontCounterClockwise = true;
    rasterizerState.DepthBias = false;
    rasterizerState.DepthBiasClamp = 0;
    rasterizerState.SlopeScaledDepthBias = 0;
    rasterizerState.DepthClipEnable = true;
    rasterizerState.ScissorEnable = true;
    rasterizerState.MultisampleEnable = false;
    rasterizerState.AntialiasedLineEnable = false;
    rasterizerState.ForcedSampleCount = 0;
    pd3dDevice->CreateRasterizerState1( &rasterizerState, &g_pRasterState );
```



This example set of state accomplishes perhaps the most basic rasterizer setup:

-   Solid fill mode
-   Cull out or remove back faces; assume counter-clockwise winding order for primitives
-   Turn off depth bias but enable depth buffering and enable the scissor rectangle
-   Turn off multisampling and line anti-aliasing

In addition, basic rasterizer operations, always include the following: clipping (to the view frustum), perspective divide, and the viewport scale. After successfully creating the rasterizer state object, set it to the device like this:


```
    pd3dDevice->RSSetState(g_pRasterState);
```



### Multisampling

Multisampling samples some or all of the components of an image at a higher resolution (followed by downsampling to the original resolution) to reduce the most visible form of aliasing caused by drawing polygon edges. Even though multisampling requires sub-pixel samples, modern GPU's implement multisampling so that a pixel shader runs once per pixel. This provides an acceptable tradeoff between performance (especially in a GPU bound application) and anti-aliasing the final image.

To use multisampling, set the enable field in the [**rasterization description**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1), create a multisampled render target, and either read the render target with a shader to resolve the samples into a single pixel color or call [**ID3D11DeviceContext::ResolveSubresource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-resolvesubresource) to resolve the samples using the video card. The most common scenario is to draw to one or more multisampled render targets.

Multisampling is independent of whether or not a sample mask is used, [alpha-to-coverage](d3d10-graphics-programming-guide-blend-state.md) is enabled, or stencil operations (which are always performed per-sample).

Depth testing is affected by multisampling:

-   When multisampling is enabled, depth is interpolated per sample and the depth/stencil test is done per sample; the pixel shader output color is duplicated for all passing samples. If the pixel shader outputs depth, the depth value is duplicated for all samples (although this scenario loses the benefit of multisampling).
-   When multisampling is disabled, depth/stencil testing is still done per-sample, but depth is not interpolated per-sample.

There are no restrictions for mixing multisampled and non-multisampled rendering within a single render target. If you enable multisampling and draw to a non-multisampled render target, you produce the same result as if multisampling were not enabled; sampling is done with a single sample per-pixel.

## Related topics

<dl> <dt>

[Rasterizer Stage](d3d10-graphics-programming-guide-rasterizer-stage.md)
</dt> </dl>

 

 
