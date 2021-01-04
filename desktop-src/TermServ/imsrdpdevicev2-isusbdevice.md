---
title: IMsRdpDeviceV2 IsUSBDevice property
description: Specifies if the device is for USB redirection.
ms.assetid: df4c9764-ad96-4f35-9537-3890293a944c
ms.tgt_platform: multiple
keywords:
- IsUSBDevice property Remote Desktop Services
- IsUSBDevice property Remote Desktop Services , IMsRdpDeviceV2 interface
- IMsRdpDeviceV2 interface Remote Desktop Services , IsUSBDevice property
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2.IsUSBDevice
- IMsRdpDeviceV2.get_IsUSBDevice
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2::IsUSBDevice property

Specifies if the device is for USB redirection.

This property is read-only.

## Syntax


```C++
HRESULT get_IsUSBDevice(
  [out, retval] VARIANT_BOOL *pvboolUSBDevice
);
```



## Property value

**true** if the device is for USB redirection; otherwise, **false**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 with SP1<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDeviceV2 is defined as 5fb94466-7661-42a8-98b7-01904c11668f<br/>      |



## See also

<dl> <dt>

[**IMsRdpDeviceV2**](imsrdpdevicev2.md)
</dt> </dl>

 

 





