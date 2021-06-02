---
title: IVMGuestOS SuiteMask property (VPCCOMInterfaces.h)
description: Retrieves the SuiteMask of the guest operating system running in the virtual machine.
ms.assetid: 11d065c1-9d46-4c81-b843-776db3507a04
keywords:
- SuiteMask property Virtual PC
- SuiteMask property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , SuiteMask property
topic_type:
- apiref
api_name:
- IVMGuestOS.SuiteMask
- IVMGuestOS.get_SuiteMask
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::SuiteMask property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the SuiteMask of the guest operating system running in the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_SuiteMask(
  [out, retval] BSTR *suiteMask
);
```



## Property value

The suite mask. The following string values are supported.



| Value                                                                                   | Meaning                                                                                                                                                                |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>"0x00000004"</dt> </dl> | Microsoft BackOffice components are installed.<br/>                                                                                                              |
| <dl> <dt>"0x00000400"</dt> </dl> | Windows Server 2003, Web Edition is installed.<br/>                                                                                                              |
| <dl> <dt>"0x00004000"</dt> </dl> | Windows Server 2003, Compute Cluster Edition is installed.<br/>                                                                                                  |
| <dl> <dt>"0x00000080"</dt> </dl> | Windows Server 2008 R2 Datacenter, Windows Server 2008 Datacenter, Windows Server 2003, Datacenter Edition, or Windows 2000 Datacenter Server is installed.<br/> |
| <dl> <dt>"0x00000002"</dt> </dl> | Windows Server 2008 R2 Enterprise, Windows Server 2008 Enterprise, Windows Server 2003, Enterprise Edition, or Windows 2000 Advanced Server is installed.<br/>   |
| <dl> <dt>"0x00000040"</dt> </dl> | Windows XP Embedded is installed.<br/>                                                                                                                           |
| <dl> <dt>"0x00000200"</dt> </dl> | Windows Vista Home Premium, Windows Vista Home Basic, or Windows XP Home Edition is installed.<br/>                                                              |
| <dl> <dt>"0x00000100"</dt> </dl> | Remote Desktop is supported, but only one interactive session is supported.<br/>                                                                                 |
| <dl> <dt>"0x00000001"</dt> </dl> | Microsoft Small Business Server was once installed on the system, but may have been upgraded to another version of Windows.<br/>                                 |
| <dl> <dt>"0x00000020"</dt> </dl> | Microsoft Small Business Server is installed with the restrictive client license in force.<br/>                                                                  |
| <dl> <dt>"0x00002000"</dt> </dl> | Windows Storage Server 2003 R2 or Windows Storage Server 2003 is installed.<br/>                                                                                 |
| <dl> <dt>"0x00000010"</dt> </dl> | Remote Desktop Services is installed. This value is always set.<br/>                                                                                             |
| <dl> <dt>"0x00008000"</dt> </dl> | Windows Home Server is installed.<br/>                                                                                                                           |



 

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                           |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The VM is not running.<br/>                               |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | Integration components are not installed in this VM.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                    |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>                 |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

