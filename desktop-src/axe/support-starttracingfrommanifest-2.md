---
title: Support StartTracingFromManifest method
description: Starts tracing from the manifest.
ms.assetid: '359F7137-5F6D-4D30-9ADC-0DDA3FE23B1F'
keywords: ["StartTracingFromManifest method Access Execution Engine", "StartTracingFromManifest method Access Execution Engine , Support interface", "Support interface Access Execution Engine , StartTracingFromManifest method"]
topic_type:
- apiref
api_name:
- Support.StartTracingFromManifest
api_location:
- AxeCore.dll
api_type:
- COM
---

# Support::StartTracingFromManifest method

Starts tracing from the manifest.

## Syntax


```C++
virtual HRESULT StartTracingFromManifest(
  [in]           const GUID    *guidAssessment,
  [in]                 LPCWSTR profileName,
  [in, optional]       LPCWSTR traceTitle,
  [in, optional]       LPCWSTR traceDescription
) = 0;
```



## Parameters

<dl> <dt>

*guidAssessment* \[in\]
</dt> <dd>

The description of the trace.

</dd> <dt>

*profileName* \[in\]
</dt> <dd>

The name of the profile.

</dd> <dt>

*traceTitle* \[in, optional\]
</dt> <dd>

Title for the trace.

</dd> <dt>

*traceDescription* \[in, optional\]
</dt> <dd>

The description of the trace.

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

 

 





