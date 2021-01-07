---
description: The ExpertIndicateStatus function indicates the percentage of completion of the experts analysis of the capture file.
ms.assetid: 6dbaa6d3-6068-4a28-9d9f-bcc7a25da407
title: ExpertIndicateStatus function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertIndicateStatus
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertIndicateStatus function

The **ExpertIndicateStatus** function indicates the percentage of completion of the expert's analysis of the capture file.

## Syntax


```C++
DWORD WINAPI ExpertIndicateStatus(
  _In_  HEXPERTKEY              hExpertKey,
  _In_  EXPERTSTATUSENUMERATION Status,
  _In_  DWORD                   SubStatus,
  _In_  char                    *sztext,
  _Out_ long                    PercentDone
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique expert identifier. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*Status* \[in\]
</dt> <dd>

Current status of the analysis. Specify one of the following [EXPERTSTATUSENUMERATION](expertstatusenumeration.md) values.



| Value                                                                                                                                                                                 | Meaning                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="EXPERTSTATUS_INACTIVE"></span><span id="expertstatus_inactive"></span><dl> <dt>**EXPERTSTATUS\_INACTIVE**</dt> </dl> | The expert never started. <br/>                                          |
| <span id="EXPERTSTATUS_STARTING"></span><span id="expertstatus_starting"></span><dl> <dt>**EXPERTSTATUS\_STARTING**</dt> </dl> | The expert is starting. <br/>                                            |
| <span id="EXPERTSTATUS_RUNNING"></span><span id="expertstatus_running"></span><dl> <dt>**EXPERTSTATUS\_RUNNING**</dt> </dl>    | The expert is running normally. <br/>                                    |
| <span id="EXPERTSTATUS_PROBLEM"></span><span id="expertstatus_problem"></span><dl> <dt>**EXPERTSTATUS\_PROBLEM**</dt> </dl>    | A problem specified in the SubStatus parameter stopped the expert. <br/> |
| <span id="EXPERTSTATUS_ABORTED"></span><span id="expertstatus_aborted"></span><dl> <dt>**EXPERTSTATUS\_ABORTED**</dt> </dl>    | Network Monitor stopped the expert. <br/>                                |
| <span id="EXPERTSTATUS_DONE"></span><span id="expertstatus_done"></span><dl> <dt>**EXPERTSTATUS\_DONE**</dt> </dl>             | The expert finished the analysis successfully. <br/>                     |



 

</dd> <dt>

*SubStatus* \[in\]
</dt> <dd>

Extension or clarification of information provided by the *Status* parameter.

</dd> <dt>

*sztext* \[in\]
</dt> <dd>

Optional text status indicator.

This parameter value may be **NULL**.

</dd> <dt>

*PercentDone* \[out\]
</dt> <dd>

Percentage of the capture data that the expert has processed.

When the expert successfully completes analysis of a capture file, the system sets the percentage to 100. Any number greater than 99 will be ignored.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is NMERR\_EXPERT\_TERMINATE; the expert must immediately clean up and return without completing the capture.

## Remarks

The **ExpertIndicateStatus** function can only be called by experts that implement the [Run](run.md) or [Configure](configure.md) export function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |
