---
description: Performs a DirectX Video Acceleration (DXVA) decoding operation.
ms.assetid: cb87a087-ca53-470e-ab46-f4022cfd7869
title: IDirect3DDXVADevice9::Execute method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DDXVADevice9.Execute
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DDXVADevice9::Execute method

Performs a DirectX Video Acceleration (DXVA) decoding operation.

## Syntax


```C++
HRESULT Execute(
   DWORD          FunctionNum,
   VOID           *pInputData,
   DWORD          InputSize,
   VOID           *OutputData,
   DWORD          OutputSize,
   DWORD          NumBuffers,
   DXVABufferInfo *pBufferInfo
);
```



## Parameters

<dl> <dt>

*FunctionNum* 
</dt> <dd>

A **DWORD** that contains one or more DXVA function numbers. For details, refer to the [DXVA 1.0 specification](/windows-hardware/drivers/display/directx-video-acceleration).

</dd> <dt>

*pInputData* 
</dt> <dd>

A pointer to a buffer that contains input data for the decoding operation. The meaning of this data depends on the surface type and function number.

</dd> <dt>

*InputSize* 
</dt> <dd>

The size of the input data, in bytes.

</dd> <dt>

*OutputData* 
</dt> <dd>

Pointer to a buffer where the video accelerator writes output data.

</dd> <dt>

*OutputSize* 
</dt> <dd>

The size of the *OutputData* buffer, in bytes.

</dd> <dt>

*NumBuffers* 
</dt> <dd>

The number of elements in the *pBufferInfo* array.

</dd> <dt>

*pBufferInfo* 
</dt> <dd>

A pointer to an array of [**DXVABufferInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvabufferinfo) structures.

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

[**IDirect3DDXVADevice9**](idirect3ddxvadevice9.md)
</dt> </dl>

 

 
