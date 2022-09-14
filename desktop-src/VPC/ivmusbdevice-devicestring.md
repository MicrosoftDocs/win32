---
title: IVMUSBDevice DeviceString property (VPCCOMInterfaces.h)
description: Retrieves the name of the USB device.
ms.assetid: 2ae82e2a-b33a-4039-acdb-958b094b1045
keywords:
- DeviceString property Virtual PC
- DeviceString property Virtual PC , IVMUSBDevice interface
- IVMUSBDevice interface Virtual PC , DeviceString property
topic_type:
- apiref
api_name:
- IVMUSBDevice.DeviceString
- IVMUSBDevice.get_DeviceString
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDevice::DeviceString property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the name of the USB device.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceString(
  [out, retval] BSTR *deviceName
);
```



## Property value

The name of the USB device.

## Error codes



| Name/value                                                                                                                                            | Meaning                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>               | The method completed successfully.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl> | The parameter is **NULL**.<br/>         |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMUSBDevice is defined as 63C1258C-5721-4070-B86B-A6CE2AFEC0B3<br/>               |



## See also

<dl> <dt>

[**IVMUSBDevice**](ivmusbdevice.md)
</dt> </dl>

 

