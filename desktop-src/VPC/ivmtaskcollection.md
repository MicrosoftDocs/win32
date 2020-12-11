---
title: IVMTaskCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of task objects. To obtain an IVMTaskCollection object, use the IVMVirtualPC Tasks property.
ms.assetid: 5cfc543c-81a1-49d2-93a9-9b1db1cb5070
keywords:
- IVMTaskCollection interface Virtual PC
- IVMTaskCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMTaskCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMTaskCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of task objects. To obtain an **IVMTaskCollection** object, use the [**IVMVirtualPC::Tasks**](ivmvirtualpc-tasks.md) property.

## Members

The **IVMTaskCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMTaskCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMTaskCollection** interface has these properties.



| Property                                                   | Access type          | Description                                                         |
|:-----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------|
| [**\_NewEnum**](ivmtaskcollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                        |
| [**Count**](ivmtaskcollection-count.md)<br/>        | Read-only<br/> | The number of tasks in this collection.<br/>                  |
| [**Item**](ivmtaskcollection-item.md)<br/>          | Read-only<br/> | The task object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMTaskCollection is defined as 5c4387c8-0e8b-4b97-8058-84679adf4c40<br/>          |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> <dt>

[**IVMVirtualPC::Tasks**](ivmvirtualpc-tasks.md)
</dt> </dl>

 

