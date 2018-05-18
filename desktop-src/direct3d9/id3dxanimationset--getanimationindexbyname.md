---
Description: 'Gets the index of an animation, given its name.'
ms.assetid: '6e91a4fe-3202-447b-b486-d29e8da64af2'
title: 'ID3DXAnimationSet::GetAnimationIndexByName method'
---

# ID3DXAnimationSet::GetAnimationIndexByName method

Gets the index of an animation, given its name.

## Syntax


```C++
HRESULT GetAnimationIndexByName(
  [in]  LPCSTR pName,
  [out] UINT   *pIndex
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Name of the animation.

</dd> <dt>

*pIndex* \[out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Pointer to the animation index.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](direct3d9.d3dxerr).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




