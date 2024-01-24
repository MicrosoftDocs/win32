---
title: IVMDVDDrive Attachment property (VPCCOMInterfaces.h)
description: Retrieves the type of media attached to the DVD drive within the virtual machine.
ms.assetid: 7ae1714d-e5e9-4f6a-85a6-c0b3c4d21820
keywords:
- Attachment property Virtual PC
- Attachment property Virtual PC , IVMDVDDrive interface
- IVMDVDDrive interface Virtual PC , Attachment property
topic_type:
- apiref
api_name:
- IVMDVDDrive.Attachment
- IVMDVDDrive.get_Attachment
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive::Attachment property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the type of media attached to the DVD drive within the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Attachment(
  [out, retval] VMDVDDriveAttachmentType *driveAttachment
);
```



## Property value

The attached media type. For a list of values, see [**VMDVDDriveAttachmentType**](vmdvddriveattachmenttype.md).

## Error codes



| Name/value                                                                                                                                                       | Meaning                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                          | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>            | The parameter is **NULL**.<br/>                  |
| <dl> <dt>E\_FAIL</dt> <dt>0x80004005</dt> </dl>               | An unexpected error has occurred.<br/>           |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>    | The virtual machine could not be found.<br/>     |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> <dt>0xA0040502</dt> </dl> | The bus location for this drive is invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>    | An unexpected error has occurred.<br/>           |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDrive is defined as b96328f6-6732-437d-a00d-ffa47e43971c<br/>                |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

