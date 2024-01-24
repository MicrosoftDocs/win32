---
title: IVMGuestOS MultipleUserSessionsAllowed property
description: Determines whether multiple simultaneous user sessions are allowed in the guest operating system.
ms.assetid: 8a4163bf-b805-4cf0-b785-ee82e8374ef6
keywords:
- MultipleUserSessionsAllowed property Virtual PC
- MultipleUserSessionsAllowed property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , MultipleUserSessionsAllowed property
topic_type:
- apiref
api_name:
- IVMGuestOS.MultipleUserSessionsAllowed
- IVMGuestOS.get_MultipleUserSessionsAllowed
api_location:
- IVMGuestOS.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::MultipleUserSessionsAllowed property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether multiple simultaneous user sessions are allowed in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_MultipleUserSessionsAllowed(
  [out, retval] VARIANT_BOOL *sessionStatus
);
```



## Property value

**VARIANT\_TRUE** if multiple simultaneous user sessions are allowed in the guest operating system, **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                                                       |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                       | Remote Desktop Services (formerly known as Terminal Services) is not yet initialized in the guest operating system.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The *sessionStatus* parameter is **NULL**.<br/>                                                                          |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine is not running.<br/>                                                                                 |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | Integration components are not installed in this virtual machine.<br/>                                                   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                                                   |



## Remarks

The value of this property is not valid unless the [**TerminalServicesInitialized**](ivmguestos-terminalservicesinitialized.md) property is **VARIANT\_TRUE**.

For Windows client operating systems, **MultipleUserSessionsAllowed** is **VARIANT\_TRUE** if Fast User Switching is supported. For Windows Server operating systems, **MultipleUserSessionsAllowed** is **VARIANT\_TRUE** if Remote Desktop Services (formerly called Terminal Services) is installed and enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| End of client support<br/>    | Windows 7<br/>                                                                      |
| IDL<br/>                      | <dl> <dt>IVMGuestOS.idl</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>             |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

