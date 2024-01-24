---
title: IVMVirtualPC Version property (VPCCOMInterfaces.h)
description: Retrieves the version of this instance of Windows Virtual PC.
ms.assetid: efcd5e71-8752-45a2-8138-4bc214762f39
keywords:
- Version property Virtual PC
- Version property Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , Version property
topic_type:
- apiref
api_name:
- IVMVirtualPC.Version
- IVMVirtualPC.get_Version
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::Version property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the version of this instance of Windows Virtual PC.

This property is read-only.

## Syntax


```C++
HRESULT get_Version(
  [out, retval] BSTR *version
);
```



## Property value

The version.

## Error codes



| Name/value                                                                                                                                                                           | Meaning                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                | The parameter is **NULL**.<br/>                                                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



## Remarks

The Windows Virtual PC version information is returned as a string value with the following format: "*v*.*s*.*bbb*.*tee*", where *v* is the major version number, *s* is the minor version number, *bbb* is the build number, *t* is the build type (0 = release build), and *ee* is the server edition (SE = Standard Edition, EE = Enterprise Edition).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

