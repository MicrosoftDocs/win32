---
title: D3DReflect function
description: Gets a pointer to a reflection interface.
ms.assetid: 601cc907-2878-4c9b-bc48-0575fd4479e8
keywords:
- D3DReflect function HLSL
topic_type:
- apiref
api_name:
- D3DReflect
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DReflect function

Gets a pointer to a reflection interface.

## Syntax

``` syntax
HRESULT WINAPI D3DReflect(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  in  REFIID pInterface,
  out void ppReflector
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

*pInterface* \[in\]
</dt> <dd>

Type: **REFIID**

The reference GUID of the COM interface to use. For example, **IID\_ID3D11ShaderReflection**.

</dd> <dt>

*ppReflector* \[out\]
</dt> <dd>

Type: **void\*\***

A pointer to a reflection interface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

Shader code contains metadata that can be inspected using the reflection APIs.

The following code illustrates retrieving a [**ID3D11ShaderReflection**](https://msdn.microsoft.com/library/windows/desktop/ff476590) Interface from a shader.


```C++
pd3dDevice->CreatePixelShader( pPixelShaderBuffer->GetBufferPointer(),
                               pPixelShaderBuffer->GetBufferSize(), g_pPSClassLinkage, &g_pPixelShader );

ID3D11ShaderReflection* pReflector = NULL; 
D3DReflect( pPixelShaderBuffer->GetBufferPointer(), pPixelShaderBuffer->GetBufferSize(), 
            IID_ID3D11ShaderReflection, (void**) &pReflector);
```



## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3dcompiler\_47.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dcompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





