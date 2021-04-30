---
description: Gets a parameter or annotation description.
ms.assetid: fd54eb08-a7e4-4106-b0ed-49a4da7fcadc
title: ID3DXBaseEffect::GetParameterDesc method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetParameterDesc
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetParameterDesc method

Gets a parameter or annotation description.

## Syntax


```C++
HRESULT GetParameterDesc(
  [in]  D3DXHANDLE         hParameter,
  [out] D3DXPARAMETER_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Parameter or annotation handle. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXPARAMETER\_DESC**](d3dxparameter-desc.md)\***

Returns a description of the specified parameter or annotation. See [**D3DXPARAMETER\_DESC**](d3dxparameter-desc.md).

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

 

 




