---
Description: 'Set the mesh''s index data.'
ms.assetid: 'f3e7e166-94b5-45f6-9d43-8d7e32b7b523'
title: 'ID3DX10Mesh::SetIndexData method'
---

# ID3DX10Mesh::SetIndexData method

Set the mesh's index data.

## Syntax


```C++
HRESULT SetIndexData(
  [in] const void *pData,
  [in]       UINT cIndices
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **const void\***

The index data.

</dd> <dt>

*cIndices* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of indices in pData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




