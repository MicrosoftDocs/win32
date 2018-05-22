---
Description: 'This section covers how to check on Format Support for Direct3D Feature Level Hardware using API calls.'
ms.assetid: '0C40C73E-06F3-41FA-AA27-2C0B730B357B'
title: Checking Hardware Feature Support
---

# Checking Hardware Feature Support

This section covers how to check on Format Support for Direct3D Feature Level Hardware using API calls.

For D3D11, use [**ID3D11Device::CheckFormatSupport**](https://msdn.microsoft.com/library/windows/desktop/ff476498) to programmatically verify the info in the previous sections. For D3D12 use [**ID3D12::CheckFeatureSupport**](https://msdn.microsoft.com/library/windows/desktop/dn788653).



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Format target</th>
<th>D3D12</th>
<th>D3D11</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Buffer</td>
<td>D3D12_FORMAT_SUPPORT1_BUFFER ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_BUFFER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Input Assembler Vertex Buffer</td>
<td>D3D12_FORMAT_SUPPORT1_IA_VERTEX_BUFFER ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_IA_VERTEX_BUFFER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Input Assembler Index Buffer</td>
<td>D3D12_FORMAT_SUPPORT1_IA_INDEX_BUFFER ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_IA_INDEX_BUFFER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Stream Output Buffer</td>
<td>D3D12_FORMAT_SUPPORT1_SO_BUFFER ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SO_BUFFER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Texture1D</td>
<td>D3D12_FORMAT_SUPPORT1_TEXTURE1D ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_TEXTURE1D ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Texture2D</td>
<td>D3D12_FORMAT_SUPPORT1_TEXTURE2D ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_TEXTURE2D ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Texture3D</td>
<td>D3D12_FORMAT_SUPPORT1_TEXTURE3D ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_TEXTURE3D ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>TextureCube</td>
<td>D3D12_FORMAT_SUPPORT1_TEXTURECUBE ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_TEXTURECUBE ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Shader ld</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_LOAD ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_LOAD ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Shader sample (any filter)</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_SAMPLE ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Shader sample_c (comparison filter)</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE_COMPARISON ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_SAMPLE_COMPARISON ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Shader sample (mono 1_bit_filter)</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE_MONO_TEXT ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_SAMPLE_MONO_TEXT ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Shader gather4</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_GATHER ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_GATHER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Shader gather4_c</td>
<td>D3D12_FORMAT_SUPPORT1_SHADER_GATHER_COMPARISON ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_SHADER_GATHER_COMPARISON ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Mipmap</td>
<td>D3D12_FORMAT_SUPPORT1_MIP ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MIP ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Mipmap Auto-Generation</td>
<td><blockquote>
[!Note]<br />
D3D12 no longer has a dedicated mipmap generation functionality. Applications must implement it on their own using shaders.
</blockquote>
<br/></td>
<td>D3D11_FORMAT_SUPPORT_MIP_AUTOGEN ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>RenderTarget</td>
<td>D3D12_FORMAT_SUPPORT1_RENDER_TARGET ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_RENDER_TARGET ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Blendable RenderTarget</td>
<td>D3D12_FORMAT_SUPPORT1_BLENDABLE ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_BLENDABLE ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Output Merger Logic Op</td>
<td>D3D12_FORMAT_SUPPORT2_OUTPUT_MERGER_LOGIC_OP</td>
<td>D3D11_FORMAT_SUPPORT2_OUTPUT_MERGER_LOGIC_OP ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>Depth/Stencil Target</td>
<td>D3D12_FORMAT_SUPPORT1_DEPTH_STENCIL ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_DEPTH_STENCIL ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Raw UAV and SRV</td>


</tr>
<tr class="even">
<td>Structured UAV and SRV</td>


</tr>
<tr class="odd">
<td>Typed UAV</td>
<td>D3D12_FORMAT_SUPPORT1_TYPED_UNORDERED_ACCESS_VIEW ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_TYPED_UNORDERED_ACCESS_VIEW ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>UAV Typed Store</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_TYPED_STORE ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_TYPED_STORE ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="odd">
<td>UAV Typed Load</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_TYPED_LOAD ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_TYPED_LOAD ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>UAV Atomic Add</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_ADD ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_ADD ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="odd">
<td>UAV Atomic Bitwise Ops</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_BITWISE_OPS ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_BITWISE_OPS ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>UAV Atomic Cmp&amp;Store/ Cmp&amp;Exch</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_COMPARE_STORE_OR_COMPARE_EXCHANGE ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_COMPARE_STORE_OR_COMPARE_EXCHANGE ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="odd">
<td>UAV Atomic Exchange</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_EXCHANGE ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_EXCHANGE ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>UAV Atomic Signed Min/Max</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_SIGNED_MIN_OR_MAX ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_SIGNED_MIN_OR_MAX ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="odd">
<td>UAV Atomic Unsigned Min/Max</td>
<td>D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_UNSIGNED_MIN_OR_MAX ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_UNSIGNED_MIN_OR_MAX ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>CPU Lockable</td>
<td><blockquote>
[!Note]<br />
Only a single format precludes cpu access (420_OPAQUE).
</blockquote>
<br/></td>
<td>D3D11_FORMAT_SUPPORT_CPU_LOCKABLE ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>4x Multisample RenderTarget</td>
<td>D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RENDERTARGET ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>8x Multisample RenderTarget</td>
<td>D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RENDERTARGET ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Other Multisample Count RT</td>
<td>D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RENDERTARGET ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Multisample Resolve</td>
<td>D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RESOLVE ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MULTISAMPLE_RESOLVE ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Multisample Load</td>
<td>D3D12_FORMAT_SUPPORT1_MULTISAMPLE_LOAD ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_MULTISAMPLE_LOAD ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Display Scan-Out</td>
<td>D3D12_FORMAT_SUPPORT1_DISPLAY ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_DISPLAY ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Cast Within Bit Layout</td>
<td>D3D12_FORMAT_SUPPORT1_CAST_WITHIN_BIT_LAYOUT ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_CAST_WITHIN_BIT_LAYOUT ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Video Decoder Support</td>
<td>D3D12_FORMAT_SUPPORT1_DECODER_OUTPUT ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_DECODER_OUTPUT ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Video Processor Input</td>
<td>D3D12_FORMAT_SUPPORT1_VIDEO_PROCESSOR_INPUT ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_VIDEO_PROCESSOR_INPUT ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="even">
<td>Video Processor Output</td>
<td>D3D12_FORMAT_SUPPORT1_VIDEO_PROCESSOR_OUTPUT ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_VIDEO_PROCESSOR_OUTPUT ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Shared Resource</td>
<td><blockquote>
[!Note]<br />
Textures of all formats may be shared committed resources or be placed in shared heaps.
</blockquote>
<br/></td>
<td>D3D11_FORMAT_SUPPORT2_SHAREABLE ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>BackBuffer Castable Even Fully Typed</td>
<td>D3D12_FORMAT_SUPPORT1_BACK_BUFFER_CAST ([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td><blockquote>
[!Note]<br />
No API available.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Tiled Resource</td>
<td>D3D12_FORMAT_SUPPORT2_TILED ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_TILED ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
<tr class="even">
<td>Video Encoder</td>
<td>D3D12_FORMAT_SUPPORT1_VIDEO_ENCODER([<strong>D3D12_FORMAT_SUPPORT1</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859389))</td>
<td>D3D11_FORMAT_SUPPORT_VIDEO_ENCODER ([<strong>D3D11_FORMAT_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476134#d3d11-format-support-buffer))</td>
</tr>
<tr class="odd">
<td>Multiplane Overlay</td>
<td>D3D12_FORMAT_SUPPORT2_MULTIPLANE_OVERLAY ([<strong>D3D12_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/dn859390))</td>
<td>D3D11_FORMAT_SUPPORT2_MULTIPLANE_OVERLAY ([<strong>D3D11_FORMAT_SUPPORT2</strong>](https://msdn.microsoft.com/library/windows/desktop/ff476135))</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[D3D12 Hardware Feature Levels](https://msdn.microsoft.com/library/windows/desktop/mt186615)
</dt> <dt>

[**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)
</dt> <dt>

[**D3D11\_FORMAT\_SUPPORT**](https://msdn.microsoft.com/library/windows/desktop/ff476134)
</dt> <dt>

[**D3D11\_FORMAT\_SUPPORT2**](https://msdn.microsoft.com/library/windows/desktop/ff476135)
</dt> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 




