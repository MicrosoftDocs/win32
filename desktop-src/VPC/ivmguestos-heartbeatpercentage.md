---
title: IVMGuestOS HeartbeatPercentage property (VPCCOMInterfaces.h)
description: Percentage of expected heartbeats received over the past minute.
ms.assetid: 456dd8ae-e946-429d-98aa-5773362fdd4e
keywords:
- HeartbeatPercentage property Virtual PC
- HeartbeatPercentage property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , HeartbeatPercentage property
topic_type:
- apiref
api_name:
- IVMGuestOS.HeartbeatPercentage
- IVMGuestOS.get_HeartbeatPercentage
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::HeartbeatPercentage property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the percentage of expected heartbeats received over the past minute.

This property is read-only.

## Syntax


```C++
HRESULT get_HeartbeatPercentage(
  [out, retval] long *heartbeatPercentage
);
```



## Property value

The percentage of expected heartbeats received over the past minute.

## Error codes



| Name/value                                                                                                                                                              | Meaning                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                 | The operation was successful.<br/>                                                                                                            |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                   | The parameter is **NULL**.<br/>                                                                                                               |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>           | The configuration is unknown.<br/>                                                                                                            |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>      | The virtual machine (VM) must be running for this operation.<br/>                                                                             |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> <dt>0xA0040504</dt> </dl> | The VM is not fully booted, the integration components feature is not installed, or the installed version does not support this feature.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>           | An unexpected error has occurred.<br/>                                                                                                        |



## Remarks

Integration components will send a periodic heartbeat to Windows Virtual PC while the guest operating system is running. If the guest operating system is heavily loaded, it's possible that Windows Virtual PC will receive fewer heartbeats than expected. If the heartbeat percentage drops to zero, it is possible that the guest operating system is not responding or is crashed. The virtual machine must be running (that is, fully booted and not shutting down) and integration components must be installed when this property is invoked.

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

 

