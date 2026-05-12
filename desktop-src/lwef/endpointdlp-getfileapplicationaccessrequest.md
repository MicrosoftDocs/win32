---
description: The request returns a list of actions that contains the Enforcement Level of each operation for specific file.
title: GetFileApplicationAccessRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFileApplicationAccessRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# GetFileApplicationAccessRequest structure

A request structure for sending file cloud application policy requests. The request returns a list of actions that contain the Enforcement Level of each operation for a specific file. If the application is enlightened, the list of actions will contain Enforcement Level of None for each operation.

## Syntax

```cpp
struct GetFileApplicationAccessRequest
{
    _Field_z_ LPCWSTR filePath;
    _Field_z_ LPCWSTR applicationName;
    BOOLEAN* isRestrictedBrowserApp;
    DWORD* numOfActions;
    _Field_size_(*numOfActions) DlpAction* actions;
    DlpSerializedBuffer policyInfo;
};
```

## Members

*filePath* `[IN]`

The fully qualified win32 file path as defined [here](/windows/win32/fileio/naming-a-file).

*applicationName* `[IN]`

The image name of the process that handles the file. For example: notepad.exe, chrome.exe.

*isRestrictedBrowserApp* `[OUT]`

Indicates whether the application is a browser that is restricted from opening the file.

*numOfActions* `[IN/OUT]`

In call the parameter holds the size of the `DlpAction` array. On return it contains the number of relevant actions.

*actions* `[OUT]`

A pointer to a pre-allocated array of `DlpAction` whose size is defined by the **numOfActions** field. On successful call, it contains a list of actions that should be applied on the file.

*policyInfo* `[OUT]`

A pointer to a [DlpSerializedBuffer](endpointdlp-dlpserializedbuffer.md) containing the internal policy information that should be passed to reporting APIs when an enforcement action occurs. This buffer must be freed using [DlpReleaseBuffer](endpointdlp-dlpreleasebuffer.md).

## Returns

The function returns S_OK if it succeeds. If not, it can return one of the following error codes:

- `E_OUTOFMEMORY` - The action array size isn't big enough.
- `ACCESS_DENIED` - The user doesn't have read permission for the file EA. In this case, the caller should impersonate the correct user context and retry the function call. Returns a FAILED HRESULT otherwise.

## Remarks

Corresponds to **RequestIdGetFileApplicationAccess** in [DlpRequestId](endpointdlp-dlprequestid.md).

Note that this function can be called from multiple threads.

The policy defines two lists: unallowed applications and cloud egress applications. The unallowed applications list is used to determine whether to enforce **AccessByUnallowedApp** action type when a file is opened by the application. If the application isn’t in the list, there is no enforcement.

The cloud egress list is used when enforcing **CloudAppEgress** action. If the action is set to `Audit`, `Warn` or `Block`, and the application type is in the list, it will be identified as a browser. Only browsers that are enlightened for Endpoint DLP are allowed to open the file and all others are restricted.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
