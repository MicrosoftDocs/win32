---
title: CreateGoalSettings method of the CIM\_AllocationCapabilities class
description: Creates a set of supported SettingData elements, from two sets of SettingData elements, provided by the caller.
ms.assetid: dcab4639-3955-40c9-8346-852b27a166ca
keywords:
- CreateGoalSettings method Hyper-V
- CreateGoalSettings method Hyper-V , CIM_AllocationCapabilities class
- CIM_AllocationCapabilities class Hyper-V , CreateGoalSettings method
topic_type:
- apiref
api_name:
- CIM_AllocationCapabilities.CreateGoalSettings
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateGoalSettings method of the CIM\_AllocationCapabilities class

Creates a set of supported SettingData elements, from two sets of SettingData elements, provided by the caller.

## Syntax


```mof
uint16 CreateGoalSettings(
  [in]      string TemplateGoalSettings[],
  [in, out] string SupportedGoalSettings[]
);
```



## Parameters

<dl> <dt>

*TemplateGoalSettings* \[in\]
</dt> <dd>

If provided, TemplateGoalSettings are elements of class CIM\_SettingData, or a derived class, that is used as the template to be matched. . At most, one instance of each SettingData subclass may be supplied. All SettingData instances provided by this property are interpreted as a set, relative to this Capabilities instance. SettingData instances that are not relevant to this instance are ignored. If not provided, it shall be set to NULL. In that case, a SettingData instance representing the default settings of the associated ManagedElement is used.

</dd> <dt>

*SupportedGoalSettings* \[in, out\]
</dt> <dd>

SupportedGoalSettings are elements of class CIM\_SettingData, or a derived class. At most, one instance of each SettingData subclass may be supplied. All SettingData instances provided by this property are interpreted as a set, relative to this Capabilities instance. To enable a client to provide additional information toward achieving the TemplateGoalSettings, an input set of SettingData instances may be provided. If not provided, this property shall be set to NULL on input.Note that when provided, what property values are changed, and how, is implementation dependent and may be the subject of other standards. If provided, the input SettingData instances must be ones that the implementation is able to support relative to the ManagedElement associated via ElementCapabilities. Typically, the input SettingData instances are created by a previous instantiation of CreateGoalSettings. If the input SupportedGoalSettings is not supported by the implementation, then an "Invalid Parameter" (5) error is returned by this call. In this case, a corresponding CIM\_ERROR should also be returned. On output, this property is used to return the best supported match to the TemplateGoalSettings. If the output SupportedGoalSettings matches the input SupportedGoalSettings, then the implementation is unable to improve further toward meeting the TemplateGoalSettings.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Alternative Proposed** (6)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Remarks

CreateGoal should be used when the SettingData instances that represents the goal will not persist beyond the execution of the client and where those instances are not intended to be shared with other, non-cooperating clients. Both TemplateGoalSettings and SupportedGoalSettings are represented as strings containing EmbeddedInstances of a CIM\_SettingData subclass. These embedded instances do not exist in the infrastructure supporting this method but are maintained by the caller/client. This method should return CIM\_Error(s) representing that a single named property of a setting (or other) parameter (either reference or embedded object) has an invalid value or that an invalid combination of named properties of a setting (or other) parameter (either reference or embedded object) has been requested.

If the input TemplateGoalSettings is NULL or the empty string, this method returns a default SettingData element that is supported by this Capabilities element. If the TemplateGoalSettings specifies values that cannot be supported, this method shall return an appropriate CIM\_Error and should return a best match for a SupportedGoalSettings. The client proposes a goal using the TemplateGoalSettings parameter and gets back Success if the TemplateGoalSettings is exactly supportable. It gets back "Alternative Proposed" if the output SupportedGoalSettings represents a supported alternative. This alternative should be a best match, as defined by the implementation.

If the implementation is conformant to a RegisteredProfile, then that profile may specify the algorithms used to determine best match. A client may compare the returned value of each property against the requested value to determine if it is left unchanged, degraded or upgraded. Otherwise, if the TemplateGoalSettings is not applicable an "Invalid Parameter" error is returned. When a mutually acceptable SupportedGoalSettings has been achieved, the client may use the contained SettingData instances as input to methods for creating a new object or modifying an existing object. Also the embedded SettingData instances returned in the SupportedGoalSettings may be instantiated via CreateInstance, either by a client or as a side-effect of the execution of an extrinsic method for which the returned SupportedGoalSettings is passed as an embedded instance.

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dt>

[**CIM\_AllocationCapabilities**](cim-allocationcapabilities.md)
</dt> </dl>

 

 





