---
description: Gets the semantics for the shader inputs. Use this method to determine the input vertex format.
ms.assetid: e94b2b14-3830-4a13-8c23-7841a56d6730
title: D3DXGetShaderInputSemantics function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXGetShaderInputSemantics
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXGetShaderInputSemantics function

Gets the semantics for the shader inputs. Use this method to determine the input vertex format.

## Syntax


```C++
HRESULT D3DXGetShaderInputSemantics(
  _In_  const DWORD        *pFunction,
  _In_        D3DXSEMANTIC *pSemantics,
  _Out_       UINT         *pCount
);
```



## Parameters

<dl> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the shader function DWORD stream.

</dd> <dt>

*pSemantics* \[in\]
</dt> <dd>

Type: **[**D3DXSEMANTIC**](d3dxsemantic.md)\***

Pointer to an array of [**D3DXSEMANTIC**](d3dxsemantic.md) structures. The function will fill this array with the semantics for each input element referenced by the shader. This array is assumed to contain at least MAXD3DDECLLENGTH elements. However, calling **D3DXGetShaderInputSemantics** with pSemantics = **NULL** will return the number of elements needed for pCount.

</dd> <dt>

*pCount* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Returns the number of elements in pSemantics.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

Use **D3DXGetShaderInputSemantics** to return a list of input semantics required by the shader. This is the way to find out what the input vertex format is for a high-level shader language (HLSL) shader. If the shader has additional inputs that your vertex declaration is missing, you could create an extra vertex stream that has a stride of 0 that has the missing components with default values. For instance, this technique could be used to provide default vertex color for models that do not specify it.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 
