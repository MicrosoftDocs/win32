---
title: IMsRdpDeviceCollection2 RedirectNow method
description: Forces devices that were selected or unselected from the collection to be redirected or removed.
ms.assetid: 9cd5849d-a589-43f3-b904-6b2e15ca033d
ms.tgt_platform: multiple
keywords:
- RedirectNow method Remote Desktop Services
- RedirectNow method Remote Desktop Services , IMsRdpDeviceCollection2 interface
- IMsRdpDeviceCollection2 interface Remote Desktop Services , RedirectNow method
topic_type:
- apiref
api_name:
- IMsRdpDeviceCollection2.RedirectNow
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceCollection2::RedirectNow method

Forces devices that were selected or unselected from the collection to be redirected or removed.

## Syntax


```C++
HRESULT RedirectNow(
  [in] RedirectDeviceType Type
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Type: **[**RedirectDeviceType**](redirectdevicetype.md)**

A value of the [**RedirectDeviceType**](redirectdevicetype.md) enumeration that specifies the type of device to be redirected.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**RedirectDeviceType**](redirectdevicetype.md)
</dt> <dt>

[**IMsRdpDeviceCollection2**](imsrdpdevicecollection2.md)
</dt> </dl>

 

 





