---
Description: 'Used to decompress encoded data. Typically this would be used to load resources from file systems, such as ZIP files. When loading from an uncompressed resource, the decompression stage does not have to do any work.'
ms.assetid: '7f7e3ffd-8dac-403f-813b-d6d21d146fa7'
title: 'ID3DX10DataLoader::Decompress method'
---

# ID3DX10DataLoader::Decompress method

Used to decompress encoded data. Typically this would be used to load resources from file systems, such as ZIP files. When loading from an uncompressed resource, the decompression stage does not have to do any work.

## Syntax


```C++
HRESULT Decompress(
  [out] void   **ppData,
  [in]  SIZE_T *pcBytes
);
```



## Parameters

<dl> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **void\*\***

Pointer to the raw data to decompress.

</dd> <dt>

*pcBytes* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)\***

The size of the data pointed to by ppData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

[**ID3DX10DataLoader Interface**](id3dx10dataloader.md) can be inherited and its members redefined. Decompress could be redefined to support your own custom file formats.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10DataLoader](id3dx10dataloader.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




