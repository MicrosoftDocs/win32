---
description: A list of the features available in Direct3D 10 is here. This page lists the Direct3D 9 features that are no longer supported in Direct3D 10.
ms.assetid: ad3eff8e-a225-47c0-a53f-b1a3c94bcaac
title: Deprecated Features (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Deprecated Features (Direct3D 10)

A list of the features available in Direct3D 10 is [here](d3d10-graphics-programming-guide-api-features.md). This page lists the Direct3D 9 features that are no longer supported in Direct3D 10.

The biggest feature changes in Direct3D 10 are:

- Direct3D 10 no longer supports the fixed-function transform and lighting pipeline.
- Direct3D 10 no longer supports the fixed-function texture blender (sometimes called a fixed-function pixel shader).
- Direct3D 10 implements new rasterization rules, which are simpler and cleaner than the legacy GDI rules that are implemented in Direct3D 9. For instance, the last-pixel control for lines is no longer supported.

Here is a complete list of the features in Direct3D 9 that have been deprecated in Direct3D 10.

- **Alpha blend**. Alpha blend is now programmed independent of color blend. Direct3D 10 adds an alpha-blend-enable toggle which is enabled by default. See [State Objects (Direct3D 10)](d3d10-graphics-programming-guide-api-features-state-objects.md) for more information.
- **Alpha test**. Alpha test is a fixed-function pixel behavior for Direct3D 9. Alpha test is moved into programmable pixel shaders for Direct3D 10 and higher. For info about emulating the Direct3D 9 alpha test functionality in Direct3D 10 and higher, see the FixedFuncEMU sample in the [DirectX SDK for June 2010](https://www.microsoft.com/download/en/details.aspx?id=6812).
- **Blend mode options**. BOTHSRCALPHA has been removed from D3D10\_BLEND since it is redundant with BOTHINVSRCALPHA. See [**D3D10\_BLEND**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_blend) for more information.
- **Block compression formats**. There is no distinction between pre-multiplied alpha or non-premultiplied alpha in Direct3D 10. These Direct3D 9 formats map to these Direct3D 10 formats: 

    | Direct3D 9 | Direct3D 10 |
    |------------|-------------|
    | DXT1       | BC1\*       |
    | DXT2,DXT3  | BC2\*       |
    | DXT4,DXT5  | BC3\*       |

    

     

    See [Block Compression (Direct3D 10)](d3d10-graphics-programming-guide-resources-block-compression.md) for additional information.

-   **Clip planes**. Instead of using clip planes, Direct3D 10 implements clip distances and cull distances, with up to 8 components each in up to 2 elements of vertex attributes. See [Semantics (DirectX HLSL)](../direct3dhlsl/dx-graphics-hlsl-semantics.md) for additional information. [FixedFuncEMU sample](https://msdn.microsoft.com/library/Ee416406(v=VS.85).aspx) provides an example of emulating clip planes in Direct3D 10.
-   **Dithering**. Direct3D 10 does not support writing dithered data to a render target.
-   **Fixed-function transform and lighting pipeline in not available**. Instead, you must use shaders. See [Shader Stages (Direct3D 10)](/previous-versions//bb205146(v=vs.85)) for additional information.
-   **Fixed-function texture blender (also called a fixed function pixel shader)**. Instead, you must use shaders. See [Shader Stages (Direct3D 10)](/previous-versions//bb205146(v=vs.85)) for additional information.
-   **Fill modes** have changed. Direct3D 10 implements solid and wireframe fill modes. D3DFILLMODE point has been removed, use a geometry shader to emulate point mode if necessary. [FixedFuncEMU sample](https://msdn.microsoft.com/library/Ee416406(v=VS.85).aspx) provides an example of emulating D3DFILLMODE point in Direct3D 10. See [**D3D10\_FILL\_MODE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_fill_mode) and [Shader Stages (Direct3D 10)](/previous-versions//bb205146(v=vs.85)) for additional information.
-   **Formats**. Hardware can use formats exposed by the API. Luminance formats are no longer implemented.
-   **Mipmap filtering**. Removed the option for selecting no-filter mode. Instead, use a texture with only a single mipmap or set the MaxLOD sampler state to 0. See [State Objects (Direct3D 10)](d3d10-graphics-programming-guide-api-features-state-objects.md) for additional information.
-   **Palettes**. Applications should use a dependent texture read instead.
-   **Pixel and vertex shader models**: 1\_x, 2\_x, and 3\_0. Direct3D 10 supports shader model 4. See [Shader Model 4](../direct3dhlsl/dx-graphics-hlsl-sm4.md) for additional information.
-   **Point sprites**. Use a geometry shader instead. See [Shader Stages (Direct3D 10)](/previous-versions//bb205146(v=vs.85)) for additional information.
-   **Rasterization rules**. Legacy GDI line rasterization rules are replaced with cleaner, simpler rules. The last-pixel control for lines is no longer supported. See [Rasterization Rules (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-rasterizer-stage-rules.md) for additional information.
-   **Shade modes**. D3DSHADEMODE (which support flat/gouraud/phong shading) has been removed. Direct3D 10 implements two interpolations modifiers for vertex shader outputs instead. See [FixedFuncEMU sample](https://msdn.microsoft.com/library/Ee416406(v=VS.85).aspx) for an example of emulating Direct3D 9 gouraud and flat shade modes in Direct3D 10.
-   **texldp** instruction. An application must implement a projected-texture load with extra HLSL statements. See [Reference for HLSL](../direct3dhlsl/dx-graphics-hlsl-reference.md) for additional information. [FixedFuncEMU sample](https://msdn.microsoft.com/library/Ee416406(v=VS.85).aspx) provides an example of emulating texldp in Direct3D 10.
-   **Texture coordinate-index** (TCI) texture-stage state (D3DTSS\_TEXCOORDINDEX) is no longer supported.
-   **Triangle fans**. An application must convert existing triangle-fans to triangle lists or triangle strips. To emulate some behaviors using DrawPrimitive in older APIs, try using DrawIndexed in Direct3D 10. See [Primitive Topologies (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-primitive-topologies.md) for additional information.
-   **W buffering**. Hardware support is not guaranteed; it is recommended that an application uses high-precision depth buffers instead. See [Configuring Depth-Stencil Functionality (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-depth-stencil.md) for additional information.
-   **Wrap modes** (texture coordinate wrapping). Texture address wrapping (such as wrap, mirror, clamp etc.) still exist. See [**D3D10\_SAMPLER\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_sampler_desc) and [**D3D10\_TEXTURE\_ADDRESS\_MODE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_texture_address_mode).

## Related topics

<dl> <dt>

[API Features (Direct3D 10)](d3d10-graphics-programming-guide-api-features.md)
</dt> </dl>

 

 
