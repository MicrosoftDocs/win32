---
description: Gets information about the compressed buffers needed for hardware-accelerated decoding.
ms.assetid: 5a9fb077-fd79-4faa-a0f8-b3ac987adf36
title: IDirect3DVideoDevice9::GetDXVACompressedBufferInfo method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.GetDXVACompressedBufferInfo
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::GetDXVACompressedBufferInfo method

Gets information about the compressed buffers needed for hardware-accelerated decoding.

## Syntax


```C++
HRESULT GetDXVACompressedBufferInfo(
   GUID               *pGuid,
   DXVAUncompDataInfo *pUncompData,
   DWORD              *pNumBuffers,
   DXVACompBufferInfo *pBufferInfo
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Pointer to a GUID that specifies the DXVA profile. To get a list of supported profiles, call [**IDirect3DVideoDevice9::GetDXVAGuids**](idirect3dvideodevice9-getdxvaguids.md).

</dd> <dt>

*pUncompData* 
</dt> <dd>

Pointer to a [**DXVAUncompDataInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvauncompdatainfo) structure that specifies the size and pixel format of the uncompressed data.

</dd> <dt>

*pNumBuffers* 
</dt> <dd>

On input, specifies the number of elements in the *pBufferInfo* array. If *pBufferInfo* is **NULL**, the value of `*pNumBuffers` must be zero.

On output, if *pBufferInfo* is **NULL**, *pNumBuffers* receives the size of array to allocate. Otherwise, *pNumBuffers* receives the actual number of elements that are copied to the *pBufferInfo* array.

</dd> <dt>

*pBufferInfo* 
</dt> <dd>

Address of an array of [**DXVACompBufferInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvacompbufferinfo) structures or **NULL**. If the value is non-**NULL**, the method copies a list of **DXVACompBufferInfo** structures to this array. Each structure corresponds to one type of compressed data buffer that is used by the video accelerator.

Set all of the array elements to zero before calling this method.

Each array index corresponds to one of the DXVA surface types defined in dxva.h. The video accelerator returns a list of up to **DXVA\_NUM\_TYPES\_COMP\_BUFFERS** array entries. For details, refer to the [DXVA 1.0 specification](/windows-hardware/drivers/display/directx-video-acceleration), section 3.4, "Buffer Description List." If a particular buffer type is not used by the DXVA profile, the entry at that index contains zeros for all values.

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

 

 
