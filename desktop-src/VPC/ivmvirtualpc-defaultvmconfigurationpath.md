---
title: IVMVirtualPC DefaultVMConfigurationPath property (VPCCOMInterfaces.h)
description: Default directory to be searched for available virtual machine configuration files.
ms.assetid: 9ae63198-e3f6-4dcb-8edb-85adfbbdca26
keywords:
- DefaultVMConfigurationPath property Virtual PC
- DefaultVMConfigurationPath property Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , DefaultVMConfigurationPath property
topic_type:
- apiref
api_name:
- IVMVirtualPC.DefaultVMConfigurationPath
- IVMVirtualPC.get_DefaultVMConfigurationPath
- IVMVirtualPC.put_DefaultVMConfigurationPath
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::DefaultVMConfigurationPath property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the default directory to be searched for available virtual machine configuration files.

This property is read/write.

## Syntax


```C++
HRESULT put_DefaultVMConfigurationPath(
  [in]          BSTR configurationPath
);

HRESULT get_DefaultVMConfigurationPath(
  [out, retval] BSTR *configurationPath
);
```



## Property value

Specifies the directory path for the default virtual machine configuration files. In the path string, a backslash (\) may appear immediately before the terminating null character.

## Error codes



| Name/value                                                                                                                                                                               | Meaning                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                                 |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                    | The *configurationPath* parameter is **NULL**.<br/>                                                                                                |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)</dt> <dt>0x80070002</dt> </dl> | The system cannot find the directory specified by the *configurationPath* parameter.<br/>                                                          |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *configurationPath* parameter.<br/>                                                               |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)</dt> <dt>0x8007007b</dt> </dl>    | The *configurationPath* parameter contains an invalid character (one of the following: "\*?<>/\|":").<br/>                                   |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)</dt> <dt>0x800700a1</dt> </dl>    | The *configurationPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                          |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *configurationPath* parameter is too long. The length of the path must be less than **MAX\_PATH** (260) characters.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                                             |
| <dl> <dt>VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                                          |



## Remarks

By default, this property value is set to the following directory: "%LocalAppData%\\Microsoft\\Windows Virtual PC\\Virtual Machines\\".

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

 

