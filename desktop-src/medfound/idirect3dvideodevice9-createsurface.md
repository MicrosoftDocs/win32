---
description: Creates a compressed surface for DirectX Video Acceleration (DXVA) decoding.
ms.assetid: 2bb8c99d-1151-4f6d-869f-2c1a592e76af
title: IDirect3DVideoDevice9::CreateSurface method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.CreateSurface
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::CreateSurface method

Creates a compressed surface for DirectX Video Acceleration (DXVA) decoding.

To get the surface requirements, call [**IDirect3DVideoDevice9::GetDXVACompressedBufferInfo**](idirect3dvideodevice9-getdxvacompressedbufferinfo.md) and examine the returned [**DXVACompBufferInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvacompbufferinfo) structures.

## Syntax


```C++
HRESULT CreateSurface(
   UINT              Width,
   UINT              Height,
   UINT              BackBuffers,
   D3DFORMAT         Format,
   D3DPOOL           Pool,
   DWORD             Usage,
   IDirect3DSurface9 **ppSurface,
   HANDLE            *pSharedHandle
);
```



## Parameters

<dl> <dt>

*Width* 
</dt> <dd>

The width of the surface, in pixels. Set this parameter equal to **DXVACompBufferInfo.WidthToCreate**.

</dd> <dt>

*Height* 
</dt> <dd>

The height of the surface, in pixels. Set this parameter equal to **DXVACompBufferInfo.HeightToCreate**.

</dd> <dt>

*BackBuffers* 
</dt> <dd>

The number of back buffers. This parameter can be zero.

</dd> <dt>

*Format* 
</dt> <dd>

The pixel format, specified as a **D3DFORMAT** value. Set this parameter equal to **DXVACompBufferInfo.Format**.

</dd> <dt>

*Pool* 
</dt> <dd>

The memory pool in which to create the surface, specified as a **D3DPOOL** value. Set this parameter equal to **DXVACompBufferInfo.Pool**.

</dd> <dt>

*Usage* 
</dt> <dd>

A bitwise **OR** of one or more **D3DUSAGE** constants. Set this parameter equal to **DXVACompBufferInfo.Usage**.

</dd> <dt>

*ppSurface* 
</dt> <dd>

Receives a pointer to the **IDirect3DSurface9** interface. The caller must release the interface.

</dd> <dt>

*pSharedHandle* 
</dt> <dd>

Reserved. Set to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[**IDirect3DVideoDevice9**](idirect3dvideodevice9.md)
</dt> </dl>

 

 




