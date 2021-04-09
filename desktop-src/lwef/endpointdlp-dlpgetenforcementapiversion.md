---
description: Retrieves the version of the endpoint Data Loss Prevention (DLP) API on the current device.
title: DlpGetEnforcementApiVersion function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetEnforcementApiVersion
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetEnforcementApiVersion function

Retrieves the version of the endpoint Data Loss Prevention (DLP) API on the current device.

## Syntax


```C++
HRESULT WINAPI DlpGetEnforcementApiVersion(_Out_ DWORD* MajorVersion, _Out_ DWORD* MinorVersion);
```



## Parameters

<dl> <dt>

*MajorVersion* \[in\]
</dt> <dd>

A **DWORD** specifying the major version number.

</dd> </dl>

<dl> <dt>

*MajorVersion* \[in\]
</dt> <dd>

A **DWORD** specifying the minor version number.

</dd> </dl>


## Return value

Returns an HRESULT including, but not limited to, the following values.

| HRESULT | Description |
|---------|-------------|
| S_OK | The function completed successfully |




## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |