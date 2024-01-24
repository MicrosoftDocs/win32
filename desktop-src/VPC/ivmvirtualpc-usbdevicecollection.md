---
title: IVMVirtualPC USBDeviceCollection property (VPCCOMInterfaces.h)
description: An enumerable collection of all USB devices connected to the host.
ms.assetid: 80844912-15b1-44d1-8d07-dca90c579927
keywords:
- USBDeviceCollection property Virtual PC
- USBDeviceCollection property Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , USBDeviceCollection property
topic_type:
- apiref
api_name:
- IVMVirtualPC.USBDeviceCollection
- IVMVirtualPC.get_USBDeviceCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::USBDeviceCollection property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an enumerable collection of all USB devices connected to the host.

This property is read-only.

## Syntax


```C++
HRESULT get_USBDeviceCollection(
  [out, retval] IVMUSBDeviceCollection **usbDeviceCollection
);
```



## Property value

A reference to an [**IVMUSBDeviceCollection**](ivmusbdevicecollection.md) pointer that represents a collection of [**IVMUSBDevice**](ivmusbdevice.md) objects.

## Error codes



| Name/value                                                                                                                                                                                | Meaning                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                   | The operation was successful.<br/>                                                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                     | The parameter is **NULL**.<br/>                                                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                             | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>VM\_E\_USB\_ENUMERATION\_FAILED\_MORE\_DEVICES</dt> <dt>0xA0040930</dt> </dl> | More than 16 USB devices are connected to the host.<br/>                                  |
| <dl> <dt>VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED</dt> <dt>0xA0040951</dt> </dl>      | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

