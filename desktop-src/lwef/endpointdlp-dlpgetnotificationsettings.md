---
description: Returns the notification settings and strings for a given DLP rule and action type.
title: DlpGetNotificationSettings function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetNotificationSettings
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetNotificationSettings function

Returns the notification settings and strings for a given DLP rule and action type.

## Syntax

```C++
HRESULT WINAPI DlpGetNotificationSettings(_In_z_ LPCWSTR locale, _In_z_ LPCWSTR policyVersion, _In_z_ LPCWSTR policyRuleId, _In_ DlpActionType actionType, _In_ BOOLEAN isUnallowedBrowser, _In_z_ LPCWSTR displayFilename, _In_z_ LPCWSTR displayProcessName, _In_opt_z_ LPCWSTR jsonExtraInfo, _Inout_ DWORD* bufferSize, _Inout_updates_(*bufferSize) WCHAR* jsonNotification);
```

## Parameters

`locale` [in]: The language locale to retrieve. Required.

`policyVersion` [in]: Blocking policy version, provided in `DlpTraceInfo`. Required.

`policyRuleId` [in]: Blocking rule ID, provided in `DlpTraceInfo`. Required.

`actionType` [in]: `DlpActionType` corresponding to the settings. Required. If `DlpGetFileCloudApplicationPolicy` was used, use the action type `DlpActionTypeCloudAppEgress`.

`isUnallowedBrowser` [in]: Indicates if the application is on the unallowed browser list. For use by Windows Defender.

`displayFilename` [in]: The filename to display. Can be the full path, or just the file name. Use `|` to separate multiple files. Required.

`displayProcessName` [in]: User-friendly process or app name to display. Required.

`jsonExtraInfo` [in]: JSON input for additional information. Optional.

`bufferSize` [in/out]: Size of the allocated buffer for JSON input. On return, contains the number of wchars written or allocated. Required if providing JSON for additional information.

`jsonNotification` [in/out]: A buffer containing the JSON input.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `E_OUTOFMEMORY` | The dropdown array size isn't big enough. |
| `FAILED` | An unexpected error prevented the function from completing. |

## Remarks

The JSON schema for additional information is as follows:

```json
{
    "title" : "<string>",           // notification title text
    "body" : "<string>",            // notification content text
    "showdropdown" : <bool>,        // flag to indicate if business justification dropdown should be shown
    "showtextbox" : <bool>,         // flag to indicate if business justification text box should be shown
    "dropdownlist" : [              // list of dropdown options to show
        {
            "id" : "<string>",      // internal id to use for reporting to sense/backend
            "text" : "<text>"       // text to for the dropdown option shown to the user
        },
        ...
    ]
}
```

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |