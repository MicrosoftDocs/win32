---
title: IVMTask interface (VPCCOMInterfaces.h)
description: Use the IVMTask interface to monitor and control asynchronous tasks for various COM methods.
ms.assetid: 9b593444-80f5-43e9-9b95-1a2150c66efd
keywords:
- IVMTask interface Virtual PC
- IVMTask interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMTask
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMTask interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Use the **IVMTask** interface to monitor and control asynchronous tasks for various COM methods.

## Members

The **IVMTask** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMTask** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMTask** interface has these methods.



| Method                                                 | Description                                                                                 |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**Cancel**](ivmtask-cancel.md)                       | Cancels the task.<br/>                                                                |
| [**WaitForCompletion**](ivmtask-waitforcompletion.md) | Waits for the task to complete or for the specified time-out interval to elapse.<br/> |



 

### Properties

The **IVMTask** interface has these properties.



| Property                                                        | Access type          | Description                                                        |
|:----------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Description**](ivmtask-description.md)<br/>           | Read-only<br/> | A description of the task.<br/>                              |
| [**Error**](ivmtask-error.md)<br/>                       | Read-only<br/> | The error recorded for this task.<br/>                       |
| [**ErrorDescription**](ivmtask-errordescription.md)<br/> | Read-only<br/> | The localized error description recorded for this task.<br/> |
| [**ID**](ivmtask-id.md)<br/>                             | Read-only<br/> | A unique identifier for this task.<br/>                      |
| [**IsCancelable**](ivmtask-iscancelable.md)<br/>         | Read-only<br/> | Indicates whether the task can be canceled.<br/>             |
| [**IsComplete**](ivmtask-iscomplete.md)<br/>             | Read-only<br/> | Indicates whether the task has completed.<br/>               |
| [**PercentCompleted**](ivmtask-percentcompleted.md)<br/> | Read-only<br/> | The completion percentage of the task.<br/>                  |
| [**Result**](ivmtask-result.md)<br/>                     | Read-only<br/> | The result of the task.<br/>                                 |



 

## Remarks

An **IVMTask** object is returned by methods that could potentially require a significant amount of time to complete. This allows the application to monitor the progress of the desired operation without forcing it to block further execution while waiting for the completion of the operation.

The following methods return an **IVMTask** object that can be used to track progress:

-   [**IVMGuestOS::Logoff**](ivmguestos-logoff.md)
-   [**IVMGuestOS::Restart**](ivmguestos-restart.md)
-   [**IVMGuestOS::Shutdown**](ivmguestos-shutdown.md)
-   [**IVMHardDisk::Compact**](ivmharddisk-compact.md)
-   [**IVMHardDisk::Convert**](ivmharddisk-convert.md)
-   [**IVMHardDisk::Merge**](ivmharddisk-merge.md)
-   [**IVMHardDisk::MergeTo**](ivmharddisk-mergeto.md)
-   [**IVMVirtualMachine::MergeUndoDisks**](ivmvirtualmachine-mergeundodisks.md)
-   [**IVMVirtualMachine::Reset**](ivmvirtualmachine-reset.md)
-   [**IVMVirtualMachine::Save**](ivmvirtualmachine-save.md)
-   [**IVMVirtualMachine::Startup**](ivmvirtualmachine-startup.md)
-   [**IVMVirtualMachine::Startup2**](ivmvirtualmachine-startup2.md)
-   [**IVMVirtualMachine::TurnOff**](ivmvirtualmachine-turnoff.md)
-   [**IVMVirtualPC::CreateDifferencingVirtualHardDisk**](ivmvirtualpc-createdifferencingvirtualharddisk.md)
-   [**IVMVirtualPC::CreateDynamicVirtualHardDisk**](ivmvirtualpc-createdynamicvirtualharddisk.md)
-   [**IVMVirtualPC::CreateFixedVirtualHardDisk**](ivmvirtualpc-createfixedvirtualharddisk.md)

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMTask is defined as ab72b222-6e9c-48ae-aa54-85e3e635767c<br/>                    |



 

