---
title: IVMHardDisk interface (VPCCOMInterfaces.h)
description: Provides access to a hard disk image. It can be accessed through the IVMHardDiskConnection HardDisk property or the IVMVirtualPC GetHardDisk method.
ms.assetid: 0c536906-91be-428a-8199-c452abef423d
keywords:
- IVMHardDisk interface Virtual PC
- IVMHardDisk interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMHardDisk
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Provides access to a hard disk image. It can be accessed through the [**IVMHardDiskConnection::HardDisk**](ivmharddiskconnection-harddisk.md) property or the [**IVMVirtualPC::GetHardDisk**](ivmvirtualpc-getharddisk.md) method.

## Members

The **IVMHardDisk** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMHardDisk** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMHardDisk** interface has these methods.



| Method                                 | Description                                                                                                                                                 |
|:---------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Compact**](ivmharddisk-compact.md) | Compacts a dynamically expanding virtual hard disk image.<br/>                                                                                        |
| [**Convert**](ivmharddisk-convert.md) | Converts any virtual hard disk to either a dynamically expanding virtual hard disk or a fixed-size virtual hard disk.<br/>                            |
| [**Merge**](ivmharddisk-merge.md)     | Merges a differencing virtual hard disk with its parent disk image.<br/>                                                                              |
| [**MergeTo**](ivmharddisk-mergeto.md) | Merges a differencing virtual hard disk with all of its parents (up to and including the root parent virtual hard disk) to a new hard disk file.<br/> |



 

### Properties

The **IVMHardDisk** interface has these properties.



| Property                                                              | Access type           | Description                                                                                    |
|:----------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------|
| [**File**](ivmharddisk-file.md)<br/>                           | Read-only<br/>  | The full path name of the virtual hard disk file.<br/>                                   |
| [**HostFreeDiskSpace**](ivmharddisk-hostfreediskspace.md)<br/> | Read-only<br/>  | The amount of remaining disk space available on the host for the virtual hard disk.<br/> |
| [**Parent**](ivmharddisk-parent.md)<br/>                       | Read/write<br/> | The parent of the differencing virtual hard disk.<br/>                                   |
| [**SizeInGuest**](ivmharddisk-sizeinguest.md)<br/>             | Read-only<br/>  | The size of the virtual hard disk in the guest operating system.<br/>                    |
| [**SizeOnHost**](ivmharddisk-sizeonhost.md)<br/>               | Read-only<br/>  | The size of the virtual hard disk file on the host computer.<br/>                        |
| [**Type**](ivmharddisk-type.md)<br/>                           | Read-only<br/>  | The type of the virtual hard disk.<br/>                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHardDisk is defined as ffa14ae6-48f5-42a4-8a22-186f2e5c7db0<br/>                |



 

