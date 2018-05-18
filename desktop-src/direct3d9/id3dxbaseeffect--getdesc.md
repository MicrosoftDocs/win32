---
Description: 'Gets the effect description.'
ms.assetid: '96b53b8a-0c20-4bfd-af45-626f6e0305d2'
title: 'ID3DXBaseEffect::GetDesc method'
---

# ID3DXBaseEffect::GetDesc method

Gets the effect description.

## Syntax


```C++
HRESULT GetDesc(
  [out] D3DXEFFECT_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXEFFECT\_DESC**](d3dxeffect-desc.md)\***

Returns a description of the effect. See [**D3DXEFFECT\_DESC**](d3dxeffect-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




