---
description: Begins the processing to create a decoded picture.
ms.assetid: 80471cc6-c66d-49d9-8593-780e41ac39b9
title: IDirect3DDXVADevice9::BeginFrame method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DDXVADevice9.BeginFrame
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DDXVADevice9::BeginFrame method

Begins the processing to create a decoded picture.

## Syntax


```C++
HRESULT BeginFrame(
   IDirect3DSurface9 *pDstSurface,
   DWORD             SizeInputData,
   VOID              *pInputData,
   DWORD             *pSizeOutputData,
   VOID              *pOutputData
);
```



## Parameters

<dl> <dt>

*pDstSurface* 
</dt> <dd>

A pointer to the **IDirect3DSurface9** interface of the uncompressed destination surface.

</dd> <dt>

*SizeInputData* 
</dt> <dd>

The size of the buffer specified by *pInputData*, in bytes. The value must be 2.

</dd> <dt>

*pInputData* 
</dt> <dd>

Pointer to a buffer that contains data for the video accelerator. This buffer must contain the zero-based frame index, specified as a **WORD** value.

</dd> <dt>

*pSizeOutputData* 
</dt> <dd>

The size of the buffer specified by *pOutputData*, in bytes. The value must be zero.

</dd> <dt>

*pOutputData* 
</dt> <dd>

Pointer to a buffer that the video accelerator can write to. Set this parameter to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For each call to **BeginFrame**, the decoder must make a corresponding call to [**IDirect3DDXVADevice9::EndFrame**](idirect3ddxvadevice9-endframe.md).

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

 

 




