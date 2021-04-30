---
description: Describes how up-to-date the OS on a device is.
ms.assetid: 157E241E-E8D8-41F8-9565-5C9298DCD1BE
title: UpdateAssessmentStatus enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateAssessmentStatus
api_type: 
- HeaderDef
api_location: 
- waasapitypes.h
---

# UpdateAssessmentStatus enumeration

Describes how up-to-date the OS on a device is. **UpdateAssessmentStatus** is used by the [**UpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-updateassessment) and [**OSUpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-osupdateassessment) structures, in the **assessmentForCurrent**, **assessmentForUpToDate**, and **securityStatus** members. Exactly one constant is returned.

## Syntax


```C++
typedef enum TagUpdateAssessmentStatus { 
      UpdateAssessmentStatus_Latest                    = 0,
      UpdateAssessmentStatus_NotLatestSoftRestriction  = 1,
      UpdateAssessmentStatus_NotLatestHardRestriction  = 2,
      UpdateAssessmentStatus_NotLatestEndOfSupport     = 3,
      UpdateAssessmentStatus_NotLatestServicingTrain   = 4,
      UpdateAssessmentStatus_NotLatestDeferredFeature  = 5,
      UpdateAssessmentStatus_NotLatestDeferredQuality  = 6,
      UpdateAssessmentStatus_NotLatestPausedFeature    = 7,
      UpdateAssessmentStatus_NotLatestPausedQuality    = 8,
      UpdateAssessmentStatus_NotLatestManaged          = 9,
      UpdateAssessmentStatus_NotLatestUnknown          = 10,
      UpdateAssessmentStatus_NotLatestTargetedVersion  = 11
} UpdateAssessmentStatus;
```



## Constants

<dl> <dt>

<span id="____UpdateAssessmentStatus_Latest"></span><span id="____updateassessmentstatus_latest"></span><span id="____UPDATEASSESSMENTSTATUS_LATEST"></span> **UpdateAssessmentStatus\_Latest**
</dt> <dd>

This result within **assessmentForCurrent** implies that the device is on the latest feature update and quality update available for that device. Within **assessmentForUpToDate**, this result implies that the device is on the latest quality update for the release of Windows it is running.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestSoftRestriction"></span><span id="____updateassessmentstatus_notlatestsoftrestriction"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTSOFTRESTRICTION"></span> **UpdateAssessmentStatus\_NotLatestSoftRestriction**
</dt> <dd>

The latest feature update has not been installed due to a soft restriction. When a soft restriction has been placed on an update, the update will not be automatically installed; a user must self-initiate the download within the Update UX. This status only applies to **assessmentForCurrent**.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestHardRestriction"></span><span id="____updateassessmentstatus_notlatesthardrestriction"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTHARDRESTRICTION"></span> **UpdateAssessmentStatus\_NotLatestHardRestriction**
</dt> <dd>

The latest feature update has not been installed due to a hard restriction. When a hard restriction has been placed on an update, the update is not applicable to the device. This status only applies to **assessmentForCurrent**.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestEndOfSupport"></span><span id="____updateassessmentstatus_notlatestendofsupport"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTENDOFSUPPORT"></span> **UpdateAssessmentStatus\_NotLatestEndOfSupport**
</dt> <dd>

The device is not on the latest update because the device's feature update is no longer supported by Microsoft. When Microsoft stops supporting a feature release, this status will be returned for both **assessmentForCurrent** and **assessmentForUpToDate**.

> [!Note]  
> When **UpdateAssessmentStatus\_NotLatestEndOfSupport** is returned, the assessment's **UpdateImpactLevel** is always **UpdateImpactLevel\_High**.

 

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestServicingTrain"></span><span id="____updateassessmentstatus_notlatestservicingtrain"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTSERVICINGTRAIN"></span> **UpdateAssessmentStatus\_NotLatestServicingTrain**
</dt> <dd>

The device is not on the latest feature update because the device's servicing train limits the device from updating to the latest feature update. For example: if a device is on Current Branch for Business (CBB) and a new feature update has been released for Current Branch (CB), this will be returned. This status only applies to **assessmentForCurrent**.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestDeferredFeature"></span><span id="____updateassessmentstatus_notlatestdeferredfeature"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTDEFERREDFEATURE"></span> **UpdateAssessmentStatus\_NotLatestDeferredFeature**
</dt> <dd>

The latest feature update has not been installed due to the device's Windows Update for Business Feature Update Deferral policy. Determining **daysOutOfDate** takes into account deferral policies; **daysOutOfDate** will not begin incrementing until the deferral period has expired. This status only applies to **assessmentForCurrent**.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestDeferredQuality"></span><span id="____updateassessmentstatus_notlatestdeferredquality"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTDEFERREDQUALITY"></span> **UpdateAssessmentStatus\_NotLatestDeferredQuality**
</dt> <dd>

The device is not on the latest quality update due to the device's Windows Update for Business Quality Update Deferral policy. Determining **daysOutOfDate** takes into account deferral policies; **daysOutOfDate** will not begin incrementing until the deferral period has expired.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestPausedFeature"></span><span id="____updateassessmentstatus_notlatestpausedfeature"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTPAUSEDFEATURE"></span> **UpdateAssessmentStatus\_NotLatestPausedFeature**
</dt> <dd>

The device is not on the latest feature update due to the device having paused Feature Updates. Whether a device is paused is not factored into the calculation of **daysOutOfDate**. This status only applies to **assessmentForCurrent**.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestPausedQuality"></span><span id="____updateassessmentstatus_notlatestpausedquality"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTPAUSEDQUALITY"></span> **UpdateAssessmentStatus\_NotLatestPausedQuality**
</dt> <dd>

The device is not on the latest quality update due to the device having paused Quality Updates. Whether a device is paused is not factored into the calculation of **daysOutOfDate**. **daysOutOfDate** does not factor whether a device is paused into its calculation.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestManaged"></span><span id="____updateassessmentstatus_notlatestmanaged"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTMANAGED"></span> **UpdateAssessmentStatus\_NotLatestManaged**
</dt> <dd>

The device is not on the latest update because the approval of updates is not done through Windows Update.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestUnknown"></span><span id="____updateassessmentstatus_notlatestunknown"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTUNKNOWN"></span> **UpdateAssessmentStatus\_NotLatestUnknown**
</dt> <dd>

The device is not on the latest update due to a reason that cannot be determined by the assessment.

</dd> <dt>

<span id="____UpdateAssessmentStatus_NotLatestTargetedVersion"></span><span id="____updateassessmentstatus_notlatesttargetedversion"></span><span id="____UPDATEASSESSMENTSTATUS_NOTLATESTTARGETEDVERSION"></span> **UpdateAssessmentStatus\_NotLatestTargetedVersion**
</dt> <dd>

The device is not on the latest feature update due to the device's Windows Update for Business Target Version policy. This policy is keeping the device on the targeted feature release version.

</dd> </dl>

## Remarks

This enumeration is used most often with the [**UpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-updateassessment) and [**OSUpdateAssessment**](/windows/win32/api/waasapitypes/ns-waasapitypes-osupdateassessment) structures, which are in turn used with the [**GetOSUpdateAssessment**](/windows/desktop/api/waasapi/nf-waasapi-iwaasassessor-getosupdateassessment) method for [**IWaaSAssessor**](/windows/desktop/api/waasapi/nn-waasapi-iwaasassessor).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                   |
| IDL<br/>                      | <dl> <dt>WaaSAPI.idl</dt> </dl> |



 

 




