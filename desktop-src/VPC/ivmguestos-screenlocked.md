---
title: IVMGuestOS ScreenLocked property (VPCCOMInterfaces.h)
description: Indicates whether the screen in the guest operating system is locked.
ms.assetid: 5ce2e0ad-b98c-4aa7-99b5-0fc85026a121
keywords:
- ScreenLocked property Virtual PC
- ScreenLocked property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , ScreenLocked property
topic_type:
- apiref
api_name:
- IVMGuestOS.ScreenLocked
- IVMGuestOS.get_ScreenLocked
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::ScreenLocked property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Indicates whether the screen in the guest operating system is locked.

This property is read-only.

## Syntax


```C++
HRESULT get_ScreenLocked(
  [out, retval] VARIANT_BOOL *guestScreenLocked
);
```



## Property value

**VARIANT\_TRUE** if screen is locked in guest operating system, **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                    |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                                       |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine (VM) must be running for this operation.<br/>                     |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | The integration components feature is not enabled in the guest operating system.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                |



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

 

