---
description: Allows DLP enforcement to be delegated to Windows Defender or to DLP-enlightened applications, as needed.
title: DlpDelegateEnforcement function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpDelegateEnforcement
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpDelegateEnforcement function

Allows DLP enforcement to be delegated to Windows Defender or to DLP-enlightened applications, as needed.

## Syntax

```C++
HRESULT WINAPI DlpDelegateEnforcement(_In_ BOOLEAN isEnable);
```

## Parameters

`isEnable` [in]: A result of TRUE indicates that calling processes for DLP enforcement should be deferred to the Windows Defender service. A result of FALSE returns behavior to the default state, where Windows Defender behaves as per policies returned by other endpoint DLP APIs.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The delegation request is successful. |
| `FAILED` | An unexpected error prevented the function from completing. |



## Remarks

This function can be called from multiple threads.

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |