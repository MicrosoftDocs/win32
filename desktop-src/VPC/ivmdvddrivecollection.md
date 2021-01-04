---
title: IVMDVDDriveCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of CD and DVD drives within the virtual machine. To obtain an IVMDVDDriveCollection object, use the IVMVirtualMachine DVDROMDrives property.
ms.assetid: 3069f530-9bc7-4f55-bf5a-82d1244d0cc5
keywords:
- IVMDVDDriveCollection interface Virtual PC
- IVMDVDDriveCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMDVDDriveCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDriveCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of CD and DVD drives within the virtual machine. To obtain an **IVMDVDDriveCollection** object, use the [**IVMVirtualMachine::DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md) property.

## Members

The **IVMDVDDriveCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMDVDDriveCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMDVDDriveCollection** interface has these properties.



| Property                                                       | Access type          | Description                                                                    |
|:---------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmdvddrivecollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                   |
| [**Count**](ivmdvddrivecollection-count.md)<br/>        | Read-only<br/> | The number of CD and DVD drives in this collection.<br/>                 |
| [**Item**](ivmdvddrivecollection-item.md)<br/>          | Read-only<br/> | The CD or DVD drive object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDriveCollection is defined as bc86e297-e55f-4742-9614-ad11d3131f68<br/>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> <dt>

[**IVMVirtualMachine::DVDROMDrives**](ivmvirtualmachine-dvdromdrives.md)
</dt> </dl>

 

