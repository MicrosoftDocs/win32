---
description: Returns whether DLP/IRM is enabled upon the browser.
title: GetBrowserExtensionConfiguration function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetBrowserExtensionConfiguration
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# GetBrowserExtensionConfiguration function

Returns whether DLP/IRM is enabled upon the browser.

## Syntax

```C++
GetBrowserExtensionConfiguration(_Out_ BrowserConfiguration* browserConfiguration);
```

## Parameters

`browserConfiguration` [out]: The status of DLP/IRM on the browser.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `ERROR_DLL_INIT_FAILED` | The function was called before [DlpInitialize](endpointdlp-dlpinitialize.md) was called. |


## Remarks

This function can be called from multiple threads.

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |