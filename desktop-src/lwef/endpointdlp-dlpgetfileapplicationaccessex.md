---
description: Returns a list of DlpAction objects that contain the enforcement level of each operation in a specified file.
title: DlpGetFileApplicationAccessEx function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetFileApplicationAccessEx
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetFileApplicationEx function

Returns a list of `DlpAction` objects that contain the enforcement level of each operation in a specified file.

## Syntax

```C++
HRESULT WINAPI DlpGetFileApplicationAccessEx(_In_z_ LPCWSTR filePath, _In_z_ LPCWSTR applicationName, DWORD processId, ULONGLONG processCreationTime, DWORD extendedAttributeSize, _In_reads_bytes_opt_(extendedAttributeSize) PBYTE pExtedendedAttributeBlob, _Out_ BOOLEAN* isRestrictedBrowserApp, _Inout_ DWORD* numOfActions, _Inout_updates_(*numOfActions) DlpAction* actions, _Out_opt_ DlpTraceInfo* traceInfo);
```

## Parameters

`filePath` [in]: A [fully qualified Win32 file path](https://docs.microsoft.com/windows/win32/fileio/naming-a-file) for the file to be analyzed.

`applicationName` [in]: The disk image name of the process that handles the file (such as `notepad.exe`, `chrome.exe`, etc).

`processId`: The process ID of the process that handles the file. If this is set to 0, the process check will be ignored.

`processCreationTime`: The process creation time of the process that handles the file. If this is set to 0, only the process ID will be used to identify the file.

`extendedAttributeSize`: The size, in bytes, of the extended attribute blob. If `pExtedendedAttributeBlob` is set to NULL, this field is ignored.

`pExtedendedAttributeBlob`: A pointer to an external attributes object. This can be NULL, in such a case the function will read the external attributes internally.

`isRestrictedBrowserApp` [out]: A pointer to a boolean variable, indicating whether the application is a browser restricted from opening the specified file.

`numOfActions` [in/out]: In the function call, this parameter holds the size of the `DlpAction` array. On a successful function call, it specifies the number of relevant actions.

`actions` [in/out]: A pointer to a pre-allocated array of `DlpAction` objects. On a successful function call, it specifies a list of actions that should be applied on the file.

`traceInfo` [out]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the `PolicyRuleID` assigned to the file. This value can be NULL.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully |
| `E_OUTOFMEMORY` | The action array size specified in *numOfActions* isn't big enough to hold the list of actions returned. |
| `ACCESS_DENIED` | The user doesn't have permission to view the designated file. |
| `FAILED` | An unexpected error prevented the function from completing. |


## Remarks

This function can be called from multiple threads.

Enforcement policy defines two lists: unallowed applications and cloud egress applications.

The unallowed Applications list is used to determine whether to enforce the `AccessByUnallowedApp` action type when a file is opened by the application. If the application isn’t in the list, no enforcement is applied.

The cloud egress list is used when enforcing the `CloudAppEgress` action. If the action is set to `Audit`, `Warn` or `Block`, and the application type is in the list, it will be identified as a browser. Only browsers that are enlightened for Endpoint DLP are allowed to open the file, all other browsers are restricted.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |