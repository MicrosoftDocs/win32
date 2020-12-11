---
title: MPTHREAT_INFO structure (MpClient.h)
description: Contains information about a threat.
ms.assetid: ED2A0BDB-0E7C-479D-ADA1-95B9A259F57E
keywords:
- MPTHREAT_INFO structure Legacy Windows Environment Features
- PMPTHREAT_INFO structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_INFO
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_INFO structure

Contains information about a threat.

## Syntax


```C++
typedef struct tagMPTHREAT_INFO {
  MPTHREAT_ID           ThreatID;
  GUID                  DetectionID;
  MP_MIDL_STRING LPWSTR Name;
  MPTHREAT_TYPE         ThreatType;
  MPTHREAT_SEVERITY     ThreatCriticality;
  MPTHREAT_CATEGORY     ThreatCategory;
  DWORD                 ThreatShortDescriptionID;
  DWORD                 ThreatAdviseDescriptionID;
  MPTHREAT_STATUS       ThreatStatus;
  DWORD                 SuggestedActionCount;
  MPTHREAT_ACTION       SuggestedActionArray[MP_MAX_SUGGESTIONS];
  DWORD                 ResourceCount;
  PMPRESOURCE_INFO      *ResourceList[ResourceCount];
  ULARGE_INTEGER        ThreatStatusTime;
  HRESULT               ThreatStatusCode;
  MPTHREAT_DETECTION    ThreatDetection;
  GUID                  QuarantineGuid;
  MPEXECUTION_STATUS    ExecutionStatus;
  union {
    PMPTHREAT_INFOEX_UNUSED   pKnownBad;
    PMPTHREAT_INFOEX_BEHAVIOR pBehavior;
    PMPTHREAT_INFOEX_UNUSED   pUnknown;
    PMPTHREAT_INFOEX_UNUSED   pKnownGood;
    PMPTHREAT_INFOEX_NIS      pNis;
  } Data;
  MPDETECTION_STATE     State;
  MP_MIDL_STRING LPWSTR DetectionUser;
  MPSOURCE              DetectionSource;
  MP_MIDL_STRING LPWSTR ProcessName;
  MPDETECTION_ORIGIN    DetectionOrigin;
  DWORD                 reserved1;
  ULARGE_INTEGER        DetectionTime;
  MPEXECUTION_STATUS    PreExecutionStatus;
  ULARGE_INTEGER        RemediationTime;
  MPEXECUTION_STATUS    PostExecutionStatus;
  BOOL                  CriticalFailure;
  DWORD                 NonCriticalReason;
  MP_MIDL_STRING LPWSTR RemediationUser;
  DWORD                 RemediationResourceCount;
  PMPRESOURCE_INFO      RemediationResourceList[RemediationResourceCount];
  BOOL                  FailureResolved;
  MPRESOLVED_REASON     ResolvedReason;
  DWORD                 AdditionalActions;
  DWORD                 ResolvedActions;
  DWORD                 dwThreatStatusFlag;
} MPTHREAT_INFO, *PMPTHREAT_INFO;
```



## Members

<dl> <dt>

**ThreatID**
</dt> <dd>

Type: **MPTHREAT\_ID**

</dd> <dd>

Threat identifier. Upper bit is set to identify antivirus-related threats.

</dd> <dt>

**DetectionID**
</dt> <dd>

Type: **GUID**

</dd> <dd>

Detection ID.

</dd> <dt>

**Name**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Threat name.

</dd> <dt>

**ThreatType**
</dt> <dd>

Type: **[**MPTHREAT\_TYPE**](mpthreat-type.md)**

</dd> <dd>

Threat type. Used to differentiate among different threat types such as known bad, unknown, or known good. See [**MPTHREAT\_TYPE**](mpthreat-type.md).

</dd> <dt>

**ThreatCriticality**
</dt> <dd>

Type: **[**MPTHREAT\_SEVERITY**](mpthreat-severity.md)**

</dd> <dd>

Threat criticality. See [**MPTHREAT\_SEVERITY**](mpthreat-severity.md).

</dd> <dt>

**ThreatCategory**
</dt> <dd>

Type: **[**MPTHREAT\_CATEGORY**](mpthreat-category.md)**

</dd> <dd>

Threat category, such as a trojan or a keylogger. See [**MPTHREAT\_CATEGORY**](mpthreat-category.md).

</dd> <dt>

