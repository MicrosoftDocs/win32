---
title: IVMVirtualMachine RemoveHardDiskConnection method
description: The RemoveHardDiskConnection method removes the specified hard disk connection from the virtual machine.
ms.assetid: 275d65a9-705e-41ff-825c-d5e3b8a75cd1
keywords:
- RemoveHardDiskConnection method Virtual Server
- RemoveHardDiskConnection method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , RemoveHardDiskConnection method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveHardDiskConnection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::RemoveHardDiskConnection method

The **RemoveHardDiskConnection** method removes the specified hard disk connection from the virtual machine.

## Syntax


```C++
HRESULT RemoveHardDiskConnection(
  [in] IVMHardDiskConnection *hardDiskConnection
);
```



## Parameters

<dl> <dt>

*hardDiskConnection* \[in\]
</dt> <dd>

Hard disk connection to remove from this virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                               |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                 | The operation was successful.<br/>                                                  |
| <dl> <dt> **E\_POINTER** </dt> </dl>           | The *hardDiskConnection* parameter is **NULL**.<br/>                                |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>    | The configuration is unknown.<br/>                                                  |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl>     | Virtual machine is running or saved.<br/>                                           |
| <dl> <dt> **VM\_E\_DRIVE\_INVALID**</dt> </dl> | Invalid drive specified (e.g. no hard disk is connected to this bus location).<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>    | An unexpected error has occurred.<br/>                                              |



 

## Remarks

You can only remove an existing hard disk connection from a stopped virtual machine. A list of connections currently attached to the virtual machine is obtained by enumerating the [**HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md) property.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





