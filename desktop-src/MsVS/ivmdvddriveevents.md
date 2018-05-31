---
title: IVMDVDDriveEvents interface
description: Defines the outgoing event interface for the IVMDVDDrive interface.
ms.assetid: e5a641b1-bd08-4bb7-8628-5c5603998ccc
keywords:
- IVMDVDDriveEvents interface Virtual Server
- IVMDVDDriveEvents interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMDVDDriveEvents
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

# IVMDVDDriveEvents interface

The **IVMDVDDriveEvents** interface defines the outgoing event interface for the [**IVMDVDDrive**](ivmdvddrive.md) interface.

## When to implement

The client implements these methods to receive events sent from [**IVMDVDDrive**](ivmdvddrive.md).

## Members

The **IVMDVDDriveEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IVMDVDDriveEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMDVDDriveEvents** interface has these methods.



| Method                                                   | Description                                                                                        |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**OnMediaEject**](ivmdvddriveevents-onmediaeject.md)   | Called when an ISO image is detached or when physical media is ejected from the drive.<br/>  |
| [**OnMediaInsert**](ivmdvddriveevents-onmediainsert.md) | Called when an ISO image is attached or when physical media is inserted into the drive.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





