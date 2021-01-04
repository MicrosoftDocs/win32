---
title: IVMGuestOS CanShutdown property (VPCCOMInterfaces.h)
description: Indicates whether the guest operating system can be cleanly shut down.
ms.assetid: 239cba43-9494-4efd-a4c8-0bb47f476b81
keywords:
- CanShutdown property Virtual PC
- CanShutdown property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , CanShutdown property
topic_type:
- apiref
api_name:
- IVMGuestOS.CanShutdown
- IVMGuestOS.get_CanShutdown
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::CanShutdown property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Indicates whether the guest operating system can be cleanly shut down (requires Integration Components).

This property is read-only.

## Syntax


```C++
HRESULT get_CanShutdown(
  [out, retval] VARIANT_BOOL *canShutdown
);
```



## Property value

**VARIANT\_TRUE** if the operating system supports the shutdown operation and **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>           |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                    | The virtual machine is not turned on.<br/>   |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>              |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The virtual machine could not be found.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>       |



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

 

