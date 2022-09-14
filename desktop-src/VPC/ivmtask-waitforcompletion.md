---
title: IVMTask WaitForCompletion method (VPCCOMInterfaces.h)
description: Waits for the task to complete or for the specified time-out interval to elapse.
ms.assetid: 28718c54-4411-4c69-89de-35ea6a8d074c
keywords:
- WaitForCompletion method Virtual PC
- WaitForCompletion method Virtual PC , IVMTask interface
- IVMTask interface Virtual PC , WaitForCompletion method
topic_type:
- apiref
api_name:
- IVMTask.WaitForCompletion
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMTask::WaitForCompletion method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Waits for the task to complete or for the specified time-out interval to elapse.

## Syntax


```C++
HRESULT WaitForCompletion(
  [in] long timeout
);
```



## Parameters

<dl> <dt>

*timeout* \[in\]
</dt> <dd>

The time, in milliseconds, that this method will wait for task completion before returning control to the caller. A value of -1 specifies that method will wait until the task completes without timing out. Other valid timeout values range from 0 to 4,000,000 milliseconds.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The *timeout* parameter is not valid.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>     |



 

## Remarks

The **WaitForCompletion** method puts the current execution thread to sleep until it returns. Specifying an infinite wait (timeout = -1) is not recommended unless it is absolutely critical that the task completes under any circumstance.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMTask is defined as ab72b222-6e9c-48ae-aa54-85e3e635767c<br/>                    |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

