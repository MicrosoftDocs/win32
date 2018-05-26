---
title: IVMTask interface
description: The IVMTask interface provides a method for managing tasks which are asynchronous to the COM method invoked.
ms.assetid: 4571f70f-51e3-46dc-924f-da6b3189ca29
keywords:
- IVMTask interface Virtual Server
- IVMTask interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMTask
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMTask interface

The **IVMTask** interface provides a method for managing tasks which are asynchronous to the COM method invoked.

## When to use

Use the **IVMTask** interface to monitor and control asynchronous tasks for COM methods.

## Inheritance

The **IVMTask** interface has been extended by the following interface:

-   [**IVMTask2**](ivmtask2.md)

## Members

The **IVMTask** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMTask** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMTask** interface has these methods.



| Method                                                 | Description                                                                                                                                                                 |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](ivmtask-cancel.md)                       | Cancels the task.<br/>                                                                                                                                                |
| [**WaitForCompletion**](ivmtask-waitforcompletion.md) | Waits for the task to complete or until the specified timeout expires.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md)) |



 

### Properties

The **IVMTask** interface has these properties.



| Property                                                        | Access type          | Description                                                                                                                                                        |
|:----------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Description**](ivmtask-description.md)<br/>           | Read-only<br/> | The description of the task.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md))                                  |
| [**ID**](ivmtask-id.md)<br/>                             | Read-only<br/> | The unique ID for the task.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md))                                   |
| [**IsCancelable**](ivmtask-iscancelable.md)<br/>         | Read-only<br/> | Indicates whether the task can be canceled before completion.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md)) |
| [**IsComplete**](ivmtask-iscomplete.md)<br/>             | Read-only<br/> | Indicates whether the task has completed.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md))                     |
| [**PercentCompleted**](ivmtask-percentcompleted.md)<br/> | Read-only<br/> | The completion percentage of the task.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md))                        |
| [**Result**](ivmtask-result.md)<br/>                     | Read-only<br/> | The result of the task.<br/> (Inherited from **IVMTaskVMTask**[**IVMTask2**](ivmtask2.md)[**VMTask2**](ivmtask2.md))                                       |



 

## Remarks

An **IVMTask** object is returned by methods which could potentially require a significant amount of time to complete. This allows the user program to monitor the progress of the desired operation without forcing the program to block further execution while waiting for the completion of the operation.

The following methods return an IVMTask object:

-   [**IVMGuestOS::Shutdown**](ivmguestos-shutdown.md)
-   [**IVMHardDisk::Compact**](ivmharddisk-compact.md)
-   [**IVMHardDisk::Convert**](ivmharddisk-convert.md)
-   [**IVMHardDisk::Merge**](ivmharddisk-merge.md)
-   [**IVMHardDisk::MergeTo**](ivmharddisk-mergeto.md)
-   [**IVMVirtualMachine::MergeUndoDisks**](ivmvirtualmachine-mergeundodisks.md)
-   [**IVMVirtualMachine::Reset**](ivmvirtualmachine-reset.md)
-   [**IVMVirtualMachine::Save**](ivmvirtualmachine-save.md)
-   [**IVMVirtualMachine::Startup**](ivmvirtualmachine-startup.md)
-   [**IVMVirtualMachine::Turnoff**](ivmvirtualmachine-turnoff.md)
-   [**IVMVirtualServer::CreateDifferencingVirtualHardDisk**](ivmvirtualserver-createdifferencingvirtualharddisk.md)
-   [**IVMVirtualServer::CreateDynamicVirtualHardDisk**](ivmvirtualserver-createdynamicvirtualharddisk.md)
-   [**IVMVirtualServer::CreateFixedVirtualHardDisk**](ivmvirtualserver-createfixedvirtualharddisk.md)
-   [**IVMVirtualServer::CreateHostDriveVirtualHardDisk**](ivmvirtualserver-createhostdrivevirtualharddisk.md)

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