**ThreatShortDescriptionID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Threat short description ID.

</dd> <dt>

**ThreatAdviseDescriptionID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Threat advise description ID.

</dd> <dt>

**ThreatStatus**
</dt> <dd>

Type: **[**MPTHREAT\_STATUS**](mpthreat-status.md)**

</dd> <dd>

Threat status such as detected, cleaned, or quarantined. See [**MPTHREAT\_STATUS**](mpthreat-status.md).

</dd> <dt>

**SuggestedActionCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Count of suggested actions in **SuggestedActionArray**.

</dd> <dt>

**SuggestedActionArray**
</dt> <dd>

Type: **[**MPTHREAT\_ACTION**](mpthreat-action.md)\[MP\_MAX\_SUGGESTIONS\]**

</dd> <dd>

Array of suggested actions. See [**MPTHREAT\_ACTION**](mpthreat-action.md).

</dd> <dt>

**ResourceCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Count of resources in **ResourceList**.

</dd> <dt>

**ResourceList**
</dt> <dd>

Type: **PMPRESOURCE\_INFO\***

</dd> <dd>

List of resources identified with the threat. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> <dt>

**ThreatStatusTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Time when threat status last changed.

</dd> <dt>

**ThreatStatusCode**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Status code associated with the threat status.

</dd> <dt>

**ThreatDetection**
</dt> <dd>

Type: **[**MPTHREAT\_DETECTION**](mpthreat-detection.md)**

</dd> <dd>

Threat detection type, such as concrete, suspicious, or generic. See [**MPTHREAT\_DETECTION**](mpthreat-detection.md).

</dd> <dt>

**QuarantineGuid**
</dt> <dd>

Type: **GUID**

</dd> <dd>

Quarantine guid.

</dd> <dt>

**ExecutionStatus**
</dt> <dd>

Type: **[**MPEXECUTION\_STATUS**](mpexecution-status.md)**

</dd> <dd>

Execution status of the threat, such as not known, blocked, or active. See [**MPEXECUTION\_STATUS**](mpexecution-status.md).

</dd> <dt>

**Data**
</dt> <dd>

Extra information. The pointer to the appropriate structure depends on the value of **ThreatType**.

<dl> <dt>

**pKnownBad**
</dt> <dd>

Type: **PMPTHREAT\_INFOEX\_UNUSED**

</dd> <dd>

When **ThreatType** == **MPTHREAT\_TYPE\_KNOWNBAD**. See [**MPTHREAT\_INFOEX\_UNUSED**](mpthreat-infoex-unused.md).

</dd> <dt>

**pBehavior**
</dt> <dd>

Type: **PMPTHREAT\_INFOEX\_BEHAVIOR**

</dd> <dd>

When **ThreatType** == **MPTHREAT\_TYPE\_BEHAVIOR**. See [**MPTHREAT\_INFOEX\_BEHAVIOR**](mpthreat-infoex-behavior.md).

</dd> <dt>

**pUnknown**
</dt> <dd>

Type: **PMPTHREAT\_INFOEX\_UNUSED**

</dd> <dd>

When **ThreatType** == **MPTHREAT\_TYPE\_UNKNOWN**. See [**MPTHREAT\_INFOEX\_UNUSED**](mpthreat-infoex-unused.md).

</dd> <dt>

**pKnownGood**
</dt> <dd>

Type: **PMPTHREAT\_INFOEX\_UNUSED**

</dd> <dd>

When **ThreatType** == MPTHREAT\_TYPE\_KNOWNGOOD. See [**MPTHREAT\_INFOEX\_UNUSED**](mpthreat-infoex-unused.md).

</dd> <dt>

**pNis**
</dt> <dd>

Type: **PMPTHREAT\_INFOEX\_NIS**

</dd> <dd>

When **ThreatType** == **MPTHREAT\_TYPE\_NIS**. See [**MPTHREAT\_INFOEX\_NIS**](mpthreat-infoex-nis.md).

</dd> </dl> </dd> <dt>

**State**
</dt> <dd>

Type: **[**MPDETECTION\_STATE**](mpdetection-state.md)**

</dd> <dd>

The current state of the detection. See [**MPDETECTION\_STATE**](mpdetection-state.md).

</dd> <dt>

**DetectionUser**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

The user associated with the detection, in the format "domain/user".

</dd> <dt>

**DetectionSource**
</dt> <dd>

