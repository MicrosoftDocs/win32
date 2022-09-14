---
title: IVMGuestOS IsHeartbeating property (VPCCOMInterfaces.h)
description: Determines whether the virtual machine has a heartbeat.
ms.assetid: b1697a7b-6119-47aa-b261-6009f5287993
keywords:
- IsHeartbeating property Virtual PC
- IsHeartbeating property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , IsHeartbeating property
topic_type:
- apiref
api_name:
- IVMGuestOS.IsHeartbeating
- IVMGuestOS.get_IsHeartbeating
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::IsHeartbeating property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether the virtual machine has a heartbeat.

This property is read-only.

## Syntax


```C++
HRESULT get_IsHeartbeating(
  [out, retval] VARIANT_BOOL *heartBeating
);
```



## Property value

**VARIANT\_TRUE** if a heartbeat is detected, **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                              | Meaning                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                 | The operation was successful.<br/>                                                                                                                         |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                   | The parameter is **NULL**.<br/>                                                                                                                            |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>           | The configuration is unknown.<br/>                                                                                                                         |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>      | The virtual machine must be running for this operation.<br/>                                                                                               |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> <dt>0xA0040504</dt> </dl> | The virtual machine is not fully booted, the integration components feature is not installed, or the installed version does not support this feature.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>           | An unexpected error has occurred.<br/>                                                                                                                     |



## Remarks

When integration components is installed in the guest operating system, a regular 'tick' or heartbeat is sent from the virtual machine session to Windows Virtual PC. If the guest operating system is heavily loaded, it's possible that Virtual PC will receive fewer heartbeats than expected. If no heartbeat is detected, it is possible that the guest operating system is not responding or is crashed.

By default, a virtual machine produces ten heartbeat ticks per minute. If no heartbeat ticks are detected for an entire minute, Windows Virtual PC will attempt to restart the virtual machine session once every ten seconds for up to two minutes. This behavior is controlled by the following key values in the virtual machine session's configuration file.



| Configuration key                                            | Default       | Description                                                                                                                             |
|--------------------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| integration/microsoft/heartbeat/time<br/>              | 60<br/> | The length of the block of time used to generate heartbeat ticks, in in seconds.<br/>                                             |
| integration/microsoft/heartbeat/rate<br/>              | 10<br/> | The number of ticks generated in each heartbeat time block.<br/>                                                                  |
| integration/microsoft/heartbeat/failure\_interval<br/> | 10<br/> | The number of seconds between restart attempts, once no heartbeat ticks are received within a specific heartbeat time block.<br/> |
| integration/microsoft/heartbeat/failure\_attempts<br/> | 12<br/> | The number of restart attempts made.<br/>                                                                                         |



 

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

 

