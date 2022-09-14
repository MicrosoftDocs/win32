---
description: Searches for the next valid technique, starting at the technique after the specified technique.
ms.assetid: 0d2f3f80-90fd-495d-acb8-075f50e9a974
title: ID3DXEffect::FindNextValidTechnique method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.FindNextValidTechnique
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::FindNextValidTechnique method

Searches for the next valid technique, starting at the technique after the specified technique.

## Syntax


```C++
HRESULT FindNextValidTechnique(
  [in]  D3DXHANDLE hTechnique,
  [out] D3DXHANDLE *pTechnique
);
```



## Parameters

<dl> <dt>

*hTechnique* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to a technique. See [Handles (Direct3D 9)](handles.md). Specify **NULL** for this parameter to find the first valid technique.

</dd> <dt>

*pTechnique* \[out\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)\***

Pointer to an identifier for the next technique. **NULL** is returned if this is the last technique. See [Handles (Direct3D 9)](handles.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> <dt>

[**D3DXTECHNIQUE\_DESC**](d3dxtechnique-desc.md)
</dt> <dt>

[**ID3DXEffect::ValidateTechnique**](id3dxeffect--validatetechnique.md)
</dt> </dl>

 

 




