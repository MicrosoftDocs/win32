---
description: Notifies the system of the desired enforcement modes for a set of endpoint Data Loss Prevention (DLP) operations.
title: DlpInitializeEnforcementMode function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpInitializeEnforcementMode
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpInitializeEnforcementMode function

Notifies the system of the desired enforcement modes for a set of endpoint Data Loss Prevention (DLP) operations.

## Syntax


```C++
HRESULT WINAPI DlpInitializeEnforcementMode(_In_ DWORD Count, _In_reads_(Count) PDLP_APP_OP_ENLIGHTENED_LEVEL OperationEnforcement);
```



## Parameters

<dl> <dt>

*Count* \[in\]
</dt> <dd>

A **DWORD** specifying the number of operations included in the *OperationEnforcement* array.

</dd> </dl>

<dl> <dt>

*OperationEnforcement* \[in\]
</dt> <dd>

An array of [PDLP_APP_OP_ENLIGHTENED_LEVEL](endpointdlp-dlp_app_op_enlightened_level.md) structures that specify the enforcement level for an endpoint DLP operation.

</dd> </dl>


## Return value

Returns an HRESULT including, but not limited to, the following values.

| HRESULT | Description |
|---------|-------------|
| S_OK | The function completed successfully |
| E_INVALIDARG | One or more of the function parameters are invalid. |
| E_OUTOFMEMORY | Memory allocation for the operation failed. |



## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |