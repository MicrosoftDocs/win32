---
Description: 'Applies a stipple pattern to the line.'
ms.assetid: '53548a9f-cf09-4ab9-9327-d5053645fc1b'
title: 'ID3DXLine::SetPattern method'
---

# ID3DXLine::SetPattern method

Applies a stipple pattern to the line.

## Syntax


```C++
HRESULT SetPattern(
  [in] DWORD dwPattern
);
```



## Parameters

<dl> <dt>

*dwPattern* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Describes the stipple pattern: 1 is opaque, 0 is transparent.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




