---
title: IVMAccountant NetworkBytesReceived property (VPCCOMInterfaces.h)
description: Total number of bytes received by all virtual network adapters for this virtual machine.
ms.assetid: 6f6b32e6-d99b-405c-a788-ed646b3a7593
keywords:
- NetworkBytesReceived property Virtual PC
- NetworkBytesReceived property Virtual PC , IVMAccountant interface
- IVMAccountant interface Virtual PC , NetworkBytesReceived property
topic_type:
- apiref
api_name:
- IVMAccountant.NetworkBytesReceived
- IVMAccountant.get_NetworkBytesReceived
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMAccountant::NetworkBytesReceived property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the total number of bytes received by all virtual network adapters for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkBytesReceived(
  [out, retval] VARIANT *bytesReceived
);
```



## Property value

The total number of bytes received. This data is returned as a **VARIANT** of type **VT\_DECIMAL**.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>          |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                    | The virtual machine is not running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>   |



## Remarks

Note that network I/O statistics are reset to zero when a virtual machine is powered up, reset, or restored from saved state.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMAccountant is defined as 6376c067-7f57-4d63-b754-06e2e4f51d73<br/>              |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

