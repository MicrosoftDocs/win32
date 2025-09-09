---
description: Generates an ETW event for the specified file, with additional parameter options and a new overrideInfoJson parameter.
title: DlpAuditOperationEnforcementEventEx4 function (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpAuditOperationEnforcementEventEx4
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpAuditOperationEnforcementEventEx4 function

Generates an ETW event for the specified file, with additional parameter options and a new *overrideInfoJson* parameter.

## Syntax

```C++
    HRESULT WINAPI DlpAuditOperationEnforcementEventEx4(
        _In_z_ LPCWSTR source,
        _In_opt_z_ LPCWSTR target,
        _In_z_ LPCWSTR actionType,
        _In_ DlpEnforcementLevel enforcementLevel,
        _In_ BOOLEAN userBypass,
        _In_ DlpTraceInfo* traceInfo,
        _In_opt_z_ LPCWSTR businessJustification,
        _In_opt_z_ LPCWSTR printerOutputFileName,
        _In_opt_z_ LPCWSTR printerName,
        _In_opt_z_ LPCWSTR printerJobName,
        _In_opt_z_ LPCWSTR overrideInfoJson);
```

## Parameters

`source` [in]: A [fully qualified Win32 file path](/windows/win32/fileio/naming-a-file) for the file to be analyzed.

`target` [in]: The target to trace. When investigating some operations like Print or Copy to Keyboard, this property can be NULL.

`actionType` [in]: The `DlpAction` type to trace.

`enforcementlevel` [in]: The enforcement level of the file specified.

`userbypass` [in]: Indicates the user decision if the `DlpEnforcementLevel` is set to Warn. A value of TRUE indicates that the operation is allowed, a value of FALSE disallows the operation.

`traceInfo` [in]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the `PolicyRuleID` assigned to the file. This value can be NULL.

`businessJustification` [in]: A business justification for the generated enforcement event.

`printerOutputFileName` [in]: The printer output file name. Only necessary when the `actionType` parameter is set to `DlpWebSiteActionTypePrint`.

`printerName` [in]: The printer name. Only necessary when the `actionType` parameter is set to `DlpWebSiteActionTypePrint`.

`printerJobName` [in]: The printer job name. Only necessary when the `actionType` parameter is set to `DlpWebSiteActionTypePrint`.

`overrideInfoJson` [in]: A JSON string containing override information for the enforcement event. It  is obtained by calls to [DlpHandleRequest](endpointdlp-dlphandlerequest.md) with `DlpRequestId=RequestIdAuthorizedGroupOverrideEdge`.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `FAILED` | An unexpected error prevented the function from completing. |


## Remarks

This function can be called from multiple threads.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpAuditOperationEnforcementEventEx2 function](endpointdlp-dlpauditoperationenforcementeventex.md)
- [DlpHandleRequest](endpointdlp-dlphandlerequest.md)
