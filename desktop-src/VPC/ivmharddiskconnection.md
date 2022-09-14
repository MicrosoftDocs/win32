---
title: IVMHardDiskConnection interface (VPCCOMInterfaces.h)
description: Defines the connection for a hard disk within the virtual machine.
ms.assetid: 7ba1ace5-a3af-4b97-b329-f12a0ecbf7d3
keywords:
- IVMHardDiskConnection interface Virtual PC
- IVMHardDiskConnection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMHardDiskConnection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDiskConnection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the connection for a hard disk within the virtual machine. An **IVMHardDiskConnection** object is returned from the [**IVMVirtualMachine::AddHardDiskConnection**](ivmvirtualmachine-addharddiskconnection.md) method. You can also retrieve an **IVMHardDiskConnection** object from the [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md) object returned from the [**IVMVirtualMachine::HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md) property.

## Members

The **IVMHardDiskConnection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMHardDiskConnection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMHardDiskConnection** interface has these methods.



| Method                                                         | Description                                                           |
|:---------------------------------------------------------------|:----------------------------------------------------------------------|
| [**SetBusLocation**](ivmharddiskconnection-setbuslocation.md) | Sets the bus location to which this hard disk is attached.<br/> |



 

### Properties

The **IVMHardDiskConnection** interface has these properties.



| Property                                                              | Access type          | Description                                                                       |
|:----------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------|
| [**BusNumber**](ivmharddiskconnection-busnumber.md)<br/>       | Read-only<br/> | The bus number to which the drive image is attached.<br/>                   |
| [**DeviceNumber**](ivmharddiskconnection-devicenumber.md)<br/> | Read-only<br/> | The device number to which the drive image is attached.<br/>                |
| [**HardDisk**](ivmharddiskconnection-harddisk.md)<br/>         | Read-only<br/> | A hard disk object corresponding to this connection.<br/>                   |
| [**UndoHardDisk**](ivmharddiskconnection-undoharddisk.md)<br/> | Read-only<br/> | A hard disk object corresponding to this connection's undo disk image.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHardDiskconnection is defined as aefa36a5-463a-46ae-9e6c-a1fb4e12e671<br/>      |



 

