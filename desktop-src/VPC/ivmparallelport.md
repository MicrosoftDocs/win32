---
title: IVMParallelPort interface
description: Defines a parallel port inside a virtual machine.
ms.assetid: 'da8daf16-5d22-49be-8fe9-72d5018c0622'
keywords: ["IVMParallelPort interface Virtual PC", "IVMParallelPort interface Virtual PC , described"]
topic_type:
- apiref
api_name:
- IVMParallelPort
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
---

# IVMParallelPort interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Defines a parallel port inside a virtual machine. This interface allows you to configure parallel ports inside a virtual machine. You can retrieve an **IVMParallelPort** object from the [**IVMParallelPortCollection**](ivmparallelportcollection.md) object returned from the [**IVMVirtualMachine::ParallelPorts**](ivmvirtualmachine-parallelports.md) property.

## Members

The **IVMParallelPort** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMParallelPort** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMParallelPort** interface has these methods.



| Method                              | Description                                                        |
|:------------------------------------|:-------------------------------------------------------------------|
| [**\_ID**](ivmparallelport--id.md) | Retrieves the internal identifier of the parallel port.<br/> |



 

### Properties

The **IVMParallelPort** interface has these properties.



| Property                                        | Access type           | Description                               |
|:------------------------------------------------|:----------------------|:------------------------------------------|
| [**Name**](ivmparallelport-name.md)<br/> | Read/write<br/> | The name of the parallel port.<br/> |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMParallelPort is defined as 097beecb-0a02-474f-abd6-298b22293fc6<br/>            |



 

 





