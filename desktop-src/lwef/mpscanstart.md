---
title: MpScanStart function (MpClient.h)
description: Starts a scanning operation.
ms.assetid: 3AF147C8-A41F-4193-AE28-72C1FBD18BA2
keywords:
- MpScanStart function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpScanStart
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpScanStart function

Starts a scanning operation.

## Syntax


```C++
HRESULT WINAPI MpScanStart(
  _In_     MPHANDLE          hMpHandle,
  _In_     MPSCAN_TYPE       ScanType,
  _In_     DWORD             dwScanOptions,
  _In_opt_ PMPSCAN_RESOURCES pScanResources,
  _In_opt_ PMPCALLBACK_INFO  pCallbackInfo,
  _Out_    PMPHANDLE         phScanHandle
);
```



## Parameters

<dl> <dt>

*hMpHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to the malware protection manager interface. This handle is returned by the [**MpManagerOpen**](mpmanageropen.md) function.

</dd> <dt>

*ScanType* \[in\]
</dt> <dd>

Type: **[**MPSCAN\_TYPE**](mpscan-type.md)**

Specifies the type of scan. This parameter must be one of the members of the [**MPSCAN\_TYPE**](mpscan-type.md) enueration.

</dd> <dt>

*dwScanOptions* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies various options for scanning operation.



| Value                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MPSCAN_OPTION_NONE"></span><span id="mpscan_option_none"></span><dl> <dt>**MPSCAN\_OPTION\_NONE**</dt> </dl>                               | No specific option is requested.<br/>                                                                                                                                                                                                                           |
| <span id="MPSCAN_OPTION_ASYNC"></span><span id="mpscan_option_async"></span><dl> <dt>**MPSCAN\_OPTION\_ASYNC**</dt> </dl>                            | The scan operation is to be asynchronous, where **MpScanStart** returns immediately after the successful initiation of scanning. (By default the scan operation is synchronous, meaning **MpScanStart** will return only after the scan is finished.)<br/>      |
| <span id="MPSCAN_OPTION_PROGRESS"></span><span id="mpscan_option_progress"></span><dl> <dt>**MPSCAN\_OPTION\_PROGRESS**</dt> </dl>                   | The caller is interested in receiving scan progress information via a callback.<br/>                                                                                                                                                                            |
| <span id="MPSCAN_OPTION_LOWPRIORITY"></span><span id="mpscan_option_lowpriority"></span><dl> <dt>**MPSCAN\_OPTION\_LOWPRIORITY**</dt> </dl>          | Perform the scan with low priority. (By default the scan operation is performed with normal priority.)<br/>                                                                                                                                                     |
| <span id="MPSCAN_OPTION_PACKEDEXES"></span><span id="mpscan_option_packedexes"></span><dl> <dt>**MPSCAN\_OPTION\_PACKEDEXES**</dt> </dl>             | Scan packed executables for possible threats.<br/>                                                                                                                                                                                                              |
| <span id="MPSCAN_OPTION_ARCHIVES"></span><span id="mpscan_option_archives"></span><dl> <dt>**MPSCAN\_OPTION\_ARCHIVES**</dt> </dl>                   | Scan archive contents for possible threats. Archives are files with extensions such as .zip, .cab, or .tar.<br/>                                                                                                                                                |
| <span id="MPSCAN_OPTION_HEURISTICS"></span><span id="mpscan_option_heuristics"></span><dl> <dt>**MPSCAN\_OPTION\_HEURISTICS**</dt> </dl>             | Enable heuristics-based scanning. This will scan for threats with detection type set to heuristics.<br/>                                                                                                                                                        |
| <span id="MPSCAN_OPTION_REPORTFRIENDLY"></span><span id="mpscan_option_reportfriendly"></span><dl> <dt>**MPSCAN\_OPTION\_REPORTFRIENDLY**</dt> </dl> | Report friendly items in a resource scan. This is intended for internal use only.<br/>                                                                                                                                                                          |
| <span id="MPSCAN_OPTION_REPORTUNKNOWN"></span><span id="mpscan_option_reportunknown"></span><dl> <dt>**MPSCAN\_OPTION\_REPORTUNKNOWN**</dt> </dl>    | Report unknown items in a resource scan. This is intended for internal use only.<br/>                                                                                                                                                                           |
| <span id="MPSCAN_OPTION_NOCONSOLIDATE"></span><span id="mpscan_option_noconsolidate"></span><dl> <dt>**MPSCAN\_OPTION\_NOCONSOLIDATE**</dt> </dl>    | Do not consolidate scan results with global threat view. This is useful for a client (such as an email client) which wants to control cleaning UX by itself rather than allowing default anti-malware cleaning UX. This is intended for internal use only.<br/> |



 

</dd> <dt>

*pScanResources* \[in, optional\]
</dt> <dd>

Type: **PMPSCAN\_RESOURCES**

A pointer to the scan resource information. This parameter must be **NULL** for a quick scan. This is an optional parameter for a full scan. For a resource scan this parameter must be specified with at least one resource information structure. To scan specific resources the caller must have **GENERIC\_READ** permission for the resource. See [**MPSCAN\_RESOURCES**](mpscan-resources.md).

</dd> <dt>

*pCallbackInfo* \[in, optional\]
</dt> <dd>

Type: **PMPCALLBACK\_INFO**

A pointer to the callback information used to feed the client with scan state changes (such as start and complete) and progress information. The [**MPCALLBACK\_DATA**](mpcallback-data.md) passed back in the callback function reports actual scan state and progress-related information. The following is a list of possible callbacks:



| Value                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MPNOTIFY_SCAN_START"></span><span id="mpnotify_scan_start"></span><dl> <dt>**MPNOTIFY\_SCAN\_START**</dt> </dl>                            | Scan operation started.<br/>                                                                                                                                                                                                                                                                                       |
| <span id="MPNOTIFY_SCAN_COMPLETE"></span><span id="mpnotify_scan_complete"></span><dl> <dt>**MPNOTIFY\_SCAN\_COMPLETE**</dt> </dl>                   | Scan operation completed. Additional information is available via [**MPSCAN\_DATA**](mpscan-data.md) structure.<br/>                                                                                                                                                                                              |
| <span id="MPNOTIFY_SCAN_PAUSED"></span><span id="mpnotify_scan_paused"></span><dl> <dt>**MPNOTIFY\_SCAN\_PAUSED**</dt> </dl>                         | Scan operation is paused.<br/>                                                                                                                                                                                                                                                                                     |
| <span id="MPNOTIFY_SCAN_RESUMED"></span><span id="mpnotify_scan_resumed"></span><dl> <dt>**MPNOTIFY\_SCAN\_RESUMED**</dt> </dl>                      | Scan operation resumed from pause.<br/>                                                                                                                                                                                                                                                                            |
| <span id="MPNOTIFY_SCAN_CANCEL"></span><span id="mpnotify_scan_cancel"></span><dl> <dt>**MPNOTIFY\_SCAN\_CANCEL**</dt> </dl>                         | Scan operation was cancelled.<br/>                                                                                                                                                                                                                                                                                 |
| <span id="MPNOTIFY_SCAN_PROGRESS"></span><span id="mpnotify_scan_progress"></span><dl> <dt>**MPNOTIFY\_SCAN\_PROGRESS**</dt> </dl>                   | Scan progress information. Additional information (such as resource statistics) is available via [**MPSCAN\_DATA**](mpscan-data.md) structure.<br/>                                                                                                                                                               |
| <span id="MPNOTIFY_SCAN_ERROR"></span><span id="mpnotify_scan_error"></span><dl> <dt>**MPNOTIFY\_SCAN\_ERROR**</dt> </dl>                            | Scan error information for a specific resource. The specific resource information is available via [**MPSCAN\_DATA**](mpscan-data.md) structure.<br/>                                                                                                                                                             |
| <span id="MPNOTIFY_SCAN_INFECTED"></span><span id="mpnotify_scan_infected"></span><dl> <dt>**MPNOTIFY\_SCAN\_INFECTED**</dt> </dl>                   | Scan found an infected resource. Note that in most of the cases this will result in some threat reported at the end of the scan. Sometimes it may not materialize as a threat because of exclusions. Additional infected resource information is available via [**MPSCAN\_DATA**](mpscan-data.md) structure.<br/> |
| <span id="MPNOTIFY_SCAN_MEMORYSTART"></span><span id="mpnotify_scan_memorystart"></span><dl> <dt>**MPNOTIFY\_SCAN\_MEMORYSTART**</dt> </dl>          | Quick scan portion of the full scan has started.<br/>                                                                                                                                                                                                                                                              |
| <span id="MPNOTIFY_SCAN_MEMORYCOMPLETE"></span><span id="mpnotify_scan_memorycomplete"></span><dl> <dt>**MPNOTIFY\_SCAN\_MEMORYCOMPLETE**</dt> </dl> | Quick scan portion of the full scan has completed.<br/>                                                                                                                                                                                                                                                            |
| <span id="MPNOTIFY_INTERNAL_FAILURE"></span><span id="mpnotify_internal_failure"></span><dl> <dt>**MPNOTIFY\_INTERNAL\_FAILURE**</dt> </dl>          | Scan operation has encountered a generic failure. The *hResult* in [**MPCALLBACK\_DATA**](mpcallback-data.md) has the specific error code.<br/>                                                                                                                                                                   |



 

</dd> <dt>

*phScanHandle* \[out\]
</dt> <dd>

Type: **PMPHANDLE**

Returned scan handle which identifies the currently initiated scan. This handle can be used in subsequent function calls, such as to retrieve a scan result. The handle must be closed with the [**MpHandleClose**](mphandleclose.md) function.

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**.

If the function fails then the return value is a failed **HRESULT** code. The caller can use the [**MpErrorMessageFormat**](mperrormessageformat.md) function to get a generic description of the error message.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MpClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**MpErrorMessageFormat**](mperrormessageformat.md)
</dt> <dt>

[**MpHandleClose**](mphandleclose.md)
</dt> <dt>

[**MpManagerOpen**](mpmanageropen.md)
</dt> <dt>

[**MPCALLBACK\_DATA**](mpcallback-data.md)
</dt> <dt>

[**MPSCAN\_DATA**](mpscan-data.md)
</dt> <dt>

[**MPSCAN\_RESOURCES**](mpscan-resources.md)
</dt> <dt>

[**MPSCAN\_TYPE**](mpscan-type.md)
</dt> </dl>

 

 





