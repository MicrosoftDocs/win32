---
title: IVMFloppyDrive ReleaseHostDrive method (VPCCOMInterfaces.h)
description: Releases a physical drive on the host from the floppy drive.
ms.assetid: 6d5a8e7c-684c-42bc-84e5-76d3e761b7f0
keywords:
- ReleaseHostDrive method Virtual PC
- ReleaseHostDrive method Virtual PC , IVMFloppyDrive interface
- IVMFloppyDrive interface Virtual PC , ReleaseHostDrive method
topic_type:
- apiref
api_name:
- IVMFloppyDrive.ReleaseHostDrive
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDrive::ReleaseHostDrive method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Releases a physical drive on the host from the floppy drive.

## Syntax


```C++
HRESULT ReleaseHostDrive();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                          | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                | The operation was successful.<br/>                                               |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>          | The configuration for this virtual machine is not valid or cannot be found.<br/> |
| <dl> <dt>**VM\_E\_MEDIA\_WRONG\_TYPE**</dt> <dt>0xA00400728</dt> </dl>  | The media attached to this floppy drive is not a physical floppy drive.<br/>     |
| <dl> <dt>**VM\_E\_NO\_MEDIA\_CAPTURED**</dt> <dt>0xA00400652</dt> </dl> | There is no media attached to this floppy drive.<br/>                            |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>          | An unexpected error has occurred.<br/>                                           |



 

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

 

