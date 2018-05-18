---
title: Support StopTracingFromManifest method
description: Stops tracing from the manifest.
ms.assetid: '1B327E03-65B2-402B-AFEF-BAE2233FB217'
keywords: ["StopTracingFromManifest method Access Execution Engine", "StopTracingFromManifest method Access Execution Engine , Support interface", "Support interface Access Execution Engine , StopTracingFromManifest method"]
topic_type:
- apiref
api_name:
- Support.StopTracingFromManifest
api_location:
- AxeCore.dll
api_type:
- COM
---

# Support::StopTracingFromManifest method

Stops tracing from the manifest.

## Syntax


```C++
virtual HRESULT StopTracingFromManifest(
  [in] LPCWSTR outputFileName
) = 0;
```



## Parameters

<dl> <dt>

*outputFileName* \[in\]
</dt> <dd>

The name of the trace output file.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





