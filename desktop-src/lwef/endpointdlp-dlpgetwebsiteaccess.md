---
description: Returns whether any website rules have been configured for DLP.
title: DlpGetWebsiteAccess function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetWebsiteAccess
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetWebsiteAccess function

Returns a list of actions and their associated enforcement level, for each operation of a specified website address.

## Syntax

```C++
HRESULT WINAPI DlpGetWebSiteAccess(_In_z_ LPCWSTR webSiteAddress, _Inout_ DWORD* numOfActions, _Inout_updates_(*numOfActions) DlpWebSiteAction *actions, _Out_opt_ DlpTraceInfoEx* traceInfoEx);
```

## Parameters

`webSiteAddress` [in]: The URL of the specified website.

`numOfActions` [in/out]: In the function call, this parameter holds the size of the `DlpWebSiteAction` array. On a successful function call, it specifies the number of relevant actions.

`*actions` [in/out]: A pointer to a pre-allocated array of `DlpWebSiteAction` objects. On a successful function call, it specifies a list of actions that should be applied on the website.

`traceInfoEx` [out]: A reference to a Trace structure. On successful completion, this structure contains the Policy version used for evaluation and the `PolicyRuleID` assigned to the file. This value can be NULL. The caller should call [DlpFreeArchiveFileTraceInfo](endpointdlp-dlpfreearchivefiletraceinfo.md) on this structure when done.

## Return value

Returns an `HRESULT` including, but not limited to, the following values.

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `E_OUTOFMEMORY` | The action array size specified in *numOfActions* isn't big enough to hold the list of actions returned. |
| `ACCESS_DENIED` | The user doesn't have permission to view the designated file. |
| `FAILED` | An unexpected error prevented the function from completing. |


## Remarks

This function can be called from multiple threads.

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |