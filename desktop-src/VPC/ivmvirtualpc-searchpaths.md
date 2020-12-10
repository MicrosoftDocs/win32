---
title: IVMVirtualPC SearchPaths property (VPCCOMInterfaces.h)
description: File system paths that are used to find files associated with Windows Virtual PC.
ms.assetid: 2a2deee5-7e6b-4b90-8ce9-0b0dbeef0f30
keywords:
- SearchPaths property Virtual PC
- SearchPaths property Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , SearchPaths property
topic_type:
- apiref
api_name:
- IVMVirtualPC.SearchPaths
- IVMVirtualPC.get_SearchPaths
- IVMVirtualPC.put_SearchPaths
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::SearchPaths property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the file system paths that are used to find files associated with Windows Virtual PC.

This property is read/write.

## Syntax


```C++
HRESULT put_SearchPaths(
  [in]          VARIANT searchPaths
);

HRESULT get_SearchPaths(
  [out, retval] VARIANT *searchPaths
);
```



## Property value

Specifies a safearray containing a file system path for each entry.

## Error codes



| Name/value                                                                                                                                                                               | Meaning                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                               |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL**.<br/>                                                                                                  |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>                                 | The *searchPaths* parameter is not valid and could not be parsed into an array of paths.<br/>                                    |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)</dt> <dt>0x80070002</dt> </dl> | The system cannot find a directory specified in the *searchPaths* parameter.<br/>                                                |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)</dt> <dt>0x80070003</dt> </dl> | The system cannot find a path specified by the *searchPaths* parameter.<br/>                                                     |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)</dt> <dt>0x8007007b</dt> </dl>    | A path specified in the *searchPaths* parameter contains illegal characters. The illegal characters are "\*?<>/\|":".<br/> |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)</dt> <dt>0x800700a1</dt> </dl>    | A path contained in the *searchPaths* parameter specifies an empty or relative path. An absolute path is required.<br/>          |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)</dt> <dt>0x8007006f</dt> </dl> | The path specified in the *searchPaths* parameter is too long. The length of the path must be less than 260 characters.<br/>     |
| <dl> <dt>VM\_E\_PREF\_NOT\_FOUND</dt> <dt>0xA0040300</dt> </dl>                       | The preference was not found.<br/>                                                                                               |
| <dl> <dt>VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                           |



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

 

