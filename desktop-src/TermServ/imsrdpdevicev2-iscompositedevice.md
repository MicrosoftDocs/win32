---
title: IMsRdpDeviceV2 IsCompositeDevice property
description: Specifies if the device is a composite device.
ms.assetid: cc54f3f0-de0b-4f75-b5a1-4f061ac95ab5
ms.tgt_platform: multiple
keywords:
- IsCompositeDevice property Remote Desktop Services
- IsCompositeDevice property Remote Desktop Services , IMsRdpDeviceV2 interface
- IMsRdpDeviceV2 interface Remote Desktop Services , IsCompositeDevice property
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2.IsCompositeDevice
- IMsRdpDeviceV2.get_IsCompositeDevice
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2::IsCompositeDevice property

Specifies if the device is a composite device.

This property is read-only.

## Syntax


```C++
HRESULT get_IsCompositeDevice(
  [out, retval] VARIANT_BOOL *pvboolCompositeDevice
);
```



## Property value

**true** if the device is a composite device; otherwise, **false**.

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

 

 





