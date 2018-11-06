---
title: IVMVirtualMachine HasMMX property
description: Determines whether the processor supports the MMX instruction set.
ms.assetid: 85350abe-ab44-42d2-9f3e-0fbdb64ff854
keywords:
- HasMMX property Virtual PC
- HasMMX property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , HasMMX property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.HasMMX
- IVMVirtualMachine.get_HasMMX
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachine::HasMMX property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Determines whether the processor supports the MMX instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_HasMMX(
  [out, retval] VARIANT_BOOL *mmxEnabled
);
```



## Property value

**TRUE** if the processor supported the MMX instruction set, **FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



|                                     |                                                                                               |
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

 

 





