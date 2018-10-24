---
title: IVMDVDDriveEvents interface
description: Defines the outgoing event interface for the IVMDVDDrive interface.
ms.assetid: aa68fb6f-032d-4322-8553-b1e840ae63b8
keywords:
- IVMDVDDriveEvents interface Virtual PC
- IVMDVDDriveEvents interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMDVDDriveEvents
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMDVDDriveEvents interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Defines the outgoing event interface for the [**IVMDVDDrive**](ivmdvddrive.md) interface.

## Members

The **IVMDVDDriveEvents** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **IVMDVDDriveEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMDVDDriveEvents** interface has these methods.



| Method                                                   | Description                                                                   |
|:---------------------------------------------------------|:------------------------------------------------------------------------------|
| [**OnMediaEject**](ivmdvddriveevents-onmediaeject.md)   | Receives notification that media has been ejected from the drive.<br/>  |
| [**OnMediaInsert**](ivmdvddriveevents-onmediainsert.md) | Receives notification that media has been inserted into the drive.<br/> |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMDVDDriveEvents is defined as c2a7d8e9-e76c-4eb8-94f7-71a5122d249b<br/>         |



 

 





