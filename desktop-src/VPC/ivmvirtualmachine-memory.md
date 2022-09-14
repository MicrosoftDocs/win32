---
title: IVMVirtualMachine Memory property (VPCCOMInterfaces.h)
description: Amount of physical memory in the virtual machine, in megabytes.
ms.assetid: 1a1d4cc7-a537-49f0-981f-0b72eca9013e
keywords:
- Memory property Virtual PC
- Memory property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Memory property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Memory
- IVMVirtualMachine.get_Memory
- IVMVirtualMachine.put_Memory
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Memory property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the amount of physical memory in the virtual machine, in megabytes.

This property is read/write.

## Syntax


```C++
HRESULT put_Memory(
  [in]          long megabytesOfMemory
);

HRESULT get_Memory(
  [out, retval] long *megabytesOfMemory
);
```



## Property value

Specifies the amount of physical memory, in megabytes.

## Error codes



| Name/value                                                                                                                                                         | Meaning                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>              | The parameter is **NULL**.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>           | The parameter is not valid or is out of range.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>                  |
| <dl> <dt>VM\_E\_PREF\_NOT\_FOUND</dt> <dt>0xA0040300</dt> </dl> | The preference was not found.<br/>                  |
| <dl> <dt>VM\_E\_PREF\_VM\_ACTIVE</dt> <dt>0xA0040302</dt> </dl> | The virtual machine is running or saved.<br/>       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>              |



## Remarks

The amount of physical memory in a virtual machine must be at least 4 MB. The upper limit on memory depends on the host configuration, but can be at most 3,712 MB.

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

 

