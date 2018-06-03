---
title: Support StartTracingFromManifest method
description: Starts tracing from the manifest.
ms.assetid: A171D456-4465-4928-964F-8628BED6CFAA
keywords:
- StartTracingFromManifest method Access Execution Engine
- StartTracingFromManifest method Access Execution Engine , Support interface
- Support interface Access Execution Engine , StartTracingFromManifest method
topic_type:
- apiref
api_name:
- Support.StartTracingFromManifest
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support::StartTracingFromManifest method

Starts tracing from the manifest.

## Syntax


```C++
virtual HRESULT StartTracingFromManifest(
  [in]           LPCWSTR profileName,
  [in, optional] LPCWSTR traceTitle,
  [in, optional] LPCWSTR traceDescription
) = 0;
```



## Parameters

<dl> <dt>

*profileName* \[in\]
</dt> <dd>

The name of the profile.

</dd> <dt>

*traceTitle* \[in, optional\]
</dt> <dd>

The title for the trace.

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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





