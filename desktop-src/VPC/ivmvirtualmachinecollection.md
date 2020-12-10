---
title: IVMVirtualMachineCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of virtual machines within Windows Virtual PC. To obtain an IVMVirtualMachineCollection object, use the IVMVirtualPC VirtualMachines property.
ms.assetid: 3d34e791-2dba-4529-b489-96a0c6227294
keywords:
- IVMVirtualMachineCollection interface Virtual PC
- IVMVirtualMachineCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualMachineCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of virtual machines within Windows Virtual PC. To obtain an **IVMVirtualMachineCollection** object, use the [**IVMVirtualPC::VirtualMachines**](ivmvirtualpc-virtualmachines.md) property.

## Members

The **IVMVirtualMachineCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualMachineCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMVirtualMachineCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                    |
|:---------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmvirtualmachinecollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                   |
| [**Count**](ivmvirtualmachinecollection-count.md)<br/>        | Read-only<br/> | The number of virtual machines in this collection.<br/>                  |
| [**Item**](ivmvirtualmachinecollection-item.md)<br/>          | Read-only<br/> | The virtual machine object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| End of client support<br/>    | Windows 7<br/>                                                                           |
| Product<br/>                  | Windows Virtual PC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl>  |
| IID<br/>                      | IID\_IVMVirtualMachineCollection is defined as 59f31786-2a3d-4fbf-9896-d85338ca0da1<br/> |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**IVMVirtualPC::VirtualMachines**](ivmvirtualpc-virtualmachines.md)
</dt> </dl>

 

