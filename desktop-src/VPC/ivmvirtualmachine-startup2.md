---
title: IVMVirtualMachine Startup2 method (VPCCOMInterfaces.h)
description: Starts the virtual machine from either the uninitialized or saved state, with advanced options.
ms.assetid: c2679ea1-bbd5-42dc-9326-2019ad99554c
keywords:
- Startup2 method Virtual PC
- Startup2 method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Startup2 method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Startup2
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Startup2 method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Starts the virtual machine (VM) from either the uninitialized or saved state, with advanced options.

This method provides a mechanism to start a VM with a differencing disk even if the parent disk's timestamp has been changed.

## Syntax


```C++
HRESULT Startup2(
  [in]          VMStartupOption startupOption,
  [out, retval] IVMTask         **startupTask
);
```



## Parameters

<dl> <dt>

*startupOption* \[in\]
</dt> <dd>

The advanced startup option. The possible values are from the [**VMStartupOption**](vmstartupoption.md) enumeration.

</dd> <dt>

*startupTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion progress of the start sequence.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                          | Description                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                | The operation was successful.<br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                               | The *startupOption* parameter is not valid.<br/>                       |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                  | The *startupTask* parameter is **NULL**.<br/>                          |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED)**</dt> <dt>0x80070005</dt> </dl> | The caller must have execute access permissions to start this VM.<br/> |
| <dl> <dt>**VM\_E\_TIMED\_OUT**</dt> <dt>0xA0040202</dt> </dl>                           | The operation did not complete in a timely manner.<br/>                |
| <dl> <dt>**VM\_E\_OUT\_OF\_RESOURCE**</dt> <dt>0xA0040203</dt> </dl>                    | There are not enough host resources.<br/>                              |
| <dl> <dt>**VM\_E\_TOO\_MANY\_VMS**</dt> <dt>0xA0040204</dt> </dl>                       | There are too many active VMs.<br/>                                    |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> <dt>0xA0040500</dt> </dl>                          | The VM is already running.<br/>                                        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                          | An unexpected error has occurred.<br/>                                 |



 

## Remarks

The following values can be returned through the [**Error**](ivmtask-error.md) property of the returned [**IVMTask**](ivmtask.md) object.



| [**Error**](ivmtask-error.md) code/Value                                                                                                                                                                                                                                      | Description                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="VM_E_UNSUPPORTED_HARDWARE__0xA0040950_"></span><span id="vm_e_unsupported_hardware__0xa0040950_"></span><span id="VM_E_UNSUPPORTED_HARDWARE__0XA0040950_"></span>`VM_E_UNSUPPORTED_HARDWARE` (0xA0040950)<br/>                                                 | The hardware does not support virtualization.<br/>              |
| <span id="VM_E_HARDWARE_VIRTUALIZATION_DISABLED__0xA0040951_"></span><span id="vm_e_hardware_virtualization_disabled__0xa0040951_"></span><span id="VM_E_HARDWARE_VIRTUALIZATION_DISABLED__0XA0040951_"></span>`VM_E_HARDWARE_VIRTUALIZATION_DISABLED` (0xA0040951)<br/> | Hardware virtualization is disabled.<br/>                       |
| <span id="VM_E_VMVIRTUALPC_OLDER_VERSION__0xA0040952_"></span><span id="vm_e_vmvirtualpc_older_version__0xa0040952_"></span><span id="VM_E_VMVIRTUALPC_OLDER_VERSION__0XA0040952_"></span>`VM_E_VMVIRTUALPC_OLDER_VERSION` (0xA0040952)<br/>                             | Both Virtual PC 2007 and Windows Virtual PC are installed.<br/> |
| <span id="VM_E_OTHER_VIRTUALIZATION_SOFTWARE__0xA0040953_"></span><span id="vm_e_other_virtualization_software__0xa0040953_"></span><span id="VM_E_OTHER_VIRTUALIZATION_SOFTWARE__0XA0040953_"></span>`VM_E_OTHER_VIRTUALIZATION_SOFTWARE` (0xA0040953)<br/>             | Other virtualization software is installed.<br/>                |
| <span id="VM_E_OUT_OF_RESOURCE__0xa00400203_"></span><span id="vm_e_out_of_resource__0xa00400203_"></span><span id="VM_E_OUT_OF_RESOURCE__0XA00400203_"></span>`VM_E_OUT_OF_RESOURCE` (0xa00400203)<br/>                                                                 | There are not enough host resources.<br/>                       |



 

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

 

