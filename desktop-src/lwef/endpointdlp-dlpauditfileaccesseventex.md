---
description: Deprecated - Generates an ETW event for the specified file, and allows a business justification to be provided for that enforcement event.
title: DlpAuditFileAccessEventEx function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpAuditFileAccessEventEx
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpAuditFileAccessEventEx function

> [!NOTE]
> This API is deprecated. Please call [DlpAuditOperationEnforcementEventEx](endpointdlp-dlpauditoperationenforcementeventex.md) instead.

Generates an ETW event for the specified file, and allows a business justification to be provided for that enforcement event.

## Syntax

```C++
HRESULT WINAPI DlpAuditFileAccessEvent(_In_z_ LPCWSTR filePath, _In_z_ LPCWSTR url, DlpEnforcementLevel enforcmentLevel, BOOLEAN userBypass, _In_ DlpTraceInfo* traceInfo,     _In_opt_z_ LPCWSTR businessJustification);
```

## Parameters

`filePath` [in]: A [fully qualified Win32 file path](https://docs.microsoft.com/windows/win32/fileio/naming-a-file) for the file to be analyzed.

`url` [in]: The accessing URL to trace. When investigating some operations like Print or Copy to Keyboard, this property can be NULL.

`enforcementlevel`: The enforcement level of the file specified.

`userbypass`: Indicates the user decision if the `DlpEnforcementLevel` is set to Warn. A value of TRUE indicates that the operation is allowed, a value of FALSE disallows the operation.

`traceInfo` [in]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the `PolicyRuleID` assigned to the file. This value can be NULL.

`businessJustification` [in]: A business justification for the generated enforcement event.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `FAILED` | An unexpected error prevented the function from completing. |



## Remarks

This function can be called from multiple threads.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |