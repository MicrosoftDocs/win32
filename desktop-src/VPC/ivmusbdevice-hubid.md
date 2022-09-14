---
title: IVMUSBDevice HubID property (VPCCOMInterfaces.h)
description: Retrieves the identifier of the hub on which the device is connected.
ms.assetid: 22e1d8fb-33f4-43a3-883f-174ddafa17c2
keywords:
- HubID property Virtual PC
- HubID property Virtual PC , IVMUSBDevice interface
- IVMUSBDevice interface Virtual PC , HubID property
topic_type:
- apiref
api_name:
- IVMUSBDevice.HubID
- IVMUSBDevice.get_HubID
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDevice::HubID property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the identifier of the hub on which the device is connected.

This property is read-only.

## Syntax


```C++
HRESULT get_HubID(
  [out, retval] long *hubID
);
```



## Property value

The hub identifier. This value is assigned by the USB connector driver.

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

 

