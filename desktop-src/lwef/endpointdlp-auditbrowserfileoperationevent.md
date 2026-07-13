---
description: Generates an ETW event for a browser file operations.
title: AuditBrowserFileOperationEvent function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuditBrowserFileOperationEvent
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# AuditBrowserFileOperationEvent function

Generates an ETW event for a browser file operations.

## Syntax

```C++
HRESULT WINAPI AuditBrowserFileOperationEvent(_In_z_ LPCWSTR source, _In_z_ LPCWSTR target, _In_z_ LPCWSTR actionType, BrowserType browserType, ::EventSource eventSource, DlpEnforcementLevel enforcementLevel, BOOLEAN userBypass, _In_ DlpTraceInfo* traceInfo, _In_z_ LPCWSTR targetDomain, _In_z_ LPCWSTR fileName, ULONGLONG lastModifiedTime, ULONGLONG fileSize, _In_z_ LPCWSTR printerOutputFileName, _In_z_ LPCWSTR printerName, _In_z_ LPCWSTR printerJobName);
```

## Parameters

Some parameters are specific to certain action types. See Remarks for details.

### Common parameters

`source` [in]: The full file path of the target file.

`target` [in]: The target to trace. For certain operations without a target, this can be NULL.

`actionType` [in]: The website action type to trace. See possible values below in Remarks.

`browserType`: The browser type used for the event being traced.

`eventSource`: The scenario that triggered the event being traced.

`enforcementLevel`: The enforcement level of the specified file.

`userbypass`: Indicates the user decision if the `DlpEnforcementLevel` is set to Warn. A value of TRUE indicates that the operation is allowed, a value of FALSE disallows the operation.

`userbypass` [in]: Indicates the user decision if the `DlpEnforcementLevel` is set to Warn. A value of TRUE indicates that the operation is allowed, a value of FALSE disallows the operation.

`traceInfo` [in]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the `PolicyRuleID` assigned to the file. This value can be NULL.

### Action-specific parameters

`targetDomain` [in]: The target domain.

`fileName` [in]: The file name. Filled only in action type `CloudEgress` where the full file path is unavailable.

`lastModifiedTime` [in]: The file last modified time. Filled only in action type `CloudEgress` where the full file path is unavailable.

`fileSize` [in]: The file size. Filled only in action type `CloudEgress` where the full file path is unavailable.

`printerOutputFileName` [in]: The printer output file name.

`printerName` [in]: The printer name.

`printerJobName` [in]: The printer job name.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `FAILED` | An unexpected error prevented the function from completing. |



## Remarks

The following are the supported `actionType` values for this function, and the associated optional parameters expected by the function for each type value.

| `actionType` | Action-specific parameters |
|--------------|----------------------------|
| `CloudEgress` | `targetDomain, fileName, lastModifiedTime, fileSize ` |
| `Print` | `PrinterOutputFileName, PrinterName, PrinterJobName` |


This function can be called from multiple threads.

## Requirements

| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |