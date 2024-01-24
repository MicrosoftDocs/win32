---
title: IVMVirtualMachineEvents OnTripleFault method (VPCCOMInterfaces.h)
description: Receives notification that a virtual machine has triple-faulted.
ms.assetid: a17b1a05-3058-48ba-a196-7e9563f3e1c0
keywords:
- OnTripleFault method Virtual PC
- OnTripleFault method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnTripleFault method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnTripleFault
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnTripleFault method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a virtual machine has triple-faulted.

## Syntax


```C++
HRESULT OnTripleFault();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when a virtual machine has triple-faulted. The client program must implement this interface method to receive notification of the vmVirtualMachineEvent\_TripleFault event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

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

 

