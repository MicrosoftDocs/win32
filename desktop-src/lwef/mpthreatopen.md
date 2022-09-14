---
title: MpThreatOpen function (MpClient.h)
description: Returns an enumeration handle for the purpose of retrieving threats.
ms.assetid: E1178F0C-E9C0-4532-AE9B-452770600DF2
keywords:
- MpThreatOpen function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpThreatOpen
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpThreatOpen function

Returns an enumeration handle for the purpose of retrieving threats. This function can be used to open threats detected by a specific scan, all the active threats in the system, the history of threat disinfection, or all the threats present in the signature database.

## Syntax


```C++
HRESULT WINAPI MpThreatOpen(
  _In_  MPHANDLE        hScanHandle,
  _In_  MPTHREAT_SOURCE ThreatSource,
  _In_  MPTHREAT_TYPE   ThreatType,
  _Out_ PMPHANDLE       phThreatEnumHandle
);
```



## Parameters

<dl> <dt>

*hScanHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Can be a handle to a completed scan operation, returned by the [**MpScanStart**](mpscanstart.md) function. Alternately, this parameter can be set to the malware protection manager interface handle returned by [**MpManagerOpen**](mpmanageropen.md) to enumerate all active threats in the system, the history of threat disinfection, or threats from signature database.

</dd> <dt>

*ThreatSource* \[in\]
</dt> <dd>

Type: **MPTHREAT\_SOURCE**

Used to control the source of threat enumeration. The possible values for this parameter are:



| Value                                                                                                                                                                                                 | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="MPTHREAT_SOURCE_SCAN"></span><span id="mpthreat_source_scan"></span><dl> <dt>**MPTHREAT\_SOURCE\_SCAN**</dt> </dl>                   | Threats that are associated with the specific scan handle.<br/>                                              |
| <span id="MPTHREAT_SOURCE_ACTIVE"></span><span id="mpthreat_source_active"></span><dl> <dt>**MPTHREAT\_SOURCE\_ACTIVE**</dt> </dl>             | Threats that are currently active in the system.<br/>                                                        |
| <span id="MPTHREAT_SOURCE_HISTORY"></span><span id="mpthreat_source_history"></span><dl> <dt>**MPTHREAT\_SOURCE\_HISTORY**</dt> </dl>          | Threats that are acted upon and preserved as a history.<br/>                                                 |
| <span id="MPTHREAT_SOURCE_QUARANTINE"></span><span id="mpthreat_source_quarantine"></span><dl> <dt>**MPTHREAT\_SOURCE\_QUARANTINE**</dt> </dl> | Threats that are quarantined.<br/>                                                                           |
| <span id="MPTHREAT_SOURCE_SIGNATURE"></span><span id="mpthreat_source_signature"></span><dl> <dt>**MPTHREAT\_SOURCE\_SIGNATURE**</dt> </dl>    | Threats that are possible to detect with the current signature database.<br/>                                |
| <span id="MPTHREAT_SOURCE_STATE"></span><span id="mpthreat_source_state"></span><dl> <dt>**MPTHREAT\_SOURCE\_STATE**</dt> </dl>                | Threats that have been acted upon recently. ("Recently" is defined by a configurable internal setting.)<br/> |



 

</dd> <dt>

*ThreatType* \[in\]
</dt> <dd>

Type: **MPTHREAT\_TYPE**

Used to filter enumerated threats based on the detection type. The possible values for this parameter are:



| Value                                                                                                                                                                                           | Meaning                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <span id="MPTHREAT_TYPE_KNOWNBAD"></span><span id="mpthreat_type_knownbad"></span><dl> <dt>**MPTHREAT\_TYPE\_KNOWNBAD**</dt> </dl>       | Detection is performed based on a specific signature, emulation, or other threat detection method.<br/> |
| <span id="MPTHREAT_TYPE_SUSPICIOUS"></span><span id="mpthreat_type_suspicious"></span><dl> <dt>**MPTHREAT\_TYPE\_SUSPICIOUS**</dt> </dl> | Detection is performed based on behavior monitoring.<br/>                                               |
| <span id="MPTHREAT_TYPE_UNKNOWN"></span><span id="mpthreat_type_unknown"></span><dl> <dt>**MPTHREAT\_TYPE\_UNKNOWN**</dt> </dl>          | Detection is performed based on unknown threats (unclassified).<br/>                                    |
| <span id="MPTHREAT_TYPE_KNOWNGOOD"></span><span id="mpthreat_type_knowngood"></span><dl> <dt>**MPTHREAT\_TYPE\_KNOWNGOOD**</dt> </dl>    | Detection is performed based on known safe threats.<br/>                                                |
| <span id="MPTHREAT_TYPE_NIS"></span><span id="mpthreat_type_nis"></span><dl> <dt>**MPTHREAT\_TYPE\_NIS**</dt> </dl>                      | Detection is performed based on NIS threats.<br/>                                                       |



 

</dd> <dt>

*phThreatEnumHandle* \[out\]
</dt> <dd>

Type: **PMPHANDLE**

Returned threat enumeration handle which identifies the enumeration context. This handle can be used to enumerate threat information using [**MpThreatEnumerate**](mpthreatenumerate.md). The handle must be closed with the [**MpHandleClose**](mphandleclose.md) function.

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

[**MpScanStart**](mpscanstart.md)
</dt> <dt>

[**MpThreatEnumerate**](mpthreatenumerate.md)
</dt> </dl>

 

 





