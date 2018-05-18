---
Description: 'Retrieves the Direct3D device associated with the line object.'
ms.assetid: '42459668-aa18-478d-82d9-b8b25dc4a898'
title: 'ID3DXLine::GetDevice method'
---

# ID3DXLine::GetDevice method

Retrieves the Direct3D device associated with the line object.

## Syntax


```C++
HRESULT GetDevice(
  [out, retval] LPDIRECT3DDEVICE9 *ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](idirect3ddevice9.md)\***

Address of a pointer to an [**IDirect3DDevice9**](idirect3ddevice9.md) interface, representing the Direct3D device object associated with the line object.

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

 

 




