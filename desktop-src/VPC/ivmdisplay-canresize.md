---
title: IVMDisplay CanResize property (VPCCOMInterfaces.h)
description: Determines whether the Guest allows resolution changes.
ms.assetid: 97f2aad9-aa27-4db2-ac5d-fa9645f0e674
keywords:
- CanResize property Virtual PC
- CanResize property Virtual PC , IVMDisplay interface
- IVMDisplay interface Virtual PC , CanResize property
topic_type:
- apiref
api_name:
- IVMDisplay.CanResize
- IVMDisplay.get_CanResize
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDisplay::CanResize property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether the Guest allows resolution changes.

This property is read-only.

## Syntax


```C++
HRESULT get_CanResize(
  [out, retval] VARIANT_BOOL *canResize
);
```



## Property value

**VARIANT\_TRUE** if the Guest allows resolution changes and **VARIANT\_FALSE** otherwise.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                                                                              |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                                                                                                 |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>                    | The configuration is unknown.<br/>                                                                                                              |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine must be running for this operation.<br/>                                                                                    |
| <dl> <dt>VM\_E\_NO\_DISPLAY</dt> <dt>0xA0040850</dt> </dl>                    | There was no video device found for the virtual machine.<br/>                                                                                   |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | The integration components feature is not available; either the integration components are not installed or the feature has been disabled.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                                                                          |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDisplay is defined as 960895e9-f743-4498-96aa-261f867e7fc5<br/>                 |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

