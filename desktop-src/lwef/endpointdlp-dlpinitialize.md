---
description: Initializes the internal data structure for endpoint Data Loss Prevention (DLP) functions.
title: DlpInitialize function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpInitialize
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpInitialize function

Initializes the internal data structure for endpoint Data Loss Prevention (DLP) functions.

## Syntax

```C++
HRESULT WINAPI DlpInitialize(void);
```

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `FAILED` | An unexpected error prevented the function from completing. |


## Remarks

Before calling any other API, the caller should call this function. Other API calls will fail if the internal data structure is not initialized.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |