---
Description: 'Gets the track description.'
ms.assetid: '7663a26f-5ad3-4a17-a502-c0dcfa730db2'
title: 'ID3DXAnimationController::GetTrackDesc method'
---

# ID3DXAnimationController::GetTrackDesc method

Gets the track description.

## Syntax


```C++
HRESULT GetTrackDesc(
  [in]  UINT             Track,
  [out] LPD3DXTRACK_DESC pDesc
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Track identifier.

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**LPD3DXTRACK\_DESC**](d3dxtrack-desc.md)**

Pointer to the track description. See [**D3DXTRACK\_DESC**](d3dxtrack-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




