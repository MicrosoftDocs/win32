---
description: Gets a list of DirectX Video Acceleration (DXVA) profiles that are supported by the display driver.
ms.assetid: 4adbbac2-a25d-4e17-b62e-a02a67dcdbed
title: IDirect3DVideoDevice9::GetDXVAGuids method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.GetDXVAGuids
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::GetDXVAGuids method

Gets a list of DirectX Video Acceleration (DXVA) profiles that are supported by the display driver.

## Syntax


```C++
HRESULT GetDXVAGuids(
   DWORD *pNumGuids,
   GUID  *pGuids
);
```



## Parameters

<dl> <dt>

*pNumGuids* 
</dt> <dd>

On input, specifies the number of elements in the *pGuids* array. If *pGuids* is **NULL**, the value of `*pNumGuids` must be zero.

On output, if *pGuids* is **NULL**, *pNumGuids* receives the number of restricted-mode DXVA profiles. Otherwise, *pNumGuids* receives the actual number of GUIDs that are copied to the *pGuids* array.

</dd> <dt>

*pGuids* 
</dt> <dd>

Address of an array of GUIDs or **NULL**. If the value is non-**NULL**, the array receives a list of GUIDs that specify restricted-mode DXVA profiles. These GUIDs are defined in dxva.h, and are documented in the [DXVA 1.0 specification](/windows-hardware/drivers/display/directx-video-acceleration).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Call this method twice. On the first call, set *pGuids* to **NULL**. The *pNumGuids* parameter receives the number of DXVA profile GUIDs. Allocate an array of GUIDs with the required size and call the method again. This time, set *pGuids* to the address of the array. The method fills the array with the list of DXVA profile GUIDs.

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

 

 
