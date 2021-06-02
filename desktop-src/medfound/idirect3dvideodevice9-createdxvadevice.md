---
description: Creates a DirectX Video Acceleration (DXVA) decoder device.
ms.assetid: aeebf65f-1bde-4a33-87cd-25c62dcc0248
title: IDirect3DVideoDevice9::CreateDXVADevice method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.CreateDXVADevice
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::CreateDXVADevice method

Creates a DirectX Video Acceleration (DXVA) decoder device.

## Syntax


```C++
HRESULT CreateDXVADevice(
   GUID                 *pGuid,
   DXVAUncompDataInfo   *pUncompData,
   LPVOID               pData,
   DWORD                DataSize,
   IDirect3DDXVADevice9 **ppDXVADevice
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Pointer to a GUID that specifies the device to create.

</dd> <dt>

*pUncompData* 
</dt> <dd>

Pointer to a [**DXVAUncompDataInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvauncompdatainfo) structure that specifies the format of the uncompressed image.

</dd> <dt>

*pData* 
</dt> <dd>

Pointer to a **DXVA\_ConnectMode** structure that specifies the DXVA mode and restricted profile.

</dd> <dt>

*DataSize* 
</dt> <dd>

Size of the **DXVA\_ConnectMode** structure, in bytes.

</dd> <dt>

*ppDXVADevice* 
</dt> <dd>

Receives a pointer to the [**IDirect3DDXVADevice9**](idirect3ddxvadevice9.md) interface. The caller must release the interface.

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

 

 




