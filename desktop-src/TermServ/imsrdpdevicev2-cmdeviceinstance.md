---
title: IMsRdpDeviceV2 CmDeviceInstance property
description: Contains the configuration manager device instance of the device.
ms.assetid: 2a3e7001-7889-417f-8f9d-cc7a1776249f
ms.tgt_platform: multiple
keywords:
- CmDeviceInstance property Remote Desktop Services
- CmDeviceInstance property Remote Desktop Services , IMsRdpDeviceV2 interface
- IMsRdpDeviceV2 interface Remote Desktop Services , CmDeviceInstance property
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2.CmDeviceInstance
- IMsRdpDeviceV2.get_CmDeviceInstance
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2::CmDeviceInstance property

Contains the configuration manager device instance of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_CmDeviceInstance(
  [out, retval] DWORD *pCmDeviceInstance
);
```



## Property value

The configuration manager device instance of the device.

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

 

 





