---
description: Gets a function description.
ms.assetid: a1a0ccf4-2428-4e60-9af0-07dc2132a367
title: ID3DXBaseEffect::GetFunctionDesc method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetFunctionDesc
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetFunctionDesc method

Gets a function description.

## Syntax


```C++
HRESULT GetFunctionDesc(
  [in]  D3DXHANDLE        hFunction,
  [out] D3DXFUNCTION_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*hFunction* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Function handle. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXFUNCTION\_DESC**](d3dxfunction-desc.md)\***

Returns a description of the function. See [**D3DXFUNCTION\_DESC**](d3dxfunction-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




