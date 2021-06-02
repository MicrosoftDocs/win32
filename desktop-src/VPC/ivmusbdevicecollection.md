---
title: IVMUSBDeviceCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of USB devices attached to the host system. To obtain an IVMUSBDeviceCollection object, use the IVMVirtualPC USBDeviceCollection property.
ms.assetid: a5cca485-29d3-47fa-9cda-fedcdc379155
keywords:
- IVMUSBDeviceCollection interface Virtual PC
- IVMUSBDeviceCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMUSBDeviceCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDeviceCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of USB devices attached to the host system. To obtain an **IVMUSBDeviceCollection** object, use the [**IVMVirtualPC::USBDeviceCollection**](ivmvirtualpc-usbdevicecollection.md) property.

## Members

The **IVMUSBDeviceCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMUSBDeviceCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMUSBDeviceCollection** interface has these properties.



| Property                                                        | Access type          | Description                                                                         |
|:----------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmusbdevicecollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                        |
| [**Count**](ivmusbdevicecollection-count.md)<br/>        | Read-only<br/> | The number of USB devices in this collection.<br/>                            |
| [**Item**](ivmusbdevicecollection-item.md)<br/>          | Read-only<br/> | The USB device object that corresponds to the specified index (1-based).<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMUSBDeviceCollection is defined as 4FBCD6A5-F53C-4d1c-9F4D-E90ABB8B3749<br/>     |



## See also

<dl> <dt>

[**IVMUSBDevice**](ivmusbdevice.md)
</dt> <dt>

[**IVMVirtualPC::USBDeviceCollection**](ivmvirtualpc-usbdevicecollection.md)
</dt> </dl>

 

