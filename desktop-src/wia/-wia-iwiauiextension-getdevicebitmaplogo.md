---
description: Gets a custom bitmap logo for the device.
ms.assetid: 56b3c7c9-64f4-4853-9eb7-d876d02a851f
title: IWiaUIExtension::GetDeviceBitmapLogo method (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension.GetDeviceBitmapLogo
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension::GetDeviceBitmapLogo method

Gets a custom bitmap logo for the device.

## Syntax


```C++
HRESULT GetDeviceBitmapLogo(
  [in]  BSTR    bstrDeviceId,
  [out] HBITMAP *phBitmap,
  [in]  ULONG   nMaxWidth,
  [in]  ULONG   nMaxHeight
);
```



## Parameters

<dl> <dt>

*bstrDeviceId* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the device ID of the WIA device for which the icon is to be obtained.

</dd> <dt>

*phBitmap* \[out\]
</dt> <dd>

Type: **HBITMAP\***

Points to a memory location that will receive a handle for the bitmap logo for the device.

</dd> <dt>

*nMaxWidth* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the desired width of the bitmap.

</dd> <dt>

*nMaxHeight* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the desired height of the bitmap.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




