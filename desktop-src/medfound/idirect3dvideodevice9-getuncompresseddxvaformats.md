---
description: Gets a list of uncompressed pixel formats that can be rendered using a specified DirectX Video Acceleration (DXVA) profile.
ms.assetid: 7c69ea5f-6054-4430-95b5-820db6854fc0
title: IDirect3DVideoDevice9::GetUncompressedDXVAFormats method (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirect3DVideoDevice9.GetUncompressedDXVAFormats
api_type: 
- COM
api_location: 
- dxva.h
---

# IDirect3DVideoDevice9::GetUncompressedDXVAFormats method

Gets a list of uncompressed pixel formats that can be rendered using a specified DirectX Video Acceleration (DXVA) profile.

## Syntax


```C++
HRESULT GetUncompressedDXVAFormats(
   GUID      *pGuid,
   DWORD     *pNumFormats,
   D3DFORMAT *pFormats
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Pointer to a GUID that specifies the DXVA profile. To get a list of supported profiles, call [**IDirect3DVideoDevice9::GetDXVAGuids**](idirect3dvideodevice9-getdxvaguids.md).

</dd> <dt>

*pNumFormats* 
</dt> <dd>

On input, specifies the number of elements in the *pFormats* array. If *pFormats* is **NULL**, the value of `*pNumFormats` must be zero.

On output, if *pFormats* is **NULL**, *pNumFormats* receives the number of supported pixel formats. Otherwise, *pNumFormats* receives the actual number of pixel formats copied to the *pFormats* array.

</dd> <dt>

*pFormats* 
</dt> <dd>

Address of an array of **D3DFORMAT** values, or **NULL**. If the value is non-**NULL**, the array receives a list of pixel formats.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Call this method twice. On the first call, set *pFormats* to **NULL**. The *pNumFormats* parameter receives the number of formats. Allocate a **D3DFORMAT** array with the required size, and call the method again. This time, set *pFormats* to the address of the array. The method fills the array with the list of pixel formats.

The driver should return the formats in decreasing order of preference, with the most preferred format listed first.

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

 

 




