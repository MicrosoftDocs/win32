---
description: Queries the read/write status of a DirectX Video Acceleration (DXVA) decoding surface.
ms.assetid: 8a4c3173-5911-49ec-8cb8-e30f96a4f1c9
title: IDirect3DDXVADevice9::QueryStatus method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DDXVADevice9.QueryStatus
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DDXVADevice9::QueryStatus method

Queries the read/write status of a DirectX Video Acceleration (DXVA) decoding surface.

## Syntax


```C++
HRESULT QueryStatus(
   IDirect3DSurface9 *pSurface,
   DWORD             Flags
);
```



## Parameters

<dl> <dt>

*pSurface* 
</dt> <dd>

Pointer to the **IDirect3DSurface9** interface of the surface to query.

</dd> <dt>

*Flags* 
</dt> <dd>

Specifies the type of query to perform.



| Value                                                                                                                             | Meaning                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="0x00"></span><span id="0X00"></span><dl> <dt>**0x00**</dt> </dl> | Test whether the surface is safe to use for writing.<br/> |
| <span id="0x01"></span><span id="0X01"></span><dl> <dt>**0x01**</dt> </dl> | Test whether the surface is safe to use for reading.<br/> |



 

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

 

 




