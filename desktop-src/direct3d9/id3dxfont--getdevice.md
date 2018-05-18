---
Description: 'Retrieves the Direct3D device associated with the font object.'
ms.assetid: 'c713cbe2-6e6e-476b-a995-14fa149cb088'
title: 'ID3DXFont::GetDevice method'
---

# ID3DXFont::GetDevice method

Retrieves the Direct3D device associated with the font object.

## Syntax


```C++
HRESULT GetDevice(
  [out] LPDIRECT3DDEVICE9 *ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](idirect3ddevice9.md)\***

Address of a pointer to an [**IDirect3DDevice9**](idirect3ddevice9.md) interface, representing the Direct3D device object associated with the font object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

> [!Note]  
> Calling this method will increase the internal reference count on the [**IDirect3DDevice9**](idirect3ddevice9.md) interface. Be sure to call [**IUnknown**](com.iunknown) when you are done using this **IDirect3DDevice9** interface or you will have a memory leak.

 

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




