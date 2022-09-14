---
title: IVMGuestOS TerminalServicesInitialized property (VPCCOMInterfaces.h)
description: Status of Remote Desktop Services in the guest operating system.
ms.assetid: 104d9256-6b2e-45ec-a290-21e0732c65ac
keywords:
- TerminalServicesInitialized property Virtual PC
- TerminalServicesInitialized property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , TerminalServicesInitialized property
topic_type:
- apiref
api_name:
- IVMGuestOS.TerminalServicesInitialized
- IVMGuestOS.get_TerminalServicesInitialized
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::TerminalServicesInitialized property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the status of Remote Desktop Services (formerly known as Terminal Services) in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_TerminalServicesInitialized(
  [out, retval] VARIANT_BOOL *termServStatus
);
```



## Property value

The initialization status.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful and Remote Desktop Services has been initialized. The returned property value indicates whether Remote Desktop Services is available in the guest operating system.<br/> |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                       | The integration components feature is running, but Remote Desktop Services is not yet initialized.<br/>                                                                                               |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                                                                                                                                                       |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine (VM) must be running for this operation.<br/>                                                                                                                                     |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | The integration components feature is not running in the guest operating system.<br/>                                                                                                                 |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                                                                                                                                |



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

 

