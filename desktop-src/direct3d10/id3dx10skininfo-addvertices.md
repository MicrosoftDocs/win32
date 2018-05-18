---
Description: 'Allocate space for additional vertices.'
ms.assetid: 'dd6445ea-4754-4ba3-a264-59295325ee08'
title: 'ID3DX10SkinInfo::AddVertices method'
---

# ID3DX10SkinInfo::AddVertices method

Allocate space for additional vertices.

## Syntax


```C++
HRESULT AddVertices(
  [in] UINT Count
);
```



## Parameters

<dl> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of vertices to add.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10SkinInfo](id3dx10skininfo.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




