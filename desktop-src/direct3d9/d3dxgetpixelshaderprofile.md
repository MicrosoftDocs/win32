---
description: Returns the name of the highest high-level shader language (HLSL) profile supported by a given device.
ms.assetid: a6c1be4e-f6f5-4f08-b6a7-b9c621e5f19b
title: D3DXGetPixelShaderProfile function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXGetPixelShaderProfile
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXGetPixelShaderProfile function

Returns the name of the highest high-level shader language (HLSL) profile supported by a given device.

## Syntax


```C++
LPCSTR D3DXGetPixelShaderProfile(
  _In_ LPDIRECT3DDEVICE9 pDevice
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to the device. See [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9).

</dd> </dl>

## Return value

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

The HLSL profile name.

If the device does not support pixel shaders then the function returns **NULL**.

## Remarks

A shader profile specifies the assembly shader version to use and the capabilities available to the HLSL compiler when compiling a shader. The following table lists the pixel shader profiles that are supported.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Shader Profile</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ps_1_1</td>
<td>Compile to ps_1_1 version.</td>
</tr>
<tr class="even">
<td>ps_1_2</td>
<td>Compile to ps_1_2 version.</td>
</tr>
<tr class="odd">
<td>ps_1_3</td>
<td>Compile to ps_1_3 version.</td>
</tr>
<tr class="even">
<td>ps_1_4</td>
<td>Compile to ps_1_4 version.</td>
</tr>
<tr class="odd">
<td>ps_2_0</td>
<td>Compile to ps_2_0 version.</td>
</tr>
<tr class="even">
<td>ps_2_a</td>
<td>Same as the ps_2_0 profile, with the following additional capabilities available for the compiler to target:
<ul>
<li>Number of Temporary Registers (r#) is greater than or equal to 22.</li>
<li>Arbitrary source swizzle.</li>
<li>Gradient instructions: dsx, dsy.</li>
<li>Predication.</li>
<li>No dependent texture read limit.</li>
<li>No limit for the number of texture instructions.</li>
</ul></td>
</tr>
<tr class="odd">
<td>ps_2_b</td>
<td>Same as the ps_2_0 profile, with the following additional capabilities available for the compiler to target:
<ul>
<li>Number of Temporary Registers (r#) is greater than or equal to 32.</li>
<li>No limit for the number of texture instructions.</li>
</ul></td>
</tr>
<tr class="even">
<td>ps_3_0</td>
<td>Compile to ps_3_0 version.</td>
</tr>
</tbody>
</table>



 

For more information about the differences between shader versions, see [Pixel Shader Differences](../direct3dhlsl/dx9-graphics-reference-asm-ps-differences.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 
