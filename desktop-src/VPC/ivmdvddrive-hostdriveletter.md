---
title: IVMDVDDrive HostDriveLetter property (VPCCOMInterfaces.h)
description: The letter of the host drive set for this device.
ms.assetid: e17f707f-e1cf-4302-a69e-caa5829df1af
keywords:
- HostDriveLetter property Virtual PC
- HostDriveLetter property Virtual PC , IVMDVDDrive interface
- IVMDVDDrive interface Virtual PC , HostDriveLetter property
topic_type:
- apiref
api_name:
- IVMDVDDrive.HostDriveLetter
- IVMDVDDrive.get_HostDriveLetter
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive::HostDriveLetter property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the letter of the host drive set for this device.

This property is read-only.

## Syntax


```C++
HRESULT get_HostDriveLetter(
  [out, retval] BSTR *driveLetter
);
```



## Property value

The drive letter.

## Error codes



| Name/value                                                                                                                                                            | Meaning                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                               | The operation was successful.<br/>                             |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                 | The parameter is **NULL**.<br/>                                |
| <dl> <dt>E\_FAIL</dt> <dt>0x80004005</dt> </dl>                    | An unexpected error has occurred.<br/>                         |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>         | The virtual machine could not be found.<br/>                   |
| <dl> <dt>VM\_E\_MEDIA\_WRONG\_TYPE</dt> <dt>0xA00400728</dt> </dl> | The media captured by this DVD drive is not a host drive.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>         | An unexpected error has occurred.<br/>                         |



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

 