Type: **[**MPSOURCE**](mpsource.md)**

</dd> <dd>

The source of the detection. See [**MPSOURCE**](mpsource.md).

</dd> <dt>

**ProcessName**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Process name associated with the detection.

</dd> <dt>

**DetectionOrigin**
</dt> <dd>

Type: **[**MPDETECTION\_ORIGIN**](mpdetection-origin.md)**

</dd> <dd>

The origin of the detection, such as local or network. See [**MPDETECTION\_ORIGIN**](mpdetection-origin.md).

</dd> <dt>

**reserved1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved metadata about the detection.

</dd> <dt>

**DetectionTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

The time of the initial detection.

</dd> <dt>

**PreExecutionStatus**
</dt> <dd>

Type: **[**MPEXECUTION\_STATUS**](mpexecution-status.md)**

</dd> <dd>

Execution status right before remediation. See [**MPEXECUTION\_STATUS**](mpexecution-status.md).

</dd> <dt>

**RemediationTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

The time remediation occured.

</dd> <dt>

**PostExecutionStatus**
</dt> <dd>

Type: **[**MPEXECUTION\_STATUS**](mpexecution-status.md)**

</dd> <dd>

Execution status after remediation. See [**MPEXECUTION\_STATUS**](mpexecution-status.md).

</dd> <dt>

**CriticalFailure**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

True if the remediation failure was critical.

</dd> <dt>

**NonCriticalReason**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The reason the remediation failure is not critical. This is not guaranteed to be supported in the future.

</dd> <dt>

**RemediationUser**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

User that requested the remediation, in the format "domain/user".

</dd> <dt>

**RemediationResourceCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Count of resources in **RemediationResourceList**.

</dd> <dt>

**RemediationResourceList**
</dt> <dd>

Type: **PMPRESOURCE\_INFO\[RemediationResourceCount\]**

</dd> <dd>

List of resources that failed during remediation. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> <dt>

**FailureResolved**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

True if remediation failure been resolved. This will move the bucket to either complete or an additional action.

</dd> <dt>

**ResolvedReason**
</dt> <dd>

Type: **[**MPRESOLVED\_REASON**](mpresolved-reason.md)**

</dd> <dd>

Reason for remediation failure being resolved. This is the reason the detection moved from failed to additional action or finished. See [**MPRESOLVED\_REASON**](mpresolved-reason.md).

</dd> <dt>

**AdditionalActions**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Are additional actions required.

</dd> <dt>

**ResolvedActions**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Any additional actions that have been performed.

</dd> <dt>

**dwThreatStatusFlag**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Additonal information about the threat detection.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MpFreeMemory**](mpfreememory.md)
</dt> <dt>

[**MpThreatEnumerate**](mpthreatenumerate.md)
</dt> <dt>

[**MpThreatQuery**](mpthreatquery.md)
</dt> <dt>

[**MPDETECTION\_ORIGIN**](mpdetection-origin.md)
</dt> <dt>

[**MPDETECTION\_STATE**](mpdetection-state.md)
</dt> <dt>

[**MPEXECUTION\_STATUS**](mpexecution-status.md)
</dt> <dt>

[**MPRESOLVED\_REASON**](mpresolved-reason.md)
</dt> <dt>

[**MPRESOURCE\_INFO**](mpresource-info.md)
</dt> <dt>

[**MPSOURCE**](mpsource.md)
</dt> <dt>

[**MPTHREAT\_ACTION**](mpthreat-action.md)
</dt> <dt>

[**MPTHREAT\_CATEGORY**](mpthreat-category.md)
</dt> <dt>

[**MPTHREAT\_DETECTION**](mpthreat-detection.md)
</dt> <dt>

[**MPTHREAT\_INFOEX\_BEHAVIOR**](mpthreat-infoex-behavior.md)
</dt> <dt>

[**MPTHREAT\_INFOEX\_NIS**](mpthreat-infoex-nis.md)
</dt> <dt>

[**MPTHREAT\_INFOEX\_UNUSED**](mpthreat-infoex-unused.md)
</dt> <dt>

[**MPTHREAT\_SEVERITY**](mpthreat-severity.md)
</dt> <dt>

[**MPTHREAT\_STATUS**](mpthreat-status.md)
</dt> <dt>

[**MPTHREAT\_TYPE**](mpthreat-type.md)
</dt> </dl>

 

 





