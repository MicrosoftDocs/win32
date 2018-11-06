---
Description: Gets a floating point value.
ms.assetid: 239dd29c-092a-4b9f-ba24-eb6181e91461
title: ID3DXBaseEffect::GetFloat method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetFloat
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetFloat method

Gets a floating point value.

## Syntax


```C++
HRESULT GetFloat(
  [in]  D3DXHANDLE hParameter,
  [out] FLOAT      *pf
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pf* \[out\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Returns a floating point value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**SetFloat**](id3dxbaseeffect--setfloat.md)
</dt> </dl>

 

 




