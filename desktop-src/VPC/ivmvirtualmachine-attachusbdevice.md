---
title: IVMVirtualMachine AttachUSBDevice method (VPCCOMInterfaces.h)
description: Attaches a USB device to a VM.
ms.assetid: 505078ee-9159-407d-ab8c-a9aba86dec48
keywords:
- AttachUSBDevice method Virtual PC
- AttachUSBDevice method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , AttachUSBDevice method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AttachUSBDevice
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::AttachUSBDevice method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches a USB device to a virtual machine (VM).

## Syntax


```C++
HRESULT AttachUSBDevice(
  [in] IVMUSBDevice *inUSBDevice
);
```



## Parameters

<dl> <dt>

*inUSBDevice* \[in\]
</dt> <dd>

A [**IVMUSBDevice**](ivmusbdevice.md) pointer that represents the USB device connected to the host.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                             | Description                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                   | The operation was successful.<br/>                                           |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                     | The parameter is **NULL**.<br/>                                              |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                        | The VM is not running.<br/>                                                  |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                             | The configuration is unknown.<br/>                                           |
| <dl> <dt>**VM\_E\_ADDITIONS\_NOT\_AVAIL**</dt> <dt>0xA0040504</dt> </dl>                   | Integration Components are not available in the guest operating system.<br/> |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl>          | The USB feature is not available.<br/>                                       |
| <dl> <dt>**VM\_E\_USB\_CONNECTOR\_DRIVER\_ERROR**</dt> <dt>0xA00400925</dt> </dl>          | There was a USB Connector driver error.<br/>                                 |
| <dl> <dt>**VM\_E\_USB\_ATTACH\_FAILED\_MORE\_DEVICES**</dt> <dt>0xA00400931</dt> </dl>     | Cannot attach more devices to the VM.<br/>                                   |
| <dl> <dt>**VM\_E\_USB\_ATTACH\_FAILED\_GP\_ERROR**</dt> <dt>0xA00400932</dt> </dl>         | A group policy setting is preventing the USB redirection.<br/>               |
| <dl> <dt>**VM\_E\_USB\_ATTACH\_FAILED\_ALREADY\_ASSIGNED**</dt> <dt>0xA00400933</dt> </dl> | A USB device has already been attached by some other client.<br/>            |
| <dl> <dt>**VM\_E\_USB\_ATTACH\_FAILED**</dt> <dt>0xA00400926</dt> </dl>                    | The attach operation failed.<br/>                                            |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                             | An unexpected error has occurred.<br/>                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

