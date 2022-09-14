---
title: IMsRdpDeviceV2 IsOptionalDevice property
description: Specifies if the device is optional for USB redirection.
ms.assetid: a7226c40-7e22-48af-9895-b1fb1f861b58
ms.tgt_platform: multiple
keywords:
- IsOptionalDevice property Remote Desktop Services
- IsOptionalDevice property Remote Desktop Services , IMsRdpDeviceV2 interface
- IMsRdpDeviceV2 interface Remote Desktop Services , IsOptionalDevice property
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2.IsOptionalDevice
- IMsRdpDeviceV2.get_IsOptionalDevice
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2::IsOptionalDevice property

Specifies if the device is optional for USB redirection.

This property is read-only.

## Syntax


```C++
HRESULT get_IsOptionalDevice(
  [out, retval] VARIANT_BOOL *pvboolOptionalDevice
);
```



## Property value

**true** if the device is a optional; otherwise, **false**.

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

 

 





