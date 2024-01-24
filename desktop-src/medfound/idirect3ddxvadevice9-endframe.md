---
description: Ends the processing to create a decoded picture.
ms.assetid: 4b47cd53-6ce0-47b0-83ed-84926e92430f
title: IDirect3DDXVADevice9::EndFrame method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DDXVADevice9.EndFrame
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DDXVADevice9::EndFrame method

Ends the processing to create a decoded picture.

## Syntax


```C++
HRESULT EndFrame(
   DWORD SizeMiscData,
   VOID  *pMiscData
);
```



## Parameters

<dl> <dt>

*SizeMiscData* 
</dt> <dd>

The size of the buffer specified by *pMiscData*, in bytes. The value must be 2.

</dd> <dt>

*pMiscData* 
</dt> <dd>

Pointer to a buffer that contains data for the video accelerator. This buffer must contain the same frame index that was passed to the [**IDirect3DDXVADevice9::BeginFrame**](idirect3ddxvadevice9-beginframe.md) method in the *pInputData* parameter.

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

 

 




