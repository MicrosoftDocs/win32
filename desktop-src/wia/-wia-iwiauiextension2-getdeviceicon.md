---
description: IWiaUIExtension2::GetDeviceIcon method - Gets a custom device icon.
ms.assetid: ea768dd1-22fe-4a0f-8851-b152e28d65fb
title: IWiaUIExtension2::GetDeviceIcon method (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension2.GetDeviceIcon
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension2::GetDeviceIcon method

Gets a custom device icon.

## Syntax


```C++
HRESULT GetDeviceIcon(
  [in]  BSTR  bstrDeviceId,
  [out] HICON *phIcon,
  [in]  ULONG nSize
);
```



## Parameters

<dl> <dt>

*bstrDeviceId* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the device ID of the WIA device for which the icon is to be obtained.

</dd> <dt>

*phIcon* \[out\]
</dt> <dd>

Type: **HICON\***

Points to a memory location that will receive a handle for the icon for the device.

</dd> <dt>

*nSize* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the desired icon size, in pixels. The icon is assumed to be square, and nSize specifies both the width and height of the requested icon.

</dd> </dl>

## Return value

Type: **HRESULT**

If the method succeeds, it returns S\_OK. If the method fails, it returns an appropriate error code. The following table shows some of the possible return status codes.



| Error code    | Description                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------|
| E\_INVALIDARG | Parameter bstrDeviceId or phIcon is **NULL**, or bstrDeviceId does not point to a valid WIA device ID string |
| E\_FAIL       | No icon resource is available.                                                                               |
| E\_NOTIMPL    | No icon of the size requested is available.                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




