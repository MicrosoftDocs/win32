---
title: IVMFloppyDriveCollection interface
description: The IVMFloppyDriveCollection interface defines a collection of floppy drives within the virtual machine. An IVMFloppyDriveCollection object is returned from the IVMVirtualMachine FloppyDrives property.
ms.assetid: 401d282b-d7bd-4189-b6b1-11414e1466f5
keywords:
- IVMFloppyDriveCollection interface Virtual Server
- IVMFloppyDriveCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMFloppyDriveCollection
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

# IVMFloppyDriveCollection interface

The **IVMFloppyDriveCollection** interface defines a collection of floppy drives within the virtual machine. An **IVMFloppyDriveCollection** object is returned from the [**IVMVirtualMachine::FloppyDrives**](ivmvirtualmachine-floppydrives.md) property.

## Members

The **IVMFloppyDriveCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMFloppyDriveCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMFloppyDriveCollection** interface has these properties.



| Property                                                          | Access type          | Description                                                                                                            |
|:------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmfloppydrivecollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                          |
| [**Count**](ivmfloppydrivecollection-count.md)<br/>        | Read-only<br/> | The number of floppy drives defined in this collection.<br/>                                                     |
| [**Item**](ivmfloppydrivecollection-item.md)<br/>          | Read-only<br/> | The [**IVMFloppyDrive**](ivmfloppydrive.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





