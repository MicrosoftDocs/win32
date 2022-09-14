---
title: IVMGuestOS IntegrationComponentsVersion property (VPCCOMInterfaces.h)
description: Retrieves the version of the Integration Components installed in the guest operating system.
ms.assetid: 4baccb7d-5a3e-460f-9669-ee8dbaec91a9
keywords:
- IntegrationComponentsVersion property Virtual PC
- IntegrationComponentsVersion property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , IntegrationComponentsVersion property
topic_type:
- apiref
api_name:
- IVMGuestOS.IntegrationComponentsVersion
- IVMGuestOS.get_IntegrationComponentsVersion
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::IntegrationComponentsVersion property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the version of the Integration Components installed in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_IntegrationComponentsVersion(
  [out, retval] BSTR *ICVersion
);
```



## Property value

The version.

## Error codes



| Name/value                                                                                                                                                              | Meaning                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                 | The operation was successful.<br/>                                                     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                   | The parameter is **NULL**.<br/>                                                        |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>           | The virtual machine (VM) could not be found.<br/>                                      |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> <dt>0xA0040504</dt> </dl> | Integration Components are not installed in this VM, or the VM was never started.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>           | An unexpected error has occurred.<br/>                                                 |



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

 

