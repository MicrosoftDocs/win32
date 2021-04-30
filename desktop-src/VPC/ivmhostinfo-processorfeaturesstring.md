---
title: IVMHostInfo ProcessorFeaturesString property (VPCCOMInterfaces.h)
description: Retrieves the list features supported by the host processor.
ms.assetid: 036c6376-0e9b-46fa-90f4-a40c71c5cf23
keywords:
- ProcessorFeaturesString property Virtual PC
- ProcessorFeaturesString property Virtual PC , IVMHostInfo interface
- IVMHostInfo interface Virtual PC , ProcessorFeaturesString property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorFeaturesString
- IVMHostInfo.get_ProcessorFeaturesString
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHostInfo::ProcessorFeaturesString property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the list features supported by the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorFeaturesString(
  [out, retval] BSTR *featuresString
);
```



## Property value

A comma-delimited list of features. An example would be "MMX,SSE,SSE2,x86-64".



| Value                                                                                 | Meaning                                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>"AMD-V"</dt> </dl>    | Supports the AMD Virtualization extensions.<br/>              |
| <dl> <dt>"Intel VT"</dt> </dl> | Supports the Intel Virtualization Technology extensions.<br/> |
| <dl> <dt>"HAVD"</dt> </dl>     | Hardware Assisted Virtualization is disabled.<br/>            |
| <dl> <dt>"HAVE"</dt> </dl>     | Hardware Assisted Virtualization is enabled.<br/>             |
| <dl> <dt>"MMX"</dt> </dl>      | Supports the MMX extensions.<br/>                             |
| <dl> <dt>"SSE"</dt> </dl>      | Supports the Streaming SIMD Extensions.<br/>                  |
| <dl> <dt>"SSE2"</dt> </dl>     | Supports the Streaming SIMD Extensions 2.<br/>                |
| <dl> <dt>"SSE3"</dt> </dl>     | Supports the Streaming SIMD Extensions 3.<br/>                |
| <dl> <dt>"TXTE"</dt> </dl>     | Supports the Trusted Execution Technology extensions.<br/>    |
| <dl> <dt>"x86-64"</dt> </dl>   | Supports x86-64 extensions.<br/>                              |



 

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

 

