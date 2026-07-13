---
description: The request returns the Enforcement Level of a file uploading to Cloud App.
title: GetFileCloudApplicationPolicyRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFileCloudApplicationPolicyRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# GetFileCloudApplicationPolicyRequest structure

A request structure for sending file access events. The request returns the Enforcement Level of a file uploading to Cloud App.

## Syntax

```cpp
struct GetFileCloudApplicationPolicyRequest
{
    _Field_z_ LPCWSTR filePath;
    _Field_z_ LPCWSTR cloudAppDomainName;
    _Field_z_ LPCWSTR url;
    DlpEnforcementLevel* enforcementLevel;
    DlpSerializedBuffer policyInfo;`
};
```

## Members

*filePath* `[IN]`

The fully qualified file path as defined [here](/windows/win32/fileio/naming-a-file).

*cloudAppDomainName* `[IN]`

The domain name component of the URI for the web application that's trying to access the file.

*url* `[IN]`

URL of a website.

*enforcementLevel* `[OUT]`

The enforcement level of the file. Note that if the file is excluded or isn't marked as "sensitive", the "off" enforcement level is returned. If the file wasn't classified, an "off" enforcement level is returned.

*policyInfo* `[OUT]`

A [DlpSerializedBuffer](endpointdlp-dlpserializedbuffer.md) containing internal policy information that should be passed to reporting APIs when an enforcement action occurs. This buffer must be freed using [DlpReleaseBuffer](endpointdlp-dlpreleasebuffer.md).

## Returns

Returns `S_OK` if the function succeeds or `ACCESS_DENIED` if the user doesn't have read permission for the file EA. In this case, the caller should impersonate the correct user context and retry the function call. Returns a FAILED HRESULT otherwise.

## Remarks

Corresponds to **RequestIdGetFileCloudApplicationPolicy** in [DlpRequestId](endpointdlp-dlprequestid.md).

Request can be performed from multiple threads.

This function is called from external sources like Edge that don't have to compute the User SID. The User SID will be detected using the current process where endpointDlp is loaded.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
