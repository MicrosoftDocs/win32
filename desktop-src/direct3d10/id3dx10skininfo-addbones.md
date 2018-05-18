---
Description: 'Allocate space for more bones.'
ms.assetid: 'f2acd338-f2c2-4340-a673-f36940cf31d9'
title: 'ID3DX10SkinInfo::AddBones method'
---

# ID3DX10SkinInfo::AddBones method

Allocate space for more bones.

## Syntax


```C++
HRESULT AddBones(
  [in] UINT Count
);
```



## Parameters

<dl> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of bones to add.

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

 

 




