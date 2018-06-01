---
title: IVMHardDiskConnection interface
description: The IVMHardDiskConnection interface defines the connection for a hard disk within the virtual machine.
ms.assetid: 98e2de69-13ca-455f-96b3-81a96f790c0f
keywords:
- IVMHardDiskConnection interface Virtual Server
- IVMHardDiskConnection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMHardDiskConnection
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMHardDiskConnection interface

The **IVMHardDiskConnection** interface defines the connection for a hard disk within the virtual machine. An **IVMHardDiskConnection** object is returned from the [**IVMVirtualMachine::AddHardDiskConnection**](ivmvirtualmachine-addharddiskconnection.md) method. You can also retrieve an **IVMHardDiskConnection** object from the [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md) object returned from the [**IVMVirtualMachine::HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md) property.

## Members

The **IVMHardDiskConnection** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMHardDiskConnection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMHardDiskConnection** interface has these methods.



| Method                                                         | Description                                                           |
|:---------------------------------------------------------------|:----------------------------------------------------------------------|
| [**SetBusLocation**](ivmharddiskconnection-setbuslocation.md) | Sets the bus location to which this hard disk is attached.<br/> |



 

### Properties

The **IVMHardDiskConnection** interface has these properties.



| Property                                                              | Access type          | Description                                                                                                 |
|:----------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------|
| [**BusNumber**](ivmharddiskconnection-busnumber.md)<br/>       | Read-only<br/> | The bus number that corresponds with this connection.<br/>                                            |
| [**BusType**](ivmharddiskconnection-bustype.md)<br/>           | Read-only<br/> | The type of bus (that is, IDE or SCSI) that corresponds with this connection.<br/>                    |
| [**DeviceNumber**](ivmharddiskconnection-devicenumber.md)<br/> | Read-only<br/> | The device number that corresponds with this connection.<br/>                                         |
| [**HardDisk**](ivmharddiskconnection-harddisk.md)<br/>         | Read-only<br/> | An [**IVMHardDisk**](ivmharddisk.md) object corresponding to this connection.<br/>                   |
| [**UndoHardDisk**](ivmharddiskconnection-undoharddisk.md)<br/> | Read-only<br/> | An [**IVMHardDisk**](ivmharddisk.md) object corresponding to this connection's undo disk image.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





