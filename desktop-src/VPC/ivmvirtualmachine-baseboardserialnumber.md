---
title: IVMVirtualMachine BaseBoardSerialNumber property (VPCCOMInterfaces.h)
description: Base board serial number.
ms.assetid: 374ad471-e0de-4e55-bab6-f7ddf3e5797f
keywords:
- BaseBoardSerialNumber property Virtual PC
- BaseBoardSerialNumber property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , BaseBoardSerialNumber property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.BaseBoardSerialNumber
- IVMVirtualMachine.get_BaseBoardSerialNumber
- IVMVirtualMachine.put_BaseBoardSerialNumber
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::BaseBoardSerialNumber property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the base board serial number.

This property is read/write.

## Syntax


```C++
HRESULT put_BaseBoardSerialNumber(
  [in]          BSTR baseBoardSerialNumber
);

HRESULT get_BaseBoardSerialNumber(
  [out, retval] BSTR *baseBoardSerialNumber
);
```



## Property value

Specifies the base board serial number.

## Error codes



| Name/value                                                                                                                                                               | Meaning                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                  | The operation was successful.<br/>                                               |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                    | The parameter is **NULL**.<br/>                                                  |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>                 | The parameter is greater than 32 characters, an empty string, or not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>            | The configuration is unknown.<br/>                                               |
| <dl> <dt>VM\_E\_VM\_RUNNING\_OR\_SAVED</dt> <dt>0xA004020B</dt> </dl> | The virtual machine is in a running or saved state.<br/>                         |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>            | An unexpected error has occurred.<br/>                                           |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

