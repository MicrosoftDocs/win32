---
title: IVMParallelPort _ID method (VPCCOMInterfaces.h)
description: Retrieves the internal identifier of the parallel port.
ms.assetid: a0de74da-0e23-489e-8a89-8deba974e548
keywords:
- _ID method Virtual PC
- _ID method Virtual PC , IVMParallelPort interface
- IVMParallelPort interface Virtual PC , _ID method
topic_type:
- apiref
api_name:
- IVMParallelPort._ID
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMParallelPort::\_ID method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the internal identifier of the parallel port.

## Syntax


```C++
HRESULT _ID(
  [out] long *portID
);
```



## Parameters

<dl> <dt>

*portID* \[out\]
</dt> <dd>

The parallel port identifier.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>                               |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                        |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl> | The configuration for this virtual machine is not valid.<br/> |



 

## Remarks

This property is not usable by scripting languages.

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

 

