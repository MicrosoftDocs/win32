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

This function -- which creates a shader-reflection object for retrieving information about a compiled shader -- no longer exists. Instead, use [**D3DReflect**](https://msdn.microsoft.com/en-us/library/Dd607334(v=VS.85).aspx) or [**D3D11Reflect**](https://msdn.microsoft.com/en-us/library/Ff728670(v=VS.85).aspx).

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

A pointer to the compiled shader. To get this pointer see [Getting a Pointer to a Compiled Shader](https://msdn.microsoft.com/en-us/library/Bb509703(v=VS.85).aspx).

</dd> <dt>

*BytecodeLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Length of pShaderBytecode.

</dd> <dt>

*ppReflector* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderReflection1**](/windows/desktop/api/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1)\*\***

Address of a shader reflection interface (see [**ID3D10ShaderReflection1 Interface**](/windows/desktop/api/D3D10_1Shader/nn-d3d10_1shader-id3d10shaderreflection1).)

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

Here is an example of creating a shader-reflection object. The example assumes you start with a compiled shader (shown as


```
pVSBuf
```



which you can see in [HLSLWithoutFX10 Sample](https://msdn.microsoft.com/en-us/library/Ee416414(v=VS.85).aspx)).


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

 

 




