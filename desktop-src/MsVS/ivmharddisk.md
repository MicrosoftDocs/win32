---
title: IVMHardDisk interface
description: The IVMHardDisk interface provides access to a hard disk image. It can be accessed through the IVMHardDiskConnection HardDisk property or the IVMVirtualServer GetHardDisk method.
ms.assetid: c7636b79-40ce-4ee0-b5ed-0abe84a4f110
keywords:
- IVMHardDisk interface Virtual Server
- IVMHardDisk interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMHardDisk
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

# IVMHardDisk interface

The **IVMHardDisk** interface provides access to a hard disk image. It can be accessed through the [**IVMHardDiskConnection::HardDisk**](ivmharddiskconnection-harddisk.md) property or the [**IVMVirtualServer::GetHardDisk**](ivmvirtualserver-getharddisk.md) method.

## Members

The **IVMHardDisk** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMHardDisk** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMHardDisk** interface has these methods.



| Method                                 | Description                                                                                                                                             |
|:---------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Compact**](ivmharddisk-compact.md) | Compacts a dynamically expanding hard disk image.<br/>                                                                                            |
| [**Convert**](ivmharddisk-convert.md) | Converts a disk image to either a dynamically expanding disk image or a fixed-size disk image.<br/>                                               |
| [**Merge**](ivmharddisk-merge.md)     | Merges a differencing hard disk image with its parent disk image.<br/>                                                                            |
| [**MergeTo**](ivmharddisk-mergeto.md) | Merges a differencing hard disk image with all of its parents (up to and including the root parent hard disk image) to a new hard disk file.<br/> |



 

### Properties

The **IVMHardDisk** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                                        |
|:--------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**File**](ivmharddisk-file.md)<br/>                               | Read-only<br/> | The full path name of the current hard disk image file.<br/>                                                 |
| [**HostDriveIdentifier**](ivmharddisk-hostdriveidentifier.md)<br/> | Read-only<br/> | A string that identifies the host drive linked to by this virtual hard disk image.<br/>                      |
| [**HostFreeDiskSpace**](ivmharddisk-hostfreediskspace.md)<br/>     | Read-only<br/> | The amount of remaining disk space available on the host computer for the current hard disk image file.<br/> |
| [**Parent**](ivmharddisk-parent.md)<br/>                           | Read-only<br/> | The parent of the current differencing hard disk image.<br/>                                                 |
| [**Security**](ivmharddisk-security.md)<br/>                       | Read-only<br/> | The virtual hard disk's security object.<br/>                                                                |
| [**SizeInGuest**](ivmharddisk-sizeinguest.md)<br/>                 | Read-only<br/> | The size, in bytes, of the hard disk image, as represented in the guest operating system.<br/>               |
| [**SizeOnHost**](ivmharddisk-sizeonhost.md)<br/>                   | Read-only<br/> | The size, in bytes, of the hard disk image file on the host computer.<br/>                                   |
| [**Type**](ivmharddisk-type.md)<br/>                               | Read-only<br/> | The type of the current hard disk image.<br/>                                                                |



 

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

 

 





