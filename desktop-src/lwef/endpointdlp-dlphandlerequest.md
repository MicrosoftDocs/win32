---
description: Handles a DLP request.
title: DlpHandleRequest function (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpHandleRequest
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpHandleRequest function

A generic interface for interacting with Endpoint DLP.

## Syntax

```cpp
HRESULT WINAPI DlpHandleRequest(_Inout_ DlpRequest* request);
```

## Parameters

`request` [in, out]: A pointer to a [DlpRequest](endpointdlp-dlprequest.md) structure that contains the parameters and result storage for the request. This parameter must not be `NULL`.

## Return value

Returns an `HRESULT` including, but not limited to, the following values:

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `E_NOTIMPL` | The request is not supported. |
| `E_INVALIDARG` | The request is invalid. |

## Example

```cpp
// Create a request for Endpoint DLP
DlpEnforcementLevel enforcementLevel = DlpEnforcementLevelOff;
auto policyRequest = GetFileCloudApplicationPolicyRequest
{
    // [In] Parameters
    .filePath = file_path,
    .cloudAppDomainName = cloud_app_host_name.c_str(),
    .url = url.c_str(),
    // [Out] Parameters
    .enforcementLevel = &enforcementLevel,
    .policyInfo = {}
};

auto request = DlpRequest
{
    .id = DlpRequestId::RequestIdGetFileCloudApplicationPolicy,
    .size = sizeof(GetFileCloudApplicationPolicyRequest),
    .getFileCloudApplicationPolicyRequest = &policyRequest,
};

// Call DlpHandleRequest
auto hr = DlpHandleRequest(&request);
if (FAILED(hr))
{
    return hr;
}

// Marshal Outputs
auto policyJSON = std::wstring{policyRequest.policyInfo.buffer, policyRequest.policyInfo.bufferSize};
DlpReleaseBuffer(&policyRequest.policyInfo);

std::wcout << L"Enforcement Level: " << enforcementLevel << std::endl;
std::wcout << L"Policy Information: " << policyJSON << std::endl;

return S_OK;
```

## Remarks

This function is designed to be a generic interface for handling DLP requests. The specific behavior is determined by the contents of the `DlpRequest` structure.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
