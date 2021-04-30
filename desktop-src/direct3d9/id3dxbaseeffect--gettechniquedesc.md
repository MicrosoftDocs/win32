---
description: Gets a technique description.
ms.assetid: 12122858-1e54-446c-8f12-20cc62499d74
title: ID3DXBaseEffect::GetTechniqueDesc method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetTechniqueDesc
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetTechniqueDesc method

Gets a technique description.

## Syntax


```C++
HRESULT GetTechniqueDesc(
  [in]  D3DXHANDLE         hTechnique,
  [out] D3DXTECHNIQUE_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*hTechnique* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Technique handle. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXTECHNIQUE\_DESC**](d3dxtechnique-desc.md)\***

Returns a description of the technique. See [**D3DXTECHNIQUE\_DESC**](d3dxtechnique-desc.md).

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

 

 




