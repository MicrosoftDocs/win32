---
title: IVMHostInfo OSVersionString property (VPCCOMInterfaces.h)
description: Retrieves the operating system version running on the host machine.
ms.assetid: ac3a162a-d3e6-420d-ac26-d77f1c9646a6
keywords:
- OSVersionString property Virtual PC
- OSVersionString property Virtual PC , IVMHostInfo interface
- IVMHostInfo interface Virtual PC , OSVersionString property
topic_type:
- apiref
api_name:
- IVMHostInfo.OSVersionString
- IVMHostInfo.get_OSVersionString
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHostInfo::OSVersionString property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the operating system version running on the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_OSVersionString(
  [out, retval] BSTR *OSVersion
);
```



## Property value

The operating system version.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



| Requirement | Value |
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

 

