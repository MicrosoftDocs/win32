---
description: Gets a pass description.
ms.assetid: 44c65a82-bcf4-49f5-9312-8320e133bb2f
title: ID3DXBaseEffect::GetPassDesc method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetPassDesc
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetPassDesc method

Gets a pass description.

## Syntax


```C++
HRESULT GetPassDesc(
  [in]  D3DXHANDLE    hPass,
  [out] D3DXPASS_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*hPass* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Pass handle. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXPASS\_DESC**](d3dxpass-desc.md)\***

Returns a description of the specified pass. See [**D3DXPASS\_DESC**](d3dxpass-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

> [!Note]  
> If an effect is created with [D3DXFX\_NOT\_CLONEABLE](d3dxfx.md), this method will return **NULL** pointers (in [**D3DXPASS\_DESC**](d3dxpass-desc.md)) to the shader functions.

 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




