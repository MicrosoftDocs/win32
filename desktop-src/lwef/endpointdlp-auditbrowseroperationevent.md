---
description: Generates an ETW event for a browser operation.
title: AuditBrowserOperationEvent function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuditBrowserOperationEvent
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# AuditBrowserOperationEvent function

Generates an ETW event for a browser operation.

## Syntax

```C++
HRESULT WINAPI AuditBrowserOperationEvent(_In_z_ LPCWSTR actionType, BrowserType browserType, ::EventSource eventSource, _In_z_ LPCWSTR url, _In_z_ LPCWSTR finalUrl, _In_z_ LPCWSTR target, _In_z_ LPCWSTR printerOutputFileName, _In_z_ LPCWSTR printerName, _In_z_ LPCWSTR printerJobName);
```

## Parameters

Some parameters are specific to certain action types. See Remarks for details.

### Common parameters

`actionType` [in]: The website action type to trace. See possible values below in Remarks.

`browserType`: The browser type used for the event being traced.

`eventSource`: The scenario that triggered the event being traced.

### Action-specific parameters

`url` [in]: The URL of the web page.

`finalUrl` [in]: The absolute URL that a download is being made from, after all redirects.

`target` [in]: The target file path.

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
| `CopyWebpageToClipboard` | `url` |
| `BrowseToUrl` | `url` |
| `PrintWebpage` | `url, PrinterOutputFileName, PrinterName, PrinterJobName`|
| `CopyWebpageToNetworkShare` | `url, Target` (full-file path)|
| `CopyWebpageToRemovableMedia` | `url, Target` (full-file path)|
| `BrowserHistoryCleanUp` | n/a |
| `PrivateBrowsingEnabled` | n/a |
| `Download` (file download) | `url, finalUrl, target`(File name)|

This function can be called from multiple threads.

## Requirements

| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |