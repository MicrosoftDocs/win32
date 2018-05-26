---
title: IVMTask2 interface
description: The IVMTask2 interface extends the IVMTask interface, adding a property to return the remote HRESULT value and a text description of the error.
ms.assetid: dd3530d7-a803-4bfd-a579-9c85e4c586c7
keywords:
- IVMTask2 interface Virtual Server
- IVMTask2 interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMTask2
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

# IVMTask2 interface

The **IVMTask2** interface extends the [**IVMTask**](ivmtask.md) interface, adding a property to return the remote **HRESULT** value and a text description of the error.

## When to use

Use the **IVMTask2** interface to monitor and control asynchronous tasks for COM methods.

## Members

The **IVMTask2** interface inherits from [**IVMTask**](ivmtask.md) and [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5). **IVMTask2** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMTask2** interface has these methods.



| Method                                                 | Description                                                                                                                                                               |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](ivmtask-cancel.md)                       | Cancels the task.<br/>                                                                                                                                              |
| [**WaitForCompletion**](ivmtask-waitforcompletion.md) | Waits for the task to complete or until the specified timeout expires.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**) |



 

### Properties

The **IVMTask2** interface has these properties.



| Property                                                         | Access type          | Description                                                                                                                                                      |
|:-----------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Description**](ivmtask-description.md)<br/>            | Read-only<br/> | The description of the task.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**)                                  |
| [**Error**](ivmtask2-error.md)<br/>                       | Read-only<br/> | The value (**HRESULT**) of the error.<br/> (Inherited from **IVMTask2VMTask2**)                                                                            |
| [**ErrorDescription**](ivmtask2-errordescription.md)<br/> | Read-only<br/> | The error description for this task.<br/> (Inherited from **IVMTask2VMTask2**)                                                                             |
| [**ID**](ivmtask-id.md)<br/>                              | Read-only<br/> | The unique ID for the task.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**)                                   |
| [**IsCancelable**](ivmtask-iscancelable.md)<br/>          | Read-only<br/> | Indicates whether the task can be canceled before completion.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**) |
| [**IsComplete**](ivmtask-iscomplete.md)<br/>              | Read-only<br/> | Indicates whether the task has completed.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**)                     |
| [**PercentCompleted**](ivmtask-percentcompleted.md)<br/>  | Read-only<br/> | The completion percentage of the task.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**)                        |
| [**Result**](ivmtask-result.md)<br/>                      | Read-only<br/> | The result of the task.<br/> (Inherited from [**IVMTask**](ivmtask.md)[**VMTask**](ivmtask.md)**IVMTask2VMTask2**)                                       |



 

## Remarks

An **IVMTask2** object is returned by methods which could potentially require a significant amount of time to complete. This allows the user program to monitor the progress of the desired operation without forcing the program to block further execution while waiting for the completion of the operation.

The following methods return an **IVMTask2** object:

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
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





