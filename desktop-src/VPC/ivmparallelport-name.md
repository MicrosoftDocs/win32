---
title: IVMParallelPort Name property (VPCCOMInterfaces.h)
description: Name of the parallel port.
ms.assetid: 254df134-2b48-4a81-8229-0f5fbacf2e1c
keywords:
- Name property Virtual PC
- Name property Virtual PC , IVMParallelPort interface
- IVMParallelPort interface Virtual PC , Name property
topic_type:
- apiref
api_name:
- IVMParallelPort.Name
- IVMParallelPort.get_Name
- IVMParallelPort.put_Name
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMParallelPort::Name property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the name of the parallel port.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]          BSTR portName
);

HRESULT get_Name(
  [out, retval] BSTR *portName
);
```



## Property value

Sets the name of the parallel port (for example, "LPT1").

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                              |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>                                 |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>      | The parameter refers to a parallel port that is not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration for this virtual machine is not valid.<br/>   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                          |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMParallelPort is defined as 097beecb-0a02-474f-abd6-298b22293fc6<br/>            |



## See also

<dl> <dt>

[**IVMParallelPort**](ivmparallelport.md)
</dt> </dl>

 

