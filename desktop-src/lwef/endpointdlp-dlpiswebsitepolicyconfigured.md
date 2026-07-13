---
description: Returns whether any website rules have been configured for DLP.
title: DlpIsWebsitePolicyConfigured function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpIsWebsitePolicyConfigured
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpIsWebsitePolicyConfigured function

Returns whether any website rules have been configured for DLP.

## Syntax

```C++
HRESULT WINAPI DlpIsWebsitePolicyConfigured(_Out_ BOOLEAN* isWebSitePolicyConfigured);
```

## Parameters

`isWebSitePolicyConfigured` [out]: Whether or not the website rules have been configured.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `ERROR_DLL_INIT_FAILED` | The function was called before [DlpInitialize](endpointdlp-dlpinitialize.md) was called. |
| `FAILED` | An unexpected error prevented the function from completing. |


## Remarks

This function can be called from multiple threads.

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |