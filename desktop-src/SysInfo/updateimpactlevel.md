---
description: Indicates a high, medium, or low impact of a device running an out-of-date OS.
ms.assetid: C7F30B63-66B0-4F37-A05B-7D366A12B640
title: UpdateImpactLevel enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateImpactLevel
api_type: 
- HeaderDef
api_location: 
- waasapitypes.h
---

# UpdateImpactLevel enumeration

Indicates a high, medium, or low impact of a device running an out-of-date OS. This enumeration is generally used by [**UpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-updateassessment) structures, which is in turn nested inside the returned [**OSUpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-osupdateassessment) from [**GetOSUpdateAssessment**](/windows/desktop/api/waasapi/nf-waasapi-iwaasassessor-getosupdateassessment).

## Syntax


```C++
typedef enum TagUpdateImpactLevel { 
      UpdateImpactLevel_None    = 0,
  UpdateImpactLevel_Low         = 1,
      UpdateImpactLevel_Medium  = 2,
  UpdateImpactLevel_High        = 3
} UpdateImpactLevel;
```



## Constants

<dl> <dt>

<span id="____UpdateImpactLevel_None"></span><span id="____updateimpactlevel_none"></span><span id="____UPDATEIMPACTLEVEL_NONE"></span> **UpdateImpactLevel\_None**
</dt> <dd>

There is no foreseeable impact to your device. This can be because the device is up-to-date, or is not up-to-date because the device is honoring its Windows Update for Business deferral periods, or is out-of-date but has not yet reached the **daysOutOfDate** threshold to reach a higher impact level.

</dd> <dt>

<span id="UpdateImpactLevel_Low"></span><span id="updateimpactlevel_low"></span><span id="UPDATEIMPACTLEVEL_LOW"></span>**UpdateImpactLevel\_Low**
</dt> <dd>

The device is not running the latest OS, but has a recent update.

</dd> <dt>

<span id="____UpdateImpactLevel_Medium"></span><span id="____updateimpactlevel_medium"></span><span id="____UPDATEIMPACTLEVEL_MEDIUM"></span> **UpdateImpactLevel\_Medium**
</dt> <dd>

The device is running the latest OS, but has a moderately recent update.

</dd> <dt>

<span id="UpdateImpactLevel_High"></span><span id="updateimpactlevel_high"></span><span id="UPDATEIMPACTLEVEL_HIGH"></span>**UpdateImpactLevel\_High**
</dt> <dd>

The device has been out-of-date for a long time. This device may have security vulnerabilities and may be missing important fixes that make Windows run better. When a device is running a version of Windows that is no longer supported, **UpdateImpactLevel\_High** is always returned.

</dd> </dl>

## Remarks

When [**GetOSUpdateAssessment**](/windows/desktop/api/waasapi/nf-waasapi-iwaasassessor-getosupdateassessment) is called, an [**OSUpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-osupdateassessment) structure is returned. Within the structure there is an **assessmentForCurrent** and **assessmentForUpToDate**. Both of these are [**UpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-updateassessment) structures. Both members have an **UpdateImpactLevel** enumeration, which indicates a high, medium, low or no impact for a device running an out-of-date OS. The These levels are determined by the value of **daysOutOfDate**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                   |
| IDL<br/>                      | <dl> <dt>WaaSAPI.idl</dt> </dl> |



 

 




