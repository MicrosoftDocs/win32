---
Description: This function -- which creates a shader-reflection object for retrieving information about a compiled shader -- no longer exists. Instead, use D3DReflect or D3D11Reflect.
ms.assetid: 7090418c-1940-4f07-b075-937e3399613c
title: D3DX10ReflectShader function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10ReflectShader function

This function -- which creates a shader-reflection object for retrieving information about a compiled shader -- no longer exists. Instead, use [**D3DReflect**](direct3dhlsl.d3dreflect) or [**D3D11Reflect**](direct3dhlsl.d3d11reflect).

## Syntax


```C++
HRESULT D3DX10ReflectShader(
  _In_  const void                    *pShaderBytecode,
  _In_        SIZE_T                  BytecodeLength,
  _Out_       ID3D10ShaderReflection1 **ppReflector
);
```



## Parameters

<dl> <dt>

*pShaderBytecode* \[in\]
</dt> <dd>

Type: **const void\***

A pointer to the compiled shader. To get this pointer see [Getting a Pointer to a Compiled Shader](direct3dhlsl.dx_graphics_hlsl_using_shaders_10).

</dd> <dt>

*BytecodeLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

Length of pShaderBytecode.

</dd> <dt>

*ppReflector* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderReflection1**](/windows/win32/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1?branch=master)\*\***

Address of a shader reflection interface (see [**ID3D10ShaderReflection1 Interface**](/windows/win32/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1?branch=master).)

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

Here is an example of creating a shader-reflection object. The example assumes you start with a compiled shader (shown as


```
pVSBuf
```



which you can see in [HLSLWithoutFX10 Sample](61f892cf-4760-177b-5048-0ba3906d8bfc)).


```
ID3D10ShaderReflection1* pIShaderReflection1 = NULL;
D3D10_SHADER_DESC desc;
hr = D3D10ReflectShader( (void*) pVSBuf->GetBufferPointer(), pVSBuf->GetBufferSize(),
    &amp;pIShaderReflection1 );
if( pIShaderReflection1 )
{
    pIShaderReflection1->GetDesc( &amp;desc );
}
```



## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




