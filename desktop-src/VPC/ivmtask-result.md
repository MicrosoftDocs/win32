---
title: IVMTask Result property (VPCCOMInterfaces.h)
description: Retrieves the result of the task.
ms.assetid: 640279ef-94b8-4e8f-88f3-a97cec54c121
keywords:
- Result property Virtual PC
- Result property Virtual PC , IVMTask interface
- IVMTask interface Virtual PC , Result property
topic_type:
- apiref
api_name:
- IVMTask.Result
- IVMTask.get_Result
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMTask::Result property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the result of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_Result(
  [out, retval] VMTaskResult *result
);
```



## Property value

The result of the task. For a list of values, see [**VMTaskResult**](vmtaskresult.md).

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter value is **NULL**.<br/>  |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



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

 

