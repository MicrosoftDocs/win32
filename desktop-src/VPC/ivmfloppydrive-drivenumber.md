---
title: IVMFloppyDrive DriveNumber property (VPCCOMInterfaces.h)
description: Retrieves the zero-based index of the controller to which the floppy drive is attached.
ms.assetid: 79a40cad-d280-4c67-9214-0532569e47e4
keywords:
- DriveNumber property Virtual PC
- DriveNumber property Virtual PC , IVMFloppyDrive interface
- IVMFloppyDrive interface Virtual PC , DriveNumber property
topic_type:
- apiref
api_name:
- IVMFloppyDrive.DriveNumber
- IVMFloppyDrive.get_DriveNumber
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDrive::DriveNumber property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the zero-based index of the controller to which the floppy drive is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_DriveNumber(
  [out, retval] long *driveNumber
);
```



## Property value

The zero-based index of the controller.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDrive is defined as 661abee6-112a-4ed9-babf-3c874969f10e<br/>             |



## See also

<dl> <dt>

[**IVMFloppyDrive**](ivmfloppydrive.md)
</dt> </dl>

 

