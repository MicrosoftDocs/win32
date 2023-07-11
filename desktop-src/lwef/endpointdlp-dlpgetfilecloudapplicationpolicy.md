---
description: Returns the enforcement level of a file uploaded to a cloud application.
title: DlpGetFileCloudApplicationPolicy function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetFileCloudApplicationPolicy
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetFileCloudApplicationPolicy function

Returns the enforcement level of a file uploaded to a cloud application.

## Syntax

```C++
HRESULT WINAPI DlpGetFileCloudApplicationPolicy(_In_z_ LPCWSTR filePath, _In_z_ LPCWSTR cloudAppDomainName, _Out_ DlpEnforcementLevel* enforcmentLevel, _Out_ DlpTraceInfo* traceInfo);
```

## Parameters

`filePath` [in]: A [fully qualified Win32 file path](https://docs.microsoft.com/windows/win32/fileio/naming-a-file) for the file to be analyzed.

`cloudAppDomainName` [in]: The domain name component of the URI for the application accessing the file.

`enforcmentLevel` [out]: The enforcement level of the designated file. If the file is excluded from enforcement or isn't marked as sensitive, an "off" result is returned.

`traceInfo` [out]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the PolicyRuleID assigned to the file. This value can be NULL.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `ACCESS_DENIED` | The user doesn't have permission to view the designated file. |
| `FAILED` | An unexpected error prevented the function from completing. |



## Remarks

This function can be called from multiple threads.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |