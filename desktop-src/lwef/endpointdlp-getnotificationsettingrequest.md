---
description: The function returns the notification settings and strings for given rule and action type.
title: GetNotificationSettingRequest structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNotificationSettingRequest
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# GetNotificationSettingRequest structure

A request structure for sending notification setting requests. The request returns the notification settings and strings for given rule and action type.

## Syntax

```cpp
struct GetNotificationSettingRequest
{
    _Field_z_ LPCWSTR locale;
    DlpSerializedBuffer policyInfo;
    DlpActionType actionType;
    BOOLEAN isUnallowedBrowser;
    _Field_z_ LPCWSTR displayFilename;
    _Field_z_ LPCWSTR displayProcessName;
    _Field_z_ LPCWSTR jsonExtraInfo;
    DlpSerializedBuffer jsonNotification;
};
```

## Members

*locale* `[IN]`

The language locale to retrieve (e.g. "en-us"). This parameter is required and shouldn't be empty.

*policyInfo* `[IN]`

The policy information obtained from a `GetFileCloudApplicationPolicyRequest` or `GetFileApplicationAccessRequest` Policy Request.

*actionType* `[IN]`

The action type for the notification request. Note that if `DlpGetFileCloudApplicationPolicy` was used, `actionType=DlpActionTypeCloudAppEgress`.

*isUnallowedBrowser* `[IN]`

Indicates if the application is on the unallowed browser list. This is to be treated differently from an unallowed app. For Microsoft Defender use.

*displayFilename* `[IN]`

The filename to display. It's up to the caller to decide if full path or just filename. For multiple files, delimit them with `|`. This parameter is required and shouldn't be empty.

*displayProcessName* `[IN]`

The user-friendly process or app name to display. This parameter is required and shouldn't be empty.

*jsonExtraInfo* `[IN][OPTIONAL]`

JSON input for additional information.

*jsonNotification* `[OUT]`

Buffer containing the notification settings JSON. Must be freed using [DlpReleaseBuffer](endpointdlp-dlpreleasebuffer.md).

The jsonNotification schema is defined as:

```json
{
  "title" : "<string>",       // notification title text
  "body" : "<string>",        // notification content text
  "showdropdown" : <bool>,    // flag to indicate if business justification dropdown should be shown
  "showtextbox" : <bool>,     // flag to indicate if business justification text box should be shown
  "dropdownlist" : [          // list of dropdown options to show
    {
      "id" : "<string>",      // internal id to use for reporting to sense/backend
      "text" : "<text>"       // text to for the dropdown option shown to the user
    },
    ...
  ]
}
```

## Returns

Returns **S_OK** if it succeeds, **E_OUTOFMEMORY** if the dropdown array size isn't big enough, or **FAILED** otherwise.

## Remarks

Corresponds to **RequestIdGetNotificationSetting** in [DlpRequestId](endpointdlp-dlprequestid.md).

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpRequest](endpointdlp-dlprequest.md)
