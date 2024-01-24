---
description: Limit the number of bones that can influence a vertex and/or limit the amount of influence a bone can have on a vertex.
ms.assetid: 75c4d2eb-0a43-494d-9642-4c08aa814794
title: ID3DX10SkinInfo::Compact method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo.Compact
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo::Compact method

Limit the number of bones that can influence a vertex and/or limit the amount of influence a bone can have on a vertex.

## Syntax


```C++
HRESULT Compact(
  [in] UINT  MaxPerVertexInfluences,
  [in] UINT  ScaleMode,
  [in] float MinWeight
);
```



## Parameters

<dl> <dt>

*MaxPerVertexInfluences* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The maximum number of bones that can influence any given vertex. This value is ignored if it is greater than the value returned by [**ID3DX10SkinInfo::GetMaxBoneInfluences**](id3dx10skininfo-getmaxboneinfluences.md).

</dd> <dt>

*ScaleMode* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

A flag describing how to scale the remaining weights on a given vertex after some have been chopped off by MinWeight. If D3DX10\_SKININFO\_NO\_SCALING is specified, the weights will not be scaled at all. If D3DX10\_SKININFO\_SCALE\_TO\_1 is specified, the weights greater than MinWeight will be scaled up so that they add up to 1.0. If D3DX10\_SKININFO\_SCALE\_TO\_TOTAL is specified, the weights greater than MinWeight will be scaled up so that they add up to the original total.

</dd> <dt>

*MinWeight* \[in\]
</dt> <dd>

Type: **float**

The minimum percentage of influence, or weight, that any bone can have on any vertex. This value must be between 0 and 1.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_OUTOFMEMORY or E\_INVALIDARG.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10SkinInfo](id3dx10skininfo.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
