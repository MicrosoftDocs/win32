---
title: IVMUSBDevice interface (VPCCOMInterfaces.h)
description: Defines the interface for a USB device attached to host. You can attach USB device to a virtual machine to use the device inside the virtual machine.
ms.assetid: f491fe8f-bc43-4dfa-b9c1-c93b4e5a7df6
keywords:
- IVMUSBDevice interface Virtual PC
- IVMUSBDevice interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMUSBDevice
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDevice interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the interface for a USB device attached to host. You can attach USB device to a virtual machine to use the device inside the virtual machine.

## Members

The **IVMUSBDevice** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMUSBDevice** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMUSBDevice** interface has these properties.



| Property                                                                 | Access type          | Description                                                                     |
|:-------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------|
| [**AttachedToVM**](ivmusbdevice-attachedtovm.md)<br/>             | Read-only<br/> | The name of the virtual machine to which the USB device is attached.<br/> |
| [**DeviceClass**](ivmusbdevice-deviceclass.md)<br/>               | Read-only<br/> | The device class of the USB device.<br/>                                  |
| [**DeviceString**](ivmusbdevice-devicestring.md)<br/>             | Read-only<br/> | The name of the USB device.<br/>                                          |
| [**HubID**](ivmusbdevice-hubid.md)<br/>                           | Read-only<br/> | The identifier of the hub on which the device is connected.<br/>          |
| [**ManufacturerString**](ivmusbdevice-manufacturerstring.md)<br/> | Read-only<br/> | The name of the USB device manufacturer.<br/>                             |
| [**Port**](ivmusbdevice-port.md)<br/>                             | Read-only<br/> | The identifier of the port on which the device is connected.<br/>         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMUSBDevice is defined as 63C1258C-5721-4070-B86B-A6CE2AFEC0B3<br/>               |



 

