---
Description: 'Get a pointer to the mesh buffer memory to modify its contents.'
ms.assetid: 'd15ed47a-450e-404a-bcc2-a641abc2d02e'
title: 'ID3DX10MeshBuffer::Map method'
---

# ID3DX10MeshBuffer::Map method

Get a pointer to the mesh buffer memory to modify its contents.

## Syntax


```C++
HRESULT Map(
  [out] void   **ppData,
  [out] SIZE_T *pSize
);
```



## Parameters

<dl> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **void\*\***

Pointer to the buffer data.

</dd> <dt>

*pSize* \[out\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)\***

Size of the buffer in bytes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks



|                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 10:<br/> Map() in Direct3D 10 is analogous to resource Map() in Direct3D 9.<br/> |



 

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10MeshBuffer](id3dx10meshbuffer.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




