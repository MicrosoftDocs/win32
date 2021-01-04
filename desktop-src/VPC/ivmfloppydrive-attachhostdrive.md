---
title: IVMFloppyDrive AttachHostDrive method (VPCCOMInterfaces.h)
description: Attaches a physical drive on the host to the floppy drive in the virtual machine.
ms.assetid: 9be84e06-e38a-419a-be50-dddd0cc6d2dd
keywords:
- AttachHostDrive method Virtual PC
- AttachHostDrive method Virtual PC , IVMFloppyDrive interface
- IVMFloppyDrive interface Virtual PC , AttachHostDrive method
topic_type:
- apiref
api_name:
- IVMFloppyDrive.AttachHostDrive
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDrive::AttachHostDrive method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches a physical drive on the host to the floppy drive in the virtual machine.

## Syntax


```C++
HRESULT AttachHostDrive(
  [in] BSTR driveLetter
);
```



## Parameters

<dl> <dt>

*driveLetter* \[in\]
</dt> <dd>

The drive letter of the physical floppy drive on the host machine to is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The *driveLetter* parameter is **NULL**, is not a valid floppy drive, or the given path is empty.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl> | The configuration for this virtual machine is not valid or cannot be found.<br/>                       |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                                 |



 

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

 

