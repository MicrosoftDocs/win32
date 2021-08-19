---
title: Migrating to Direct3D 11
description: This section provides info for migrating to Direct3D 11 from an earlier version of Direct3D.
ms.assetid: 3ec8b5c2-01e6-4fbe-ada7-43898db63bbe
ms.topic: article
ms.date: 05/31/2018
---

# Migrating to Direct3D 11

This section provides info for migrating to Direct3D 11 from an earlier version of Direct3D.

-   [Direct3D 9 to Direct3D 11](#direct3d-9-to-direct3d-11)
-   [Direct3D 10 to Direct3D 11](#direct3d-10-to-direct3d-11)
    -   [Enumerations and Defines](#enumerations-and-defines)
    -   [Structures](#structures)
    -   [Interfaces](#interfaces)
    -   [Other Related Technologies](#other-related-technologies)
-   [Direct3D 10.1 to Direct3D 11](#direct3d-101-to-direct3d-11)
    -   [Enumerations and Defines](#enumerations-and-defines)
    -   [Structures](#structures)
    -   [Interfaces](#interfaces)
-   [New Features for Direct3D 11](#new-features-for-direct3d-11)
-   [New Features for DirectX 11.1](#new-features-for-directx-111)
-   [New Features for DirectX 11.2](#new-features-for-directx-112)
-   [Related topics](#related-topics)

## Direct3D 9 to Direct3D 11

The Direct3D 11 API builds on the infrastructural improvements made in Direct3D 10 and 10.1. Porting from Direct3D 9 to Direct3D 11 is similar to moving from Direct3D 9 to Direct3D 10. The following are the key challenges in this effort.

-   Removal of all fixed function pipeline usage in favor of programmable shaders authored exclusively in HLSL (compiled via D3DCompiler instead of D3DX9).
-   State management based on immutable objects rather than individual state toggles.
-   Updating to comply with strict linkage requirements of vertex buffer input layouts and shader signatures.
-   Associating shader resource views with all texture resources.
-   Mapping all image content to a DXGI\_FORMAT, including the removal of all 16-bit color formats (5/5/5/1, 5/6/5, 4/4/4/4), removal of all 24-bit color formats (8/8/8), and strict RGB color ordering.
-   Breaking up global constant state usage into several small, more efficiently updated constant buffers.

For more information about moving from Direct3D 9 to Direct3D 10, see [Direct3D 9 to Direct3D 10 Considerations](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-d3d9-to-d3d10-considerations).

## Direct3D 10 to Direct3D 11

Converting programs written to use the Direct3D 10 or 10.1 API is a straight-forward process as Direct3D 11 is an extension of the existing API. With only one minor exception (noted below - monochrome text filtering), all methods and functionality in Direct3D 10/10.1 is available in Direct3D 11. The outline below describes the differences between the two APIs to aid in updating existing code. The key differences here include:

-   Rendering operations (Draw, state, etc.) are no longer part of the Device interface, but are instead part of the new DeviceContext interface along with resource Map/Unmap and device query methods.
-   Direct3D 11 includes all enhancements and changes made between Direct3D 10.0 and 10.1

### Enumerations and Defines



| Direct3D 10                            | Direct3D 11                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DXGI\_FORMAT                           | [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)Several new DXGI formats were defined.<br/>                                                                                                                                                                                                                                                                                                                                |
| D3D10\_CREATE\_DEVICE\_SWITCH\_TO\_REF | [**D3D11\_CREATE\_DEVICE\_SWITCH\_TO\_REF**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_create_device_flag)The switch-to-ref functionality is not supported by Direct3D 11.<br/>                                                                                                                                                                                                                                                                        |
| D3D10\_DRIVER\_TYPE                    | [**D3D\_DRIVER\_TYPE**](/windows/desktop/api/D3DCommon/ne-d3dcommon-d3d_driver_type)Note that the enumeration identifiers in [**D3D\_DRIVER\_TYPE**](/windows/desktop/api/D3DCommon/ne-d3dcommon-d3d_driver_type) were redefined from the identifiers in [**D3D10\_DRIVER\_TYPE**](/windows/desktop/api/d3d10misc/ne-d3d10misc-d3d10_driver_type). Therefore, you should be sure to use the enumeration identifiers instead of literal numbers.<br/> [**D3D\_DRIVER\_TYPE**](/windows/desktop/api/D3DCommon/ne-d3dcommon-d3d_driver_type) is defined in D3Dcommon.h.<br/> |
| D3D10\_RESOURCE\_MISC\_FLAG            | [**D3D11\_RESOURCE\_MISC\_FLAG**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag)Note that many of these flags were redefined, so be sure to use enumeration identifiers instead of literal numbers.<br/>                                                                                                                                                                                                                                |
| D3D10\_FILTER                          | [**D3D11\_FILTER**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_filter)Note that text filtering D3D10\_FILTER\_TEXT\_1BIT was removed from Direct3D 11. See DirectWrite.<br/>                                                                                                                                                                                                                                                                            |
| D3D11\_COUNTER                         | [**D3D11\_COUNTER**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_counter)Note that the vendor-neutral counters were removed for Direct3D 11 as they were rarely supported.<br/>                                                                                                                                                                                                                                                                          |
| D3D10\_x                               | D3D11\_x Many enumerations and defines are the same, have larger limits, or have additional values.<br/>                                                                                                                                                                                                                                                                                                               |



 

### Structures



| Direct3D 10                              | Direct3D 11                                                                                                                                                 |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_SO\_DECLARATION\_ENTRY            | [**D3D11\_SO\_DECLARATION\_ENTRY**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_so_declaration_entry)Adds Stream.<br/>                                                                  |
| D3D10\_BLEND\_DESC                       | [**D3D11\_BLEND\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_blend_desc)Note this structure changed significantly from 10 to 10.1 to provide per render target blend state<br/> |
| D3D10\_BUFFER\_DESC                      | [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc)Adds a StructureByteStride for use with Compute Shader resources<br/>                                 |
| D3D10\_SHADER\_RESOURCE\_VIEW\_DESC      | [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_shader_resource_view_desc)Note this structure had additional union members added for 10.1<br/>    |
| D3D10\_DEPTH\_STENCIL\_VIEW\_DESC        | [**D3D11\_DEPTH\_STENCIL\_VIEW\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencil_view_desc)Has a new Flags member.<br/>                                                |
| D3D10\_QUERY\_DATA\_PIPELINE\_STATISTICS | [**D3D11\_QUERY\_DATA\_PIPELINE\_STATISTICS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_query_data_pipeline_statistics)Adds several new shader stage counters.<br/>                  |
| D3D10\_x                                 | D3D11\_x Many structures are identical between the two APIs.<br/>                                                                                     |



 

### Interfaces



| Direct3D 10        | Direct3D 11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID3D10Device       | [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)<br/> The device interface was split into these two parts. For quick porting you can make use of [**ID3D11Device::GetImmediateContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-getimmediatecontext).<br/> "ID3D10Device::GetTextFilterSize" and "SetTextFilerSize" methods no longer exist. See DirectWrite.<br/> Create\*Shader takes an additional optional parameter for [**ID3D11ClassLinkage**](/windows/desktop/api/D3D11/nn-d3d11-id3d11classlinkage).<br/> \*SetShader and \*GetShader take additional optional parameters for [**ID3D11ClassInstance**](/windows/desktop/api/D3D11/nn-d3d11-id3d11classinstance)(s).<br/> [**CreateGeometryShaderWithStreamOutput**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput) takes an array and count for multiple output stream strides.<br/> The limit for the NumEntries parameter of [**CreateGeometryShaderWithStreamOutput**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput) has increased to D3D11\_SO\_STREAM\_COUNT \* D3D11\_SO\_OUTPUT\_COMPONENT\_COUNT in Direct3D 11.<br/> |
| ID3D10Buffer       | [**ID3D11Buffer**](/windows/desktop/api/D3D11/nn-d3d11-id3d11buffer)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ID3D10SwitchToRef  | [**ID3D11SwitchToRef**](/windows/desktop/api/D3D11SDKLayers/nn-d3d11sdklayers-id3d11switchtoref)Switch-to-ref functionality is not supported in Direct3D 11.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ID3D10Texture1D    | [**ID3D11Texture1D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture1d)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ID3D10Texture2D    | [**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ID3D10Texture3D    | [**ID3D11Texture3D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture3d)The Map and Unmap methods were moved to [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext), and all Map methods use [**D3D11\_MAPPED\_SUBRESOURCE**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_mapped_subresource) instead of a void\*\*.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ID3D10Asynchronous | [**ID3D11Asynchronous**](/windows/desktop/api/D3D11/nn-d3d11-id3d11asynchronous)Begin, End, and GetData were moved to [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ID3D10x            | ID3D11x Many interfaces are identical between the two APIs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

### Other Related Technologies




| 10/10.1 Solution | 11 Solution | 
|------------------|-------------|
| HLSL Complier (D3D10Compile*, D3DX10Compile*) and shader reflection APIs | D3DCompiler (see D3DCompiler.h)<blockquote>[!Note]<br />For Windows Store apps, the <a href="/windows/desktop/direct3dhlsl/dx-graphics-d3dcompiler-reference">D3DCompiler APIs</a> are supported only for development, not deployment.</blockquote><br /> | 
| Effects 10 | <a href="https://github.com/Microsoft/FX11">Effects 11</a> is available as shared source online.<blockquote>[!Note]<br />This solution is not suited to Windows Store apps because it requires the <a href="/windows/desktop/direct3dhlsl/dx-graphics-d3dcompiler-reference">D3DCompiler APIs</a> at runtime (deployment).</blockquote><br /> | 
| D3DX9/D3DX10 Math | <a href="/windows/desktop/dxmath/directxmath-portal">DirectXMath</a> | 
| D3DX10 | D3DX11 in the legacy DirectX SDK <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a>, <a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a>, and <a href="https://github.com/Microsoft/DirectXMesh">DirectXMesh</a> offer alternatives to many technologies in the legacy D3DX10 and D3DX11 libraries.<br /><a href="/windows/desktop/Direct2D/direct2d-portal">Direct2D</a> and <a href="/windows/desktop/DirectWrite/direct-write-portal">DirectWrite</a> offer high-quality support for rendering styled lines and fonts.<br /> | 




 

For info about the legacy DirectX SDK, see [Where is the DirectX SDK?](/windows/desktop/directx-sdk--august-2009-).

## Direct3D 10.1 to Direct3D 11

Direct3D 10.1 is an extension of the Direct3D 10 interface, and all features of Direct3D 10.1 are available in Direct3D 11. Most of the porting from 10.1 to 11 is already addressed above moving from 10 to 11.

### Enumerations and Defines



| Direct3D 10.1          | Direct3D 11                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_FEATURE\_LEVEL1 | [**D3D\_FEATURE\_LEVEL**](/windows/desktop/api/D3DCommon/ne-d3dcommon-d3d_feature_level)Identical but defined in D3DCommon.h plus the addition of D3D\_FEATURE\_LEVEL\_11\_0 for 11 class hardware along with D3D\_FEATURE\_LEVEL\_9\_1, D3D\_FEATURE\_LEVEL\_9\_2, and D3D\_FEATURE\_LEVEL\_9\_3 for 10level9<br/> (D3D10\_FEATURE\_LEVEL\_9\_1, D3D10\_FEATURE\_LEVEL\_9\_2, and D3D10\_FEATURE\_LEVEL\_9\_3 were also added for 10.1 to d3d10\_1.h)<br/> |



 

### Structures



| Direct3D 10.1                        | Direct3D 11                                                                                                                   |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_BLEND\_DESC1                  | [**D3D11\_BLEND\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_blend_desc)The 11 version is identical to 10.1.<br/>                                 |
| D3D10\_SHADER\_RESOURCE\_VIEW\_DESC1 | [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_shader_resource_view_desc)The 11 version is identical to 10.1.<br/> |



 

### Interfaces



| Direct3D 10.1             | Direct3D 11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID3D10Device1             | [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)<br/> The device interface was split into these two parts. For quick porting you can make use of [**ID3D11Device::GetImmediateContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-getimmediatecontext).<br/> " ID3D10Device::GetTextFilterSize" and "SetTextFilerSize" methods no longer exist. See DirectWrite.<br/> Create\*Shader takes an additional optional parameter for [**ID3D11ClassLinkage**](/windows/desktop/api/D3D11/nn-d3d11-id3d11classlinkage).<br/> \*SetShader and \*GetShader take additional optional parameters for [**ID3D11ClassInstance**](/windows/desktop/api/D3D11/nn-d3d11-id3d11classinstance)(s).<br/> [**CreateGeometryShaderWithStreamOutput**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput) takes an array and count for multiple output stream strides.<br/> The limit for the NumEntries parameter of [**CreateGeometryShaderWithStreamOutput**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput) has increased to D3D11\_SO\_STREAM\_COUNT \* D3D11\_SO\_OUTPUT\_COMPONENT\_COUNT in Direct3D 11.<br/> |
| ID3D10BlendState1         | [**ID3D11BlendState**](/windows/desktop/api/D3D11/nn-d3d11-id3d11blendstate)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ID3D10ShaderResourceView1 | [**ID3D11ShaderResourceView**](/windows/desktop/api/D3D11/nn-d3d11-id3d11shaderresourceview)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## New Features for Direct3D 11

Once your code is updated to use the Direct3D 11 API, there are numerous [new features](direct3d-11-features.md) to consider.

-   Multithreaded rendering through command lists and multiple contexts
-   Implementing advanced algorithms using Compute Shader (using 4.0, 4.1, or 5.0 shader profiles)
-   New 11 class hardware features:
    -   HLSL Shader Model 5.0
    -   Dynamic Shader Linkage
    -   Tessellation through Hull and Domain shaders
    -   New block compression formats: BC6H for HDR images, BC7 for higher-fidelity standard images
-   Utilizing [10level9 technology](overviews-direct3d-11-devices-downlevel.md) for rendering on many Shader Model 2.0 and Shader Model 3.0 devices through the DIrect3D 11 API for lower-end video hardware support on Windows Vista and Windows 7.
-   Leveraging the WARP software rendering device.

## New Features for DirectX 11.1

Windows 8 includes further DirectX graphics enhancements to consider when you implement your DirectX graphics code, which include [Direct3D 11.1](direct3d-11-features.md), [DXGI 1.2](/windows/desktop/direct3ddxgi/dxgi-1-2-improvements), [Windows Display Driver Model (WDDM) 1.2](/windows-hardware/drivers/display/wddm-in-windows-8), [feature level](overviews-direct3d-11-devices-downlevel-intro.md) 11.1 hardware, Direct2D device contexts, and other improvements.

Partial support for [Direct3D 11.1](direct3d-11-features.md) is available on Windows 7 as well via the [Platform Update for Windows 7](/windows/desktop/direct3darticles/platform-update-for-windows-7), which is available through the [Platform Update for Windows 7](https://support.microsoft.com/kb/2670838).

## New Features for DirectX 11.2

The Windows 8.1 includes [Direct3D 11.2](direct3d-11-2-features.md), [DXGI 1.3](/windows/desktop/direct3ddxgi/dxgi-1-3-improvements), and other improvements.

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 11](dx-graphics-overviews.md)
</dt> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

