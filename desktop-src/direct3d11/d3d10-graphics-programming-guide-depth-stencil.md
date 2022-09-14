---
title: Configuring Depth-Stencil Functionality
description: This section covers the steps for setting up the depth-stencil buffer, and depth-stencil state for the output-merger stage.
ms.assetid: e8f52d5f-266f-4e2c-b38d-d7fd9e27fe1f
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Depth-Stencil Functionality

This section covers the steps for setting up the depth-stencil buffer, and depth-stencil state for the output-merger stage.

-   [Create a Depth-Stencil Resource](#create-a-depth-stencil-resource)
-   [Create Depth-Stencil State](#create-depth-stencil-state)
-   [Bind Depth-Stencil Data to the OM Stage](#bind-depth-stencil-data-to-the-om-stage)

Once you know how to use the depth-stencil buffer and the corresponding depth-stencil state, refer to [advanced-stencil techniques](#advanced-stencil-techniques).

## Create a Depth-Stencil Resource

Create the depth-stencil buffer using a texture resource.


```
ID3D11Texture2D* pDepthStencil = NULL;
D3D11_TEXTURE2D_DESC descDepth;
descDepth.Width = backBufferSurfaceDesc.Width;
descDepth.Height = backBufferSurfaceDesc.Height;
descDepth.MipLevels = 1;
descDepth.ArraySize = 1;
descDepth.Format = pDeviceSettings->d3d11.AutoDepthStencilFormat;
descDepth.SampleDesc.Count = 1;
descDepth.SampleDesc.Quality = 0;
descDepth.Usage = D3D11_USAGE_DEFAULT;
descDepth.BindFlags = D3D11_BIND_DEPTH_STENCIL;
descDepth.CPUAccessFlags = 0;
descDepth.MiscFlags = 0;
hr = pd3dDevice->CreateTexture2D( &descDepth, NULL, &pDepthStencil );
```



## Create Depth-Stencil State

The depth-stencil state tells the output-merger stage how to perform the [depth-stencil test](d3d10-graphics-programming-guide-output-merger-stage.md). The depth-stencil test determines whether or not a given pixel should be drawn.


```
D3D11_DEPTH_STENCIL_DESC dsDesc;

// Depth test parameters
dsDesc.DepthEnable = true;
dsDesc.DepthWriteMask = D3D11_DEPTH_WRITE_MASK_ALL;
dsDesc.DepthFunc = D3D11_COMPARISON_LESS;

// Stencil test parameters
dsDesc.StencilEnable = true;
dsDesc.StencilReadMask = 0xFF;
dsDesc.StencilWriteMask = 0xFF;

// Stencil operations if pixel is front-facing
dsDesc.FrontFace.StencilFailOp = D3D11_STENCIL_OP_KEEP;
dsDesc.FrontFace.StencilDepthFailOp = D3D11_STENCIL_OP_INCR;
dsDesc.FrontFace.StencilPassOp = D3D11_STENCIL_OP_KEEP;
dsDesc.FrontFace.StencilFunc = D3D11_COMPARISON_ALWAYS;

// Stencil operations if pixel is back-facing
dsDesc.BackFace.StencilFailOp = D3D11_STENCIL_OP_KEEP;
dsDesc.BackFace.StencilDepthFailOp = D3D11_STENCIL_OP_DECR;
dsDesc.BackFace.StencilPassOp = D3D11_STENCIL_OP_KEEP;
dsDesc.BackFace.StencilFunc = D3D11_COMPARISON_ALWAYS;

// Create depth stencil state
ID3D11DepthStencilState * pDSState;
pd3dDevice->CreateDepthStencilState(&dsDesc, &pDSState);
```



DepthEnable and StencilEnable enable (and disable) depth and stencil testing. Set DepthEnable to **FALSE** to disable depth testing and prevent writing to the depth buffer. Set StencilEnable to **FALSE** to disable stencil testing and prevent writing to the stencil buffer (when DepthEnable is **FALSE** and StencilEnable is **TRUE**, the depth test always passes in the stencil operation).

DepthEnable only affects the output-merger stage - it does not affect clipping, depth bias, or clamping of values before the data is input to a pixel shader.

## Bind Depth-Stencil Data to the OM Stage

Bind the depth-stencil state.


```
// Bind depth stencil state
pDevice->OMSetDepthStencilState(pDSState, 1);
```



Bind the depth-stencil resource using a view.


```
D3D11_DEPTH_STENCIL_VIEW_DESC descDSV;
descDSV.Format = DXGI_FORMAT_D32_FLOAT_S8X24_UINT;
descDSV.ViewDimension = D3D11_DSV_DIMENSION_TEXTURE2D;
descDSV.Texture2D.MipSlice = 0;

// Create the depth stencil view
ID3D11DepthStencilView* pDSV;
hr = pd3dDevice->CreateDepthStencilView( pDepthStencil, // Depth stencil texture
                                         &descDSV, // Depth stencil desc
                                         &pDSV );  // [out] Depth stencil view

// Bind the depth stencil view
pd3dDeviceContext->OMSetRenderTargets( 1,          // One rendertarget view
                                &pRTV,      // Render target view, created earlier
                                pDSV );     // Depth stencil view for the render target
```



An array of render-target views may be passed into [**ID3D11DeviceContext::OMSetRenderTargets**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetrendertargets), however all of those render-target views will correspond to a single depth stencil view. The render target array in Direct3D 11 is a feature that enables an application to render onto multiple render targets simultaneously at the primitive level. Render target arrays offer increased performance over individually setting render targets with multiple calls to **ID3D11DeviceContext::OMSetRenderTargets** (essentially the method employed in Direct3D 9).

Render targets must all be the same type of resource. If multisample antialiasing is used, all bound render targets and depth buffers must have the same sample counts.

When a buffer is used as a render target, depth-stencil testing and multiple render targets are not supported.

-   As many as 8 render targets can be bound simultaneously.
-   All render targets must have the same size in all dimensions (width and height, and depth for 3D or array size for \*Array types).
-   Each render target may have a different data format.
-   Write masks control what data gets written to a render target. The output write masks control on a per-render target, per-component level what data gets written to the render target(s).

## Advanced Stencil Techniques

The stencil portion of the depth-stencil buffer can be used for creating rendering effects such as compositing, decaling, and outlining.

-   [Compositing](#compositing)
-   [Decaling](#decaling)
-   [Outlines and Silhouettes](#outlines-and-silhouettes)
-   [Two-Sided Stencil](#two-sided-stencil)
-   [Reading the Depth-Stencil Buffer as a Texture](#reading-the-depth-stencil-buffer-as-a-texture)

### Compositing

Your application can use the stencil buffer to composite 2D or 3D images onto a 3D scene. A mask in the stencil buffer is used to occlude an area of the rendering target surface. Stored 2D information, such as text or bitmaps, can then be written to the occluded area. Alternately, your application can render additional 3D primitives to the stencil-masked region of the rendering target surface. It can even render an entire scene.

Games often composite multiple 3D scenes together. For instance, driving games typically display a rear-view mirror. The mirror contains the view of the 3D scene behind the driver. It is essentially a second 3D scene composited with the driver's forward view.

### Decaling

Direct3D applications use decaling to control which pixels from a particular primitive image are drawn to the rendering target surface. Applications apply decals to the images of primitives to enable coplanar polygons to render correctly.

For instance, when applying tire marks and yellow lines to a roadway, the markings should appear directly on top of the road. However, the z values of the markings and the road are the same. Therefore, the depth buffer might not produce a clean separation between the two. Some pixels in the back primitive may be rendered on top of the front primitive and vice versa. The resulting image appears to shimmer from frame to frame. This effect is called z-fighting or flimmering.

To solve this problem, use a stencil to mask the section of the back primitive where the decal will appear. Turn off z-buffering and render the image of the front primitive into the masked-off area of the render-target surface.

Multiple texture blending can be used to solve this problem.

### Outlines and Silhouettes

You can use the stencil buffer for more abstract effects, such as outlining and silhouetting.

If your application does two render passes - one to generate the stencil mask and second to apply the stencil mask to the image, but with the primitives slightly smaller on the second pass - the resulting image will contain only the primitive's outline. The application can then fill the stencil-masked area of the image with a solid color, giving the primitive an embossed look.

If the stencil mask is the same size and shape as the primitive you are rendering, the resulting image contains a hole where the primitive should be. Your application can then fill the hole with black to produce a silhouette of the primitive.

### Two-Sided Stencil

Shadow Volumes are used for drawing shadows with the stencil buffer. The application computes the shadow volumes cast by occluding geometry, by computing the silhouette edges and extruding them away from the light into a set of 3D volumes. These volumes are then rendered twice into the stencil buffer.

The first render draws forward-facing polygons, and increments the stencil-buffer values. The second render draws the back-facing polygons of the shadow volume, and decrements the stencil buffer values. Normally, all incremented and decremented values cancel each other out. However, the scene was already rendered with normal geometry causing some pixels to fail the z-buffer test as the shadow volume is rendered. Values left in the stencil buffer correspond to pixels that are in the shadow. These remaining stencil-buffer contents are used as a mask, to alpha-blend a large, all-encompassing black quad into the scene. With the stencil buffer acting as a mask, the result is to darken pixels that are in the shadows.

This means that the shadow geometry is drawn twice per light source, hence putting pressure on the vertex throughput of the GPU. The two-sided stencil feature has been designed to mitigate this situation. In this approach, there are two sets of stencil state (named below), one set each for the front-facing triangles and the other for the back-facing triangles. This way, only a single pass is drawn per shadow volume, per light.

An example of two-sided stencil implementation can be found in the [ShadowVolume10 Sample](https://msdn.microsoft.com/library/Ee416427(v=VS.85).aspx).

### Reading the Depth-Stencil Buffer as a Texture

An inactive depth-stencil buffer can be read by a shader as a texture. An application that reads a depth-stencil buffer as a texture renders in two passes, the first pass writes to the depth-stencil buffer and the second pass reads from the buffer. This allows a shader to compare depth or stencil values previously written to the buffer against the value for the pixel currrently being rendered. The result of the comparison can be used to create effects such as shadow mapping or soft particles in a particle system.

To create a depth-stencil buffer that can be used as both a depth-stencil resource and a shader resource a few changes need to be made to sample code in the [Create a Depth-Stencil Resource](#create-a-depth-stencil-resource) section.

-   The depth-stencil resource must have a typeless format such as DXGI\_FORMAT\_R32\_TYPELESS.
    ```
    descDepth.Format = DXGI_FORMAT_R32_TYPELESS;
    ```

    

-   The depth-stencil resource must use both the D3D10\_BIND\_DEPTH\_STENCIL and D3D10\_BIND\_SHADER\_RESOURCE bind flags.
    ```
    descDepth.BindFlags = D3D10_BIND_DEPTH_STENCIL | D3D10_BIND_SHADER_RESOURCE;
    ```

    

In addition a shader resource view needs to be created for the depth buffer using a [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_shader_resource_view_desc) structure and [**ID3D11Device::CreateShaderResourceView**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createshaderresourceview). The shader resource view will use a typed format such as **DXGI\_FORMAT\_R32\_FLOAT** that is the equivalent to the typeless format specified when the depth-stencil resource was created.

In the first render pass the depth buffer is bound as described in the [Bind Depth-Stencil Data to the OM Stage](#bind-depth-stencil-data-to-the-om-stage) section. Note that the format passed to [**D3D11\_DEPTH\_STENCIL\_VIEW\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencil_view_desc).Format will use a typed format such as **DXGI\_FORMAT\_D32\_FLOAT**. After the first render pass the depth buffer will contain the depth values for the scene.

In the second render pass the [**ID3D11DeviceContext::OMSetRenderTargets**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetrendertargets) function is used to set the depth-stencil view to **NULL** or a different depth-stencil resource and the shader resource view is passed to the shader using [**ID3D11EffectShaderResourceVariable::SetResource**](id3dx11effectshaderresourcevariable-setresource.md). This allows the shader to look up the depth values calculated in the first rendering pass. Note that a transformation will need to be applied to retrieve depth values if the point of view of the first render pass is different from the second render pass. For example, if a shadow mapping technique is being used the first render pass will be from the perspective of a light source while the second render pass will from the viewer's perspective.

## Related topics

<dl> <dt>

[Output-Merger Stage](d3d10-graphics-programming-guide-output-merger-stage.md)
</dt> <dt>

[Pipeline Stages (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-pipeline-stages)
</dt> </dl>

 

 