---
title: IVMVirtualMachine AttachedDriveTypes property (VPCCOMInterfaces.h)
description: An array indicating the type of drive attached to each location in the VM.
ms.assetid: 6896c9cd-5448-4fbb-8c8e-eef306a5cea1
keywords:
- AttachedDriveTypes property Virtual PC
- AttachedDriveTypes property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , AttachedDriveTypes property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AttachedDriveTypes
- IVMVirtualMachine.get_AttachedDriveTypes
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::AttachedDriveTypes property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an array indicating the type of drive attached to each location in the virtual machine (VM).

This property is read-only.

## Syntax


```C++
HRESULT get_AttachedDriveTypes(
  [out, retval] VARIANT *driveTypes
);
```



## Property value

A variant of type **VT\_ARRAY** \| **VT\_VARIANT** containing entries of type **VT\_UI1**. The array contains the [**VMDriveType**](vmdrivetype.md) value of each device connected to every bus location. The array is ordered by \[*busNumber*\]\[*deviceID*\].

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



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

 

