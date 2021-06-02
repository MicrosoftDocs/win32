---
description: Direct3D 10.1 Features
ms.assetid: e60c6116-e2f9-46b7-aed8-13e3e5ae2b90
title: Direct3D 10.1 Features
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 10.1 Features

Direct3D 10.1 extends the feature set of Direct3D 10.0 with the following new features:

-   Blend Modes - Independent blend modes per render target using the new blend-state interface (see [**ID3D10BlendState1 Interface**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10blendstate1)). Dual source blending operations are restricted to render target slot 0; you may not write to other outputs or have any render targets bound to slots other than slot 0.
-   Culling Behavior - Zero-area faces are automatically culled; this affects wireframe rendering only.
-   Floating Point Rules - Uses the same IEEE-754 rules for floating-point EXCEPT 32-bit floating point operations have been tightened to produce a result within 0.5 unit-last-place (0.5 ULP) of the infinitely precise result. This applies to addition, subtraction, and multiplication. (accuracy to 0.5 ULP for multiply, 1.0 ULP for reciprocal).
-   Formats - The precision of float16 blending has increased to 0.5 ULP. Blending is also required for UNORM16/SNORM16/SNORM8 formats.
-   Multisample Anti-Aliasing - Multisampling has been enhanced to generalize coverage based transparency and make multisampling work more effectively with multi-pass rendering. To achieve this, all multisample semantics are defined as if the pixel shader always runs once per sample (sample-frequency), computing a separate color per sample. If a pixel shader doesn't use any per-sample attributes, then it will compute the same value for each covered sample in a pixel. In that case, it is equivalent to the hardware executing the shader once per pixel (pixel-frequency), replicating the result to all covered samples. Naturally, running at pixel-frequency always produces the same results as running the same shader at sample-frequency, when the attributes are sampled at a pixel-frequency. The PSInvocations pipeline statistic increments at sample-frequency unless the shader is running at pixel-frequency.
-   Pipeline Stage Bandwidth - Increased the amount of data that can be passed between shader stages: 

    | Resource                        | Limits                    |
    |---------------------------------|---------------------------|
    | Registers between Shader Stages | 32 (32-bit x 4-component) |
    | Vertex Shader Input Registers   | 32                        |
    | Input Assembler input slots     | 32                        |

    

     

-   Rasterization Rules - The rules for rasterization have changed for lines, in addition, new functionality has been added.
    -   MultisampleEnable only affects line rasterization (points and triangles are unaffected), and is used to choose a line drawing algorithm. This means that some multisample rasterization from Direct3D 10 are no longer supported.
    -   New sample-frequency pixel shader execution with primitive rasterization.
-   Resources - CopyResource is enabled in two new scenarios:
    -   Both color and depth/stencil MSAA surfaces can now be used with CopyResource as either a source or destination
    -   Format Conversion while copying between certain 32/64/128 bit prestructured, typed resources and compressed representations of the same bit widths.
-   Texture Sampling - sample\_c and sample\_c\_lz instructions are defined to work with both Texture2DArrays and TextureCubeArrays, use the Location member (the alpha component) to specify an an array index.
-   Views - TextureCube and the new TextureCubeArray (see [**D3D10\_TEXCUBE\_ARRAY\_SRV1**](/windows/desktop/api/d3d10_1/ns-d3d10_1-d3d10_texcube_array_srv1)) are not actual resources, but are new views on a Texture2DArray resource. Create a resource view from a Texture2DArray resource with a new usage flag (D3D10\_RESOURCE\_MISC\_TEXTURECUBE), use the new [**ID3D10ShaderResourceView1 Interface**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10shaderresourceview1) interface to bind a cube-texture view to the pipeline.

The new features require a 10.1 device type (see [**ID3D10Device1 Interface**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10device1)) which can be created by calling [**D3D10CreateDevice1**](/windows/desktop/api/D3D10_1/nf-d3d10_1-d3d10createdevice1), or you can create the device and swap chain at the same time by calling [**D3D10CreateDeviceAndSwapChain1**](/windows/desktop/api/D3D10_1/nf-d3d10_1-d3d10createdeviceandswapchain1).

In Windows Vista Service Pack 1, Direct3D 10.0 and Direct3D 10.1 DLLs exist side-by-side on the system. To access 10.1 features, do either of the following:

## Accessing 10.1 Features on Vista Gold and Vista Service Pack 1

Developers that wish to support Vista Gold as well as SP1 will have to account for the lack of the new 10.1 API extensions on Vista Gold. Both DXUT and D3DX10 will provide convenience functions to create the appropriate device, based on the DLLs available on the system and the available hardware (10.0 or 10.1). The 10.1 device inherits from the 10.0 device, and can be retrieved using QueryInterface(). It is recommended that each application keeps track of the device type and maintains a pointer to the 10.1 device (if available) to avoid frequent QueryInterface calls when 10.1 functionality is desired. Likewise, where 10.1 resource views and state objects are associated by an application's custom class, it is recommended that the application track whether the object is a 10.0 or 10.1 type to avoid redundant QueryInterface() calls. D3DX10 includes a set of utility functions to simplify this process (see [**D3DX10CreateDevice**](d3dx10createdevice.md) and [**D3DX10CreateDeviceAndSwapChain**](d3dx10createdeviceandswapchain.md)).

## Accessing 10.1 Features on Vista Service Pack 1 Exclusively

Some developers may choose to require Vista Service Pack 1, which will be distributed broadly to end-users and includes a series of improvements outside of Direct3D 10.1. These developers can use the Direct3D 10.1 headers and libraries exclusively, taking a dependency on the Direct3D 10.1 DLLs which support both 10.0 and 10.1 hardware (some calls may fail, however, on 10.0 devices where the new functionality is not supported).

Some additional notes:

-   The APIs exposed in the D3DX10.dll will accept both 10.0 and 10.1 devices, and will take advantage of 10.1 functionality when available.
-   D3D10SDKLayers.dll supports a 10.1 device and can output the appropriate debug spew for 10.1 features.
-   D3D10Ref.dll implements a 10.0 and 10.1 software device.
-   D3DX10 and FXC support the updated 10.1 shader model with the following targets: vs\_4\_1, gs\_4\_1, ps\_4\_1, and fx\_4\_1 which can be bound to a 10.1 device. A 10.1 device supports shader model 4.0 and 4.1 shaders.
-   The Direct3D 10.0 effect framework supports 10.0 and 10.1 devices, however, any technique that includes shader model 4.1 shaders or the new 10.1 features must use a 10.1 device.

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 



