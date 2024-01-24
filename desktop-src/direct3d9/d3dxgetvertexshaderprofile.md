---
description: D3DXGetVertexShaderProfile function - Returns the name of the highest high-level shader language (HLSL) profile supported by a given device.
ms.assetid: a50e2a17-8170-4364-a562-7886593341b3
title: D3DXGetVertexShaderProfile function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXGetVertexShaderProfile
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXGetVertexShaderProfile function

Returns the name of the highest high-level shader language (HLSL) profile supported by a given device.

## Syntax


```C++
LPCSTR D3DXGetVertexShaderProfile(
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

If the device does not support vertex shaders then the function returns **NULL**.

## Remarks

A shader profile specifies the assembly shader version to use and the capabilities available to the HLSL compiler when compiling a shader. The following table lists the vertex shader profiles that are supported.




| Shader Profile | Description | 
|----------------|-------------|
| vs_1_1 | Compile to vs_1_1 version. | 
| vs_2_0 | Compile to vs_2_0 version. | 
| vs_2_a | Same as the vs_2_0 profile, with the following additional capabilities available for the compiler to target:<ul><li>Number of Temporary Registers (r#) is greater than or equal to 13.</li><li>Dynamic flow control instruction.</li><li>Predication.</li></ul> | 
| vs_3_0 | Compile to vs_3_0 version. | 




 

For more information about the differences between shader versions, see [Vertex Shader Differences](../direct3dhlsl/dx9-graphics-reference-asm-vs-differences.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 
