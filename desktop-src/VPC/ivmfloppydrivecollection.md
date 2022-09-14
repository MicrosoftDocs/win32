---
title: IVMFloppyDriveCollection interface (VPCCOMInterfaces.h)
description: Defines a collection of floppy drives within the virtual machine.
ms.assetid: ba05fa84-81c3-4e70-98f5-404a9bc517ad
keywords:
- IVMFloppyDriveCollection interface Virtual PC
- IVMFloppyDriveCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMFloppyDriveCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDriveCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines a collection of floppy drives within the virtual machine. To obtain an **IVMFloppyDriveCollection** object, use the [**IVMVirtualMachine::FloppyDrives**](ivmvirtualmachine-floppydrives.md) property.

## Members

The **IVMFloppyDriveCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMFloppyDriveCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMFloppyDriveCollection** interface has these properties.



| Property                                                          | Access type          | Description                                                                 |
|:------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**\_NewEnum**](ivmfloppydrivecollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                |
| [**Count**](ivmfloppydrivecollection-count.md)<br/>        | Read-only<br/> | The number of floppy drives in this collection.<br/>                  |
| [**Item**](ivmfloppydrivecollection-item.md)<br/>          | Read-only<br/> | The floppy drive object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDriveCollection is defined as 8ba70a25-f698-4ee5-85ce-3cc93a925516<br/>   |



## See also

<dl> <dt>

[**IVMFloppyDrive**](ivmfloppydrive.md)
</dt> <dt>

[**IVMVirtualMachine::FloppyDrives**](ivmvirtualmachine-floppydrives.md)
</dt> </dl>

 

