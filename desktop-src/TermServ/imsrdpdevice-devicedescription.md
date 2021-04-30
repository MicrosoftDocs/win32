---
title: IMsRdpDevice DeviceDescription property
description: Retrieves the device description to be displayed to the user if the display name is not available.
ms.assetid: 969f96c6-5655-4cac-9e91-059114dc3815
ms.tgt_platform: multiple
keywords:
- DeviceDescription property Remote Desktop Services
- DeviceDescription property Remote Desktop Services , IMsRdpDevice interface
- IMsRdpDevice interface Remote Desktop Services , DeviceDescription property
topic_type:
- apiref
api_name:
- IMsRdpDevice.DeviceDescription
- IMsRdpDevice.get_DeviceDescription
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDevice::DeviceDescription property

Retrieves the device description to be displayed to the user if the display name is not available.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceDescription(
  [out] BSTR *pDeviceDescription
);
```



## Property value

The device description.

## Error codes

If the method succeeds, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDevice is defined as 60c3b9c8-9e92-4f5e-a3e7-604a912093ea<br/>        |



## See also

<dl> <dt>

[**IMsRdpDevice**](imsrdpdevice.md)
</dt> </dl>

 

 





