---
title: IVMDVDDriveCollection interface
description: The IVMDVDDriveCollection interface defines the collection of DVD drives within the virtual machine. An IVMDVDDriveCollection object is returned from the IVMVirtualMachine DVDROMDrives property.
ms.assetid: 6c3bc962-1907-4895-bcb0-8c54d467a39c
keywords:
- IVMDVDDriveCollection interface Virtual Server
- IVMDVDDriveCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMDVDDriveCollection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMDVDDriveCollection interface

The **IVMDVDDriveCollection** interface defines the collection of DVD drives within the virtual machine. An **IVMDVDDriveCollection** object is returned from the [**IVMVirtualMachine::DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md) property.

## Members

The **IVMDVDDriveCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMDVDDriveCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMDVDDriveCollection** interface has these properties.



| Property                                                       | Access type          | Description                                                                                                      |
|:---------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmdvddrivecollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                    |
| [**Count**](ivmdvddrivecollection-count.md)<br/>        | Read-only<br/> | The number of DVD drives defined in this collection.<br/>                                                  |
| [**Item**](ivmdvddrivecollection-item.md)<br/>          | Read-only<br/> | The [**IVMDVDDrive**](ivmdvddrive.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





