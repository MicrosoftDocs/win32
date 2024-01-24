---
title: IVMGuestOS GetOsVersionInfo method (VPCCOMInterfaces.h)
description: Retrieves version information for the guest operating system running in the virtual machine.
ms.assetid: 1f9d749f-6007-466d-9df9-71c6a72e8112
keywords:
- GetOsVersionInfo method Virtual PC
- GetOsVersionInfo method Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , GetOsVersionInfo method
topic_type:
- apiref
api_name:
- IVMGuestOS.GetOsVersionInfo
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::GetOsVersionInfo method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves version information for the guest operating system running in the virtual machine (VM).

## Syntax


```C++
HRESULT GetOsVersionInfo(
  [out, retval] GUESTOSVERSIONINFOEX **guestOsVersionInfo
);
```



## Parameters

<dl> <dt>

*guestOsVersionInfo* \[out, retval\]
</dt> <dd>

A pointer to a [**GUESTOSVERSIONINFOEX**](guestosversioninfoex.md) structure.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                       | Description                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                             | The operation was successful.<br/>                                  |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                               | The parameter is **NULL**.<br/>                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_OUTOFMEMORY)**</dt> <dt>0x8007000e</dt> </dl> | There is not enough memory available to complete this request.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                       | An unexpected error has occurred.<br/>                              |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                  | The VM is not running.<br/>                                         |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl>    | Integration components are not installed in this VM.<br/>           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>                 |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

