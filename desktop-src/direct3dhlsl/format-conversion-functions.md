---
title: Format conversion functions (HLSL reference)
description: The section contains the format conversion functions used in Compute and Pixel Shaders.
ms.assetid: 05575ee8-4428-437f-bfb6-e5c676405d65
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- apiref
api_name:
api_type:
api_location:
---

# Format conversion functions (HLSL reference)

The section contains the format conversion functions used in Compute and Pixel Shaders.

-   [Converter Functions](#converter-functions)
-   [Related topics](#related-topics)

> The D3DX_DXGIFormatConvert.inl header ships in the legacy DirectX SDK and relied on XNAMath for C++ support. It is also included in the [Microsoft.DXSDK.D3DX](https://www.nuget.org/packages/Microsoft.DXSDK.D3DX) NuGet package. The latest version uses DirectXMath for C++ support, and all functions are defined in the **DirectX** C++ namespace.

## Converter Functions

### DXGI\_FORMAT\_R10G10B10A2\_UNORM

<dl>

[**D3DX\_R10G10B10A2\_UNORM\_to\_FLOAT4**](d3dx-r10g10b10a2-unorm-to-float4.md)  
[**D3DX\_FLOAT4\_to\_R10G10B10A2\_UNORM**](d3dx-float4-to-r10g10b10a2-unorm.md)  
</dl>

### DXGI\_FORMAT\_R10G10B10A2\_UINT

<dl>

[**D3DX\_R10G10B10A2\_UINT\_to\_UINT4**](d3dx-r10g10b10a2-uint-to-uint4.md)  
[**D3DX\_UINT4\_to\_R10G10B10A2\_UINT**](d3dx-uint4-to-r10g10b10a2-uint.md)  
</dl>

### DXGI\_FORMAT\_R8G8B8A8\_UNORM:

<dl>

[**D3DX\_R8G8B8A8\_UNORM\_to\_FLOAT4**](d3dx-r8g8b8a8-unorm-to-float4.md)  
[**D3DX\_FLOAT4\_to\_R8G8B8A8\_UNORM**](d3dx-float4-to-r8g8b8a8-unorm.md)  
</dl>

### DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB

<dl>

[**D3DX\_R8G8B8A8\_UNORM\_SRGB\_to\_FLOAT4\_inexact**](d3dx-r8g8b8a8-unorm-srgb-to-float4-inexact.md)  
[**D3DX\_R8G8B8A8\_UNORM\_SRGB\_to\_FLOAT4**](d3dx-r8g8b8a8-unorm-srgb-to-float4.md)  
[**D3DX\_FLOAT4\_to\_R8G8B8A8\_UNORM\_SRGB**](d3dx-float4-to-r8g8b8a8-unorm-srgb.md)  
</dl>

### DXGI\_FORMAT\_R8G8B8A8\_UINT

<dl>

[**D3DX\_R8G8B8A8\_UINT\_to\_UINT4**](d3dx-r8g8b8a8-uint-to-uint4.md)  
[**D3DX\_UINT4\_to\_R8G8B8A8\_UINT**](d3dx-uint4-to-r8g8b8a8-uint.md)  
</dl>

### DXGI\_FORMAT\_R8G8B8A8\_SNORM

<dl>

[**D3DX\_R8G8B8A8\_SNORM\_to\_FLOAT4**](d3dx-r8g8b8a8-snorm-to-float4.md)  
[**D3DX\_FLOAT4\_to\_R8G8B8A8\_SNORM**](d3dx-float4-to-r8g8b8a8-snorm.md)  
</dl>

### DXGI\_FORMAT\_R8G8B8A8\_SINT

<dl>

[**D3DX\_R8G8B8A8\_SINT\_to\_INT4**](d3dx-r8g8b8a8-sint-to-int4.md)  
[**D3DX\_INT4\_to\_R8G8B8A8\_SINT**](d3dx-int4-to-r8g8b8a8-sint.md)  
</dl>

### DXGI\_FORMAT\_B8G8R8A8\_UNORM

<dl>

[**D3DX\_B8G8R8A8\_UNORM\_to\_FLOAT4**](d3dx-b8g8r8a8-unorm-to-float4.md)  
[**D3DX\_FLOAT4\_to\_B8G8R8A8\_UNORM**](d3dx-float4-to-b8g8r8a8-unorm.md)  
</dl>

### DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB

<dl>

[**D3DX\_B8G8R8A8\_UNORM\_SRGB\_to\_FLOAT4\_inexact**](d3dx-b8g8r8a8-unorm-srgb-to-float4-inexact.md)  
[**D3DX\_B8G8R8A8\_UNORM\_SRGB\_to\_FLOAT4**](d3dx-b8g8r8a8-unorm-srgb-to-float4.md)  
[**D3DX\_FLOAT4\_to\_R8G8B8A8\_UNORM\_SRGB**](d3dx-float4-to-r8g8b8a8-unorm-srgb.md)  
</dl>

### DXGI\_FORMAT\_B8G8R8X8\_UNORM

<dl>

[**D3DX\_B8G8R8X8\_UNORM\_to\_FLOAT3**](d3dx-b8g8r8x8-unorm-to-float3.md)  
[**D3DX\_FLOAT3\_to\_B8G8R8X8\_UNORM**](d3dx-float3-to-b8g8r8x8-unorm.md)  
</dl>

### DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB

<dl>

[**D3DX\_B8G8R8X8\_UNORM\_SRGB\_to\_FLOAT3\_inexact**](d3dx-b8g8r8x8-unorm-srgb-to-float3-inexact.md)  
[**D3DX\_B8G8R8X8\_UNORM\_SRGB\_to\_FLOAT3**](d3dx-b8g8r8x8-unorm-srgb-to-float3.md)  
[**D3DX\_FLOAT3\_to\_B8G8R8X8\_UNORM\_SRGB**](d3dx-float3-to-b8g8r8x8-unorm-srgb.md)  
</dl>

### DXGI\_FORMAT\_R16G16\_FLOAT

<dl>

[**D3DX\_R16G16\_FLOAT\_to\_FLOAT2**](d3dx-r16g16-float-to-float2.md)  
[**D3DX\_FLOAT2\_to\_R16G16\_FLOAT**](d3dx-float2-to-r16g16-float.md)  
</dl>

### DXGI\_FORMAT\_R16G16\_UNORM

<dl>

[**D3DX\_R16G16\_UNORM\_to\_FLOAT2**](d3dx-r16g16-unorm-to-float2.md)  
[**D3DX\_FLOAT2\_to\_R16G16\_UNORM**](d3dx-float2-to-r16g16-unorm.md)  
</dl>

### DXGI\_FORMAT\_R16G16\_UINT

<dl>

[**D3DX\_R16G16\_UINT\_to\_UINT2**](d3dx-r16g16-uint-to-uint2.md)  
[**D3DX\_UINT2\_to\_R16G16\_UINT**](d3dx-uint2-to-r16g16-uint.md)  
</dl>

### DXGI\_FORMAT\_R16G16\_SNORM

<dl>

[**D3DX\_R16G16\_SNORM\_to\_FLOAT2**](d3dx-r16g16-snorm-to-float2.md)  
[**D3DX\_FLOAT2\_to\_R16G16\_SNORM**](d3dx-float2-to-r16g16-snorm.md)  
</dl>

### DXGI\_FORMAT\_R16G16\_SINT

<dl>

[**D3DX\_R16G16\_SINT\_to\_INT2**](d3dx-r16g16-sint-to-int2.md)  
[**D3DX\_INT2\_to\_R16G16\_SINT**](d3dx-int2-to-r16g16-sint.md)  
</dl>

## Related topics

<dl> <dt>

[Inline Format Conversion Reference](inline-format-conversion-reference.md)
</dt> <dt>

[Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md)
</dt> </dl>

 

 
