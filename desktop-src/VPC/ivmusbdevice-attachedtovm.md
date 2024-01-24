---
title: IVMUSBDevice AttachedToVM property (VPCCOMInterfaces.h)
description: Retrieves the name of the virtual machine to which the USB Device is attached.
ms.assetid: 214ed891-1fca-4311-945a-0ce3d05d604e
keywords:
- AttachedToVM property Virtual PC
- AttachedToVM property Virtual PC , IVMUSBDevice interface
- IVMUSBDevice interface Virtual PC , AttachedToVM property
topic_type:
- apiref
api_name:
- IVMUSBDevice.AttachedToVM
- IVMUSBDevice.get_AttachedToVM
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDevice::AttachedToVM property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the name of the virtual machine to which the USB Device is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_AttachedToVM(
  [out, retval] BSTR *ConfigName
);
```



## Property value

The name of the virtual machine (VM).

## Error codes



| Name/value                                                                                                                                                           | Meaning                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                              | The device is attached to the VM, and its name is returned.<br/> |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                           | The device is attached to the host.<br/>                         |
| <dl> <dt>VM\_E\_USB\_EXTERNAL\_VM</dt> <dt>0xA00400929</dt> </dl> | The device is attached to a VM in another user session.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                | The parameter is **NULL**.<br/>                                  |



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

 

