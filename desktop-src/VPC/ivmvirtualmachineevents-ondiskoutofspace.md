---
title: IVMVirtualMachineEvents OnDiskOutOfSpace method (VPCCOMInterfaces.h)
description: Receives notification that a disk required for a VM is low on free space.
ms.assetid: 1c431904-fffd-4513-8670-b9723f53edf1
keywords:
- OnDiskOutOfSpace method Virtual PC
- OnDiskOutOfSpace method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnDiskOutOfSpace method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnDiskOutOfSpace
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnDiskOutOfSpace method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a disk required for a virtual machine (VM) is low on free space. If free space drops below 100 MB this event is received as a warning and if free space drops below 20 MB this event is received again as an error and the VM will be paused.

## Syntax


```C++
HRESULT OnDiskOutOfSpace(
  [in] VARIANT_BOOL criticallyLow
);
```



## Parameters

<dl> <dt>

*criticallyLow* \[in\]
</dt> <dd>

Set to **VARIANT\_TRUE** if the disk has less than 20 MB free and to **VARIANT\_FALSE** if the free space is more than 20 MB but less than 100 MB.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMVirtualMachineEvents is defined as 9d84f560-bb67-4961-bd12-a4da780c67e4<br/>   |



## See also

<dl> <dt>

[**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)
</dt> </dl>

 

