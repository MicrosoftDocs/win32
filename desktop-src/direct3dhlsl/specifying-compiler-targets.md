---
title: Specifying Compiler Targets
description: Here we list the targets for various profiles that the D3DCompile\ functions and the HLSL compiler support.
ms.assetid: 594E1C14-C1D4-4207-91A1-28892CE6D821
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Compiler Targets

You need to specify the shader target — set of shader features — to compile against when you call the [**D3DCompile**](d3dcompile.md), [**D3DCompile2**](d3dcompile2.md), or [**D3DCompileFromFile**](d3dcompilefromfile.md) function. Here we list the targets for various profiles that the **D3DCompile\*** functions and the HLSL compiler support.

-   [Direct3D 11.0 and 11.1 feature levels](#direct3d-110-and-111-feature-levels)
-   [Direct3D 10.1 feature level](#direct3d-101-feature-level)
-   [Direct3D 10.0 feature level](#direct3d-100-feature-level)
-   [Direct3D 9.1, 9.2, and 9.3 feature levels](#direct3d-91-92-and-93-feature-levels)
-   [Legacy Direct3D 9 Shader Model 3.0](#legacy-direct3d-9-shader-model-30)
-   [Legacy Direct3D 9 Shader Model 2.0](#legacy-direct3d-9-shader-model-20)
-   [Legacy Direct3D 9 Shader Model 1.x](#legacy-direct3d-9-shader-model-1x)
-   [Legacy Effects](#legacy-effects)
-   [Notes](#notes)
-   [Related topics](#related-topics)

## Direct3D 11.0 and 11.1 feature levels

Here are the shader targets that Direct3D 11.0 and 11.1 [feature levels](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) support.



| Target   | Description                                                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| cs\_5\_0 | DirectCompute 5.0 ([compute shader](https://msdn.microsoft.com/library/windows/desktop/ff476331))                              |
| ds\_5\_0 | [Domain shader](https://msdn.microsoft.com/library/windows/desktop/ff476340#domain-shader-stage)             |
| gs\_5\_0 | [Geometry shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#geometry-shader-stage) |
| hs\_5\_0 | [Hull shader](https://msdn.microsoft.com/library/windows/desktop/ff476340#hull-shader-stage)                   |
| ps\_5\_0 | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage)          |
| vs\_5\_0 | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage)       |



 

## Direct3D 10.1 feature level

Here are the shader targets that the Direct3D 10.1 [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) supports.



| Target   | Description                                                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| cs\_4\_1 | DirectCompute 4.1 ([compute shader](https://msdn.microsoft.com/library/windows/desktop/ff476331))¹                             |
| gs\_4\_1 | [Geometry shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#geometry-shader-stage) |
| ps\_4\_1 | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage)          |
| vs\_4\_1 | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage)       |



 

## Direct3D 10.0 feature level

Here are the shader targets that the Direct3D 10.0 [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) supports.



| Target   | Description                                                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| cs\_4\_0 | DirectCompute 4.0 ([compute shader](https://msdn.microsoft.com/library/windows/desktop/ff476331))¹                             |
| gs\_4\_0 | [Geometry shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#geometry-shader-stage) |
| ps\_4\_0 | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage)          |
| vs\_4\_0 | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage)       |



 

## Direct3D 9.1, 9.2, and 9.3 feature levels

Here are the shader targets that Direct3D 9.1, 9.2 and 9.3 [feature levels](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) support.

> [!Note]  
> When you use the \*\_4\_0\_level\_9\_x HLSL shader profiles, you implicitly use of the [Shader Model 2.x](dx-graphics-hlsl-sm2.md) profiles to support Direct3D 9 capable hardware. Shader Model 2.x profiles support more limited flow control behavior than the [Shader Model 4.x](dx-graphics-hlsl-sm4.md) and later profiles.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Target</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ps_4_0_level_9_1</td>
<td>[Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) for 9.1 and 9.2 (similar limits to ps_2_0)
<ul>
<li>64 arithmetic and 32 texture instructions</li>
<li>12 temporary registers</li>
<li>4 levels of dependent reads</li>
</ul></td>
</tr>
<tr class="even">
<td>ps_4_0_level_9_3</td>
<td>[Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) for 9.3 (similar limits to ps_2_x² with additional shader features)
<ul>
<li>512 instructions</li>
<li>32 temporary registers</li>
<li>Static flow control (max depth of 4)</li>
<li>Dynamic flow control (max depth of 24)</li>
<li>D3DPS20CAPS_ARBITRARYSWIZZLE</li>
<li>D3DPS20CAPS_GRADIENTINSTRUCTIONS</li>
<li>D3DPS20CAPS_PREDICATION</li>
<li>D3DPS20CAPS_NODEPENDENTREADLIMIT</li>
<li>D3DPS20CAPS_NOTEXINSTRUCTIONLIMIT</li>
</ul></td>
</tr>
<tr class="odd">
<td>vs_4_0_level_9_1</td>
<td>[Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) for 9.1 and 9.2 (similar to vs_2_0)
<ul>
<li>256 instructions</li>
<li>12 temporary registers</li>
<li>Static flow control (max depth of 1)</li>
</ul></td>
</tr>
<tr class="even">
<td>vs_4_0_level_9_3</td>
<td>[Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) for 9.3 (similar to vs_2_a² with additional shader features and instancing)
<ul>
<li>256 instructions</li>
<li>32 temporary registers</li>
<li>Static flow control (max depth of 4)</li>
<li>D3DVS20CAPS_PREDICATION</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Legacy Direct3D 9 Shader Model 3.0

Here are the shader targets for legacy Direct3D 9 shader model 3.0³.



| Target    | Description                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| ps\_3\_0  | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 3.0               |
| ps\_3\_sw | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 3.0 (software)    |
| vs\_3\_0  | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 3.0            |
| vs\_3\_sw | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 3.0 (software) |



 

## Legacy Direct3D 9 Shader Model 2.0

Here are the shader targets for legacy Direct3D 9 shader model 2.0³.



| Target    | Description                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| ps\_2\_0  | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 2.0             |
| ps\_2\_a  | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 2a              |
| ps\_2\_b  | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 2b              |
| ps\_2\_sw | [Pixel shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#pixel-shader-stage) 2.0 software    |
| vs\_2\_0  | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 2.0          |
| vs\_2\_a  | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 2a           |
| vs\_2\_sw | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 2.0 software |



 

## Legacy Direct3D 9 Shader Model 1.x

Here are the shader targets for legacy Direct3D 9 shader model 1.x⁴.



| Target   | Description                                                                                                                                                                       |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tx\_1\_0 | Texture shader profile that legacy D3DX9⁵ functions [**D3DXCreateTextureShader**](https://msdn.microsoft.com/library/windows/desktop/bb172808) and [**D3DXFillTextureTX**](https://msdn.microsoft.com/library/windows/desktop/bb172834) use |
| vs\_1\_1 | [Vertex shader](https://msdn.microsoft.com/library/windows/desktop/bb205146#vertex-shader-stage) 1.1                                                            |



 

## Legacy Effects

Here are the effect targets for legacy effects.



| Target   | Description                               |
|----------|-------------------------------------------|
| fx\_2\_0 | Effects (FX) for Direct3D 9 in D3DX9⁵     |
| fx\_4\_0 | Effects (FX) for Direct3D 10.0 in D3DX10⁵ |
| fx\_4\_1 | Effects (FX) for Direct3D 10.1 in D3DX10⁵ |
| fx\_5\_0 | Effects (FX) for Direct3D 11⁵             |



 

## Notes

Here are some notes that the preceding sections refer to:

1.  [Feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) 10.0 and 10.1 devices can optionally support DirectCompute. To verify support, use [**ID3D11Device::CheckFeatureSupport**](https://msdn.microsoft.com/library/windows/desktop/ff476497) with [**D3D11\_FEATURE\_D3D10\_X\_HARDWARE\_OPTIONS**](https://msdn.microsoft.com/library/windows/desktop/ff476124#d3d11-feature-d3d10-x-hardware-options).
2.  [Feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) 9.3 effectively requires hardware that complies with the requirements for [legacy Direct3D 9 shader model 3.0](#legacy-direct3d-9-shader-model-30), but this feature level does not make use of vs\_3\_0 or ps\_3\_0 targets.
3.  Only use legacy Direct3D 9 shader models with the Direct3D 9 API. Instead, use the 9.x profiles with the Direct3D 10.x and 11.x API.
4.  The current HLSL shader **D3DCompile\*** functions don't support legacy 1.x pixel shaders. The last version of HLSL to support these targets was D3DX9 in the October 2006 release of the DirectX SDK.
5.  All versions of D3DX and the DirectX SDK are deprecated. For more info, see [Where is the DirectX SDK?](https://msdn.microsoft.com/library/windows/desktop/ee663275).

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 




