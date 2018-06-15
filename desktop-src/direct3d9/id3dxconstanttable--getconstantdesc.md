---
Description: Gets a pointer to an array of constant descriptions in the constant table.
ms.assetid: bd407fd6-b1cc-4197-ae98-1c2ca74d2ad0
title: ID3DXConstantTable::GetConstantDesc method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXConstantTable::GetConstantDesc method

Gets a pointer to an array of constant descriptions in the constant table.

## Syntax


```C++
HRESULT GetConstantDesc(
  [in]      D3DXHANDLE        hConstant,
  [in, out] D3DXCONSTANT_DESC *pDesc,
  [in, out] UINT              *pCount
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to a constant. See [D3DXHANDLE](dx9-graphics-reference-effects-constants.md).

</dd> <dt>

*pDesc* \[in, out\]
</dt> <dd>

Type: **[**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md)\***

Returns a pointer to an array of descriptions. See [**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md).

</dd> <dt>

*pCount* \[in, out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

The input supplied must be the maximum size of the array. The output is the number of elements that are filled in the array when the function returns.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

**ID3DXConstantTable::GetConstantDesc** will sometimes return a [**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md) with a Register\_Count of 0. This will happen with a constant appears in more than one Register\_Set but does not have space in that register set allocated.

Because a sampler can appear more than once in a constant table, this method can return an array of descriptions, each one with a different register index.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXConstantTable](id3dxconstanttable.md)
</dt> <dt>

[**ID3DXConstantTable::GetDesc**](id3dxconstanttable--getdesc.md)
</dt> </dl>

 

 




