---
description: D3DXGetPixelShaderProfile function - Returns the name of the highest high-level shader language (HLSL) profile supported by a given device.
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




| Shader Profile | Description | 
|----------------|-------------|
| ps_1_1 | Compile to ps_1_1 version. | 
| ps_1_2 | Compile to ps_1_2 version. | 
| ps_1_3 | Compile to ps_1_3 version. | 
| ps_1_4 | Compile to ps_1_4 version. | 
| ps_2_0 | Compile to ps_2_0 version. | 
| ps_2_a | Same as the ps_2_0 profile, with the following additional capabilities available for the compiler to target:<ul><li>Number of Temporary Registers (r#) is greater than or equal to 22.</li><li>Arbitrary source swizzle.</li><li>Gradient instructions: dsx, dsy.</li><li>Predication.</li><li>No dependent texture read limit.</li><li>No limit for the number of texture instructions.</li></ul> | 
| ps_2_b | Same as the ps_2_0 profile, with the following additional capabilities available for the compiler to target:<ul><li>Number of Temporary Registers (r#) is greater than or equal to 32.</li><li>No limit for the number of texture instructions.</li></ul> | 
| ps_3_0 | Compile to ps_3_0 version. | 




 

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

 

 
