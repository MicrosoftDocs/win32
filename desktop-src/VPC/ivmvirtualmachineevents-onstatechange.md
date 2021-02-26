---
title: IVMVirtualMachineEvents OnStateChange method (VPCCOMInterfaces.h)
description: Receives notification that a virtual machine's state has changed. | IVMVirtualMachineEvents OnStateChange method (VPCCOMInterfaces.h)
ms.assetid: 1737bb5e-078d-4ebe-9558-de083aae1baa
keywords:
- OnStateChange method Virtual PC
- OnStateChange method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnStateChange method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnStateChange
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnStateChange method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a virtual machine's state has changed.

## Syntax


```C++
HRESULT OnStateChange(
  [in] VMVMState virtualMachineState
);
```



## Parameters

<dl> <dt>

*virtualMachineState* \[in\]
</dt> <dd>

The new state of the virtual machine. For a list of values, see [**VMVMState**](vmvmstate.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when the state for this virtual machine changes. The client program must implement this interface method to receive notification of the vmVirtualMachineEvent\_StateChanged event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

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

 

