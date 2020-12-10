---
title: IVMTask Error property (VPCCOMInterfaces.h)
description: Retrieves the error recorded for this task.
ms.assetid: 9023e24b-679b-43e4-8db4-b8510a582382
keywords:
- Error property Virtual PC
- Error property Virtual PC , IVMTask interface
- IVMTask interface Virtual PC , Error property
topic_type:
- apiref
api_name:
- IVMTask.Error
- IVMTask.get_Error
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMTask::Error property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the error recorded for this task.

This property is read-only.

## Syntax


```C++
HRESULT get_Error(
  [out, retval] long *outError
);
```



## Property value

The recorded error.

## Error codes

Instances of [**IVMTask**](ivmtask.md) returned by other interfaces may return additional values. For details, see the documentation of the methods that return a **IVMTask** instance.



| Name/value                                                                                                                                                                        | Meaning                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                           | The operation was successful.<br/>                              |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                             | The parameter value is **NULL**.<br/>                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                     | An unexpected error has occurred.<br/>                          |
| <dl> <dt>VM\_E\_VMVIRTUALPC\_OLDER\_VERSION</dt> <dt>0xA0040952</dt> </dl>     | Both Virtual PC 2007 and Windows Virtual PC are installed.<br/> |
| <dl> <dt>VM\_E\_OTHER\_VIRTUALIZATION\_SOFTWARE</dt> <dt>0xA0040953</dt> </dl> | Other virtualization software is installed.<br/>                |



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

 

