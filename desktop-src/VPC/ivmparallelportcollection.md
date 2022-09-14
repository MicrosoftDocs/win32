---
title: IVMParallelPortCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of parallel ports within the virtual machine. To obtain an IVMParallelPortCollection object, use the IVMVirtualMachine ParallelPorts property.
ms.assetid: 038a5c08-cd92-426f-a059-9a4c2110548d
keywords:
- IVMParallelPortCollection interface Virtual PC
- IVMParallelPortCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMParallelPortCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMParallelPortCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of parallel ports within the virtual machine. To obtain an **IVMParallelPortCollection** object, use the [**IVMVirtualMachine::ParallelPorts**](ivmvirtualmachine-parallelports.md) property.

## Members

The **IVMParallelPortCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMParallelPortCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMParallelPortCollection** interface has these properties.



| Property                                                           | Access type          | Description                                                                  |
|:-------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------|
| [**\_NewEnum**](ivmparallelportcollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                 |
| [**Count**](ivmparallelportcollection-count.md)<br/>        | Read-only<br/> | The number of parallel ports in this collection.<br/>                  |
| [**Item**](ivmparallelportcollection-item.md)<br/>          | Read-only<br/> | The parallel port object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMParallelPortCollection is defined as 27c3e036-198f-430c-8735-6e652f7203fd<br/>  |



## See also

<dl> <dt>

[**IVMParallelPort**](ivmparallelport.md)
</dt> <dt>

[**IVMVirtualMachine::ParallelPorts**](ivmvirtualmachine-parallelports.md)
</dt> </dl>

 

