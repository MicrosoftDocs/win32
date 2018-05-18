---
Description: 'Retrieves the device associated with the effect.'
ms.assetid: 'acef5d0a-b185-4054-8982-0580440ab76b'
title: 'ID3DXEffect::GetDevice method'
---

# ID3DXEffect::GetDevice method

Retrieves the device associated with the effect.

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

Address of a pointer to an [**IDirect3DDevice9**](idirect3ddevice9.md) interface, representing the device associated with the effect.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Calling this method will increase the internal reference count for the [**IDirect3DDevice9**](idirect3ddevice9.md) interface. Be sure to call IUnknown::Release when you are done using the **IDirect3DDevice9** interface or you will have a memory leak.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 




