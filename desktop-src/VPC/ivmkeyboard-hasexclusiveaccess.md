---
title: IVMKeyboard HasExclusiveAccess property (VPCCOMInterfaces.h)
description: Indicates whether this object has exclusive control over the VM's keyboard device.
ms.assetid: edba154e-e700-488c-9133-91649daecef1
keywords:
- HasExclusiveAccess property Virtual PC
- HasExclusiveAccess property Virtual PC , IVMKeyboard interface
- IVMKeyboard interface Virtual PC , HasExclusiveAccess property
topic_type:
- apiref
api_name:
- IVMKeyboard.HasExclusiveAccess
- IVMKeyboard.get_HasExclusiveAccess
- IVMKeyboard.put_HasExclusiveAccess
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMKeyboard::HasExclusiveAccess property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Indicates whether this object has exclusive control over the virtual machine's (VM) keyboard device.

This property is read/write.

## Syntax


```C++
HRESULT put_HasExclusiveAccess(
  [in]          VARIANT_BOOL makeExclusive
);

HRESULT get_HasExclusiveAccess(
  [out, retval] VARIANT_BOOL *isExclusive
);
```



## Property value

**TRUE** if exclusive access to the VM's keyboard device has been acquired, **FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                      | The operation was successful.<br/>                                                                                                                                                                                                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                        | The *isExclusive* parameter is **NULL**.<br/>                                                                                                                                                                                             |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                   | The requested exclusive mode is already set for this device. This can happen when trying to set exclusive mode when it has already been acquired, or when trying to release exclusive mode when it had not been previously acquired.<br/> |
| <dl> <dt>VM\_E\_SET\_EXCLUSIVE\_MODE\_FAIL</dt> <dt>0xA0040825</dt> </dl> | Failed to set or release exclusive mode as requested. This could be because the VM is no longer running, or because another process has already acquired exclusive mode on the VM's keyboard device.<br/>                                 |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>                     | The specified string is empty, or contains an invalid key code.<br/>                                                                                                                                                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                | An unexpected error has occurred.<br/>                                                                                                                                                                                                    |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMKeyboard is defined as 00695f2e-c5ad-4d6e-b1ab-336ed121f8c4<br/>                |



## See also

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> </dl>

 

