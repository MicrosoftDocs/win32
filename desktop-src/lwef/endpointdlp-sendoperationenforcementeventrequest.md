---
description: A request structure for sending operation enforcement events.
title: SendOperationEnforcementEventRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SendOperationEnforcementEventRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# SendOperationEnforcementEventRequest structure

A request structure for sending operation enforcement events. The request is responsible for generating an ETW event for operation enforcement DLP.

## Syntax

```cpp
struct SendOperationEnforcementEventRequest
{
    _Field_z_ LPCWSTR source;
    _Field_z_ LPCWSTR target;
    _Field_z_ LPCWSTR actionType;
    DlpSerializedBuffer policyInfo;
    DlpEnforcementLevel enforcementLevel;
    BOOLEAN userBypass;
    _Field_z_ LPCWSTR businessJustification;
    _Field_z_ LPCWSTR printerOutputFileName;
    _Field_z_ LPCWSTR printerName;
    _Field_z_ LPCWSTR printerJobName;
    _Field_z_ LPCWSTR overrideInfoJson;
};
```

## Members

*source* `[in]`

Fully qualified Win32 file path as defined in [Naming a file](/windows/win32/fileio/naming-a-file).

*target* `[IN][OPTIONAL]`

The target to trace. The parameter can be `NULL` for some of the operations like print or copy to clipboard.

*actionType* `[IN]`

The ActionType to trace.

*policyInfo* `[IN]`

Policy info obtained from a `GetFileCloudApplicationPolicyRequest` or `GetFileApplicationAccessRequest` policy request.

*enforcementLevel* `[IN]`

The enforcement level of the file.

*userBypass* `[IN]`

Indicates the user decision on `DlpEnforcementLevel::Warn`. When `TRUE`, indicates the user allow the operation. `FALSE`, otherwise.

*businessJustification* `[IN][OPTIONAL]`

Business justification string, if any.

*printerOutputFileName* `[IN][OPTIONAL]`

The printer output file name. Provided only when *actionType* is `DlpWebSiteActionTypePrint`.

*printerName* `[IN][OPTIONAL]`

The printer name. Provided only when *actionType* is `DlpWebSiteActionTypePrint`.

*printerJobName* `[IN][OPTIONAL]`

The printer job name. Provided only when *actionType* is `DlpWebSiteActionTypePrint`.

*overrideInfoJson* `[IN][OPTIONAL]`

JSON string containing override information.

## Returns

Returns `S_OK` if the function succeeds. Otherwise, it returns a failed HRESULT.

## Remarks

Corresponds to **RequestIdSendOperationEnforcementEvent** in the [DlpRequestId](endpointdlp-dlprequestid.md).

Note that the function can be called from multiple threads.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
