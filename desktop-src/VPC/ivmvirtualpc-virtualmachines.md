---
title: IVMVirtualPC VirtualMachines property (VPCCOMInterfaces.h)
description: Retrieves an enumerable collection of virtual machines.
ms.assetid: 9e8dcd65-7cf8-4cdd-a412-62cbb96eb8ec
keywords:
- VirtualMachines property Virtual PC
- VirtualMachines property Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , VirtualMachines property
topic_type:
- apiref
api_name:
- IVMVirtualPC.VirtualMachines
- IVMVirtualPC.get_VirtualMachines
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::VirtualMachines property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an enumerable collection of virtual machines.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualMachines(
  [out, retval] IVMVirtualMachineCollection **virtualMachineCollection
);
```



## Property value

A collection of [**IVMVirtualMachine**](ivmvirtualmachine.md) objects. See [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md).

## Error codes



| Name/value                                                                                                                                                                           | Meaning                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                | The parameter is **NULL**.<br/>                                                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



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

 

