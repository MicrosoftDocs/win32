---
title: IVMVirtualPC UnregisterVirtualMachine method (VPCCOMInterfaces.h)
description: Unregisters a VM configuration without deleting the configuration file.
ms.assetid: 82ca6ef3-e9e5-471e-b2dc-0ff689a618d9
keywords:
- UnregisterVirtualMachine method Virtual PC
- UnregisterVirtualMachine method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , UnregisterVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualPC.UnregisterVirtualMachine
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::UnregisterVirtualMachine method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Unregisters a virtual machine (VM) configuration without deleting the configuration file.

## Syntax


```C++
HRESULT UnregisterVirtualMachine(
  [in] IVMVirtualMachine *virtualMachine
);
```



## Parameters

<dl> <dt>

*virtualMachine* \[in\]
</dt> <dd>

A pointer to an [**IVMVirtualMachine**](ivmvirtualmachine.md) object that represents the VM configuration to be unregistered.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                        | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                | The *virtualMachine* parameter was **NULL**.<br/>                                         |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> <dt>0xA0040500</dt> </dl>                        | The VM is running.<br/>                                                                   |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |



 

## Remarks

Only stopped VMs can be unregistered. Existing saved state or undo drive data for this configuration will be retained when a VM is unregistered.

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

 

