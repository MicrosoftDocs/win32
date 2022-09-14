---
title: IVMGuestOS Logoff method (VPCCOMInterfaces.h)
description: Logs off all users from the guest operating system.
ms.assetid: 224aa7cb-0892-4e8a-84bd-78dd5cb724df
keywords:
- Logoff method Virtual PC
- Logoff method Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , Logoff method
topic_type:
- apiref
api_name:
- IVMGuestOS.Logoff
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::Logoff method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Logs off all users from the guest operating system.

## Syntax


```C++
HRESULT Logoff(
  [out, retval] IVMTask **outLogoffTask
);
```



## Parameters

<dl> <dt>

*outLogoffTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion progress of the logoff sequence.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                          | Description                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                | The operation was successful.<br/>                                                |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                          | An unexpected error has occurred.<br/>                                            |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                  | The parameter is **NULL**.<br/>                                                   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED)**</dt> <dt>0x80070005</dt> </dl> | The caller must have execute access permissions for this VM.<br/>                 |
| <dl> <dt>**VM\_E\_TIMED\_OUT**</dt> <dt>0xA0040202</dt> </dl>                           | The operation did not complete in a timely manner.<br/>                           |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl>       | The integration components feature is not installed in this virtual machine.<br/> |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                     | The virtual machine (VM) must be running for this operation.<br/>                 |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                          | The configuration is unknown.<br/>                                                |



 

## Remarks

`HRESULT_FROM_WIN32(ERROR_NO_SUCH_LOGON_SESSION)` (0x80070520) is returned through the [**Error**](ivmtask-error.md) property of the returned [**IVMTask**](ivmtask.md) object there are no logon sessions in the guest operating system.

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

 

