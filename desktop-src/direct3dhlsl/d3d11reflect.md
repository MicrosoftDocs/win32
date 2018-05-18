---
title: D3D11Reflect function
description: Gets a pointer to a reflection interface.
ms.assetid: '855097c7-988b-4ab6-90c5-e5dd0bc9e1e0'
keywords: ["D3D11Reflect function HLSL"]
topic_type:
- apiref
api_name:
- D3D11Reflect
api_location:
- D3dcompiler_47.dll
api_type:
- DllExport
---

# D3D11Reflect function

Gets a pointer to a reflection interface.

## Syntax

``` syntax
HRESULT D3D11Reflect(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  out ID3D11ShaderReflection ppReflector
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to source data as compiled HLSL code.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*ppReflector* \[out\]
</dt> <dd>

Type: **[**ID3D11ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/ff476590)\*\***

The address of a pointer to the [**ID3D11ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/ff476590) interface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the return codes described in the topic [Direct3D 11 Return Codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

The inline **D3D11Reflect** compiler function is a wrapper for the [**D3DReflect**](d3dreflect.md) compiler function. **D3D11Reflect** can retrieve only a [**ID3D11ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/ff476590) interface from a shader. **D3DReflect** can retrieve a **ID3D11ShaderReflection** interface or a Direct3D 10 or Direct3D 10.1 reflection interface, for example, [**ID3D10ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/bb173835).

Shader code contains metadata that can be inspected using the reflection APIs.

The following code shows how to retrieve a [**ID3D11ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/ff476590) interface from a shader.


```C++
pd3dDevice->CreatePixelShader( pPixelShaderBuffer->GetBufferPointer(),
                               pPixelShaderBuffer->GetBufferSize(), g_pPSClassLinkage, &amp;g_pPixelShader );

ID3D11ShaderReflection* pReflector = NULL; 
D3D11Reflect( pPixelShaderBuffer->GetBufferPointer(), pPixelShaderBuffer->GetBufferSize(), 
            &amp;pReflector);
```



## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DCompiler.inl</dt> </dl>     |
| Library<br/> | <dl> <dt>D3dcompiler\_47.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dcompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





