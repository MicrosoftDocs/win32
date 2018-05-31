---
title: IVMFloppyDriveEvents interface
description: Defines the outgoing event interface for the IVMFloppyDrive interface.
ms.assetid: 3c350c36-75eb-4dc9-a6f0-3bfe0e7a3893
keywords:
- IVMFloppyDriveEvents interface Virtual Server
- IVMFloppyDriveEvents interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMFloppyDriveEvents
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

# IVMFloppyDriveEvents interface

The **IVMFloppyDriveEvents** interface defines the outgoing event interface for the [**IVMFloppyDrive**](ivmfloppydrive.md) interface.

## When to implement

The client implements these methods to receive events sent from [**IVMFloppyDrive**](ivmfloppydrive.md).

## Members

The **IVMFloppyDriveEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IVMFloppyDriveEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMFloppyDriveEvents** interface has these methods.



| Method                                                      | Description                                                                                               |
|:------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**OnMediaEject**](ivmfloppydriveevents-onmediaeject.md)   | Called when a floppy disk image is detached or when physical media is ejected from the drive.<br/>  |
| [**OnMediaInsert**](ivmfloppydriveevents-onmediainsert.md) | Called when a floppy disk image is attached or when physical media is inserted into the drive.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





