---
Description: This function -- which creates a shader-reflection object for retrieving information about a compiled shader -- no longer exists. Instead, use D3DReflect or D3D11Reflect.
ms.assetid: 7090418c-1940-4f07-b075-937e3399613c
title: D3DX10ReflectShader function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DX10ReflectShader function

This function -- which creates a shader-reflection object for retrieving information about a compiled shader -- no longer exists. Instead, use [**D3DReflect**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dreflect.htm) or [**D3D11Reflect**](https://msdn.microsoft.com/855097c7-988b-4ab6-90c5-e5dd0bc9e1e0).

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

A pointer to the compiled shader. To get this pointer see [Getting a Pointer to a Compiled Shader](https://msdn.microsoft.com/VS|directx_sdk|~\dx_graphics_hlsl_using_shaders_10.htm).

</dd> <dt>

*BytecodeLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Length of pShaderBytecode.

</dd> <dt>

*ppReflector* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderReflection1**](/windows/desktop/api/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1)\*\***

Address of a shader reflection interface (see [**ID3D10ShaderReflection1 Interface**](/windows/desktop/api/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1).)

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

Here is an example of creating a shader-reflection object. The example assumes you start with a compiled shader (shown as


```
pVSBuf
```



which you can see in [HLSLWithoutFX10 Sample](https://msdn.microsoft.com/windows/desktop/61f892cf-4760-177b-5048-0ba3906d8bfc)).


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

 

 




