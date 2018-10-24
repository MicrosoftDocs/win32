---
title: IVMHostInfo ProcessorSpeed property
description: Speed of the host processor, in megahertz (MHz) or gigahertz (GHz).
ms.assetid: 2d5e3f2e-8e81-4527-bd7f-52bf5b1f56ef
keywords:
- ProcessorSpeed property Virtual PC
- ProcessorSpeed property Virtual PC , IVMHostInfo interface
- IVMHostInfo interface Virtual PC , ProcessorSpeed property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorSpeed
- IVMHostInfo.get_ProcessorSpeed
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMHostInfo::ProcessorSpeed property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Retrieves the speed of the host processor, in megahertz (MHz) or gigahertz (GHz).

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorSpeed(
  [out, retval] long *processorSpeed
);
```



## Property value

The processor speed, in megahertz or gigahertz.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHostInfo is defined as 5b5cf343-05ad-453b-be99-adf4e27b2ebc<br/>                |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





