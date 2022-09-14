---
title: IVMGuestOS InstallIntegrationComponents method (VPCCOMInterfaces.h)
description: Locates and installs the latest Integration Components into the guest operating system.
ms.assetid: 06f302b3-ec2b-471a-8e2e-095ed6ecbd3d
keywords:
- InstallIntegrationComponents method Virtual PC
- InstallIntegrationComponents method Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , InstallIntegrationComponents method
topic_type:
- apiref
api_name:
- IVMGuestOS.InstallIntegrationComponents
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::InstallIntegrationComponents method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Locates and installs the latest Integration Components into the guest operating system.

## Syntax


```C++
HRESULT InstallIntegrationComponents();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                               |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                       | The virtual machine must be running for this operation.<br/>                     |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                            | The virtual machine could not be found.<br/>                                     |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl>                         | The virtual machine does not have an empty DVD drive.<br/>                       |
| <dl> <dt>**VM\_E\_MEDIA\_UNMOUNT\_FAIL**</dt> <dt>0xA0040508</dt> </dl>                   | The attempt to unmount the media from the virtual machine DVD drive failed.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                           |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)**</dt> <dt>0x80070002</dt> </dl> | The system cannot find the ISO file for the Integration Components.<br/>         |



 

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

 

