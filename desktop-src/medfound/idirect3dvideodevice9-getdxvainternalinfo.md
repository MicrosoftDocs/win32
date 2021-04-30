---
description: Queries for the amount of scratch memory that the hardware abstraction layer (HAL) will allocate for its private use.
ms.assetid: 20e3dbef-daf5-487a-8d50-e2ebdb712cc0
title: IDirect3DVideoDevice9::GetDXVAInternalInfo method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.GetDXVAInternalInfo
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::GetDXVAInternalInfo method

Queries for the amount of scratch memory that the hardware abstraction layer (HAL) will allocate for its private use.

## Syntax


```C++
HRESULT GetDXVAInternalInfo(
   GUID               *pGuid,
   DXVAUncompDataInfo *pUncompData,
   DWORD              *pMemoryUsed
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

*pMemoryUsed* 
</dt> <dd>

Receives the amount of scratch memory that the HAL will allocate, in bytes.

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

 

 




