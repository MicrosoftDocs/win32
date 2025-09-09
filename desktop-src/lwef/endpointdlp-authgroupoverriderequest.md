---
description: A request structure for sending authentication group override requests.
title: AuthGroupOverrideRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuthGroupOverrideRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# AuthGroupOverrideRequest structure

A request structure for sending authentication group override requests. Checks whether the target of an enforcement action has an applicable authorized group that should alter the enforcement.

## Syntax

```cpp
struct AuthGroupOverrideRequest
{
    LPCWSTR filePath;
    LPCWSTR attrDetails;
    DlpActionType action;
    DlpSerializedBuffer outputBuffer;
};
```

## Members

*filePath* `[in]`

The path to the source file of the action.

*attrDetails* `[in]`

The details associated with the specific action. This will vary depending on the *action* type:

- `DlpActionTypeCopyToRemovableMedia`: Target Path of the save operation (on a removable media device)
- `DlpActionTypeCopyToNetworkShare`: Target Path of the save operation (on a network share)
- `DlpActionTypePrint`: Name of the printer

*action* `[in]`

The action to evaluate authorized groups for. Can be `DlpActionTypeCopyToRemovableMedia`, `DlpActionTypeCopyToNetworkShare`, or `DlpActionTypePrint`.

*outputBuffer* `[out]`

AuthGroup metadata and enforcement as a JSON string. This should be passed as the *overrideInfoJson* parameter to `DlpAuditOperationEnforcementEventEx4`. The buffer must be freed using `DlpReleaseBuffer`.

The schema is defined as:

```json
{
  "enforcement" : <int>,          // new enforcement
  "ruleId" : "<string>",          // most restrictive rule
  "applicableRules" : "<string>", // semi-colon delimited list of all applicable rules
  "policyVersion" : "<string>",   // policy version
  "alertNeeded" : <bool>,         // Should this action alert
  "overrideActionInfo" : {}       // Information about the override group
}
```

## Returns

Returns **S_OK** if successful, or a **HRESULT** error code otherwise.

## Remarks

Corresponds to **RequestIdAuthorizedGroupOverrideEdge** in [DlpRequestId](endpointdlp-dlprequestid.md).

When saving a file to a removable storage device, this API will evaluate the device attributes of the storage device to determine if it is a member of an authorized group. If it is, the *outputBuffer* will contain new enforcement actions that should be used instead of the original enforcement provided by [GetFileApplicationAccess](endpointdlp-getfileapplicationaccessrequest.md).

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
