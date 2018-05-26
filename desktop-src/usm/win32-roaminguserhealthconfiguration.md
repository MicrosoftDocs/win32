---
title: Win32\_RoamingUserHealthConfiguration class
description: Represents health configuration properties for all roaming user profiles on a computer.
ms.assetid: ab772e16-2d08-41a0-84de-7cca9bc7f47d
keywords:
- Win32_RoamingUserHealthConfiguration class User State Manageability API
- Win32_RoamingUserHealthConfiguration class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_RoamingUserHealthConfiguration
- Win32_RoamingUserHealthConfiguration.HealthStatusForTempProfiles
- Win32_RoamingUserHealthConfiguration.LastProfileUploadIntervalCautionInHours
- Win32_RoamingUserHealthConfiguration.LastProfileDownloadIntervalCautionInHours
- Win32_RoamingUserHealthConfiguration.LastProfileUploadIntervalUnhealthyInHours
- Win32_RoamingUserHealthConfiguration.LastProfileDownloadIntervalUnhealthyInHours
api_location:
- Root\CIMv2
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_RoamingUserHealthConfiguration class

Represents health configuration properties for all roaming user profiles on a computer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RoamingUserHealthConfiguration
{
  uint8  HealthStatusForTempProfiles;
  uint16 LastProfileUploadIntervalCautionInHours;
  uint16 LastProfileDownloadIntervalCautionInHours;
  uint16 LastProfileUploadIntervalUnhealthyInHours;
  uint16 LastProfileDownloadIntervalUnhealthyInHours;
};
```

## Members

The **Win32\_RoamingUserHealthConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RoamingUserHealthConfiguration** class has these properties.

<dl> <dt>

**HealthStatusForTempProfiles**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Values** (Healthy, Unhealthy, Caution), **ValueMap** (0, 1, 2)
</dt> </dl>

Indicates how the [**Win32\_UserProfile**](win32-userprofile.md) class's **HealthStatus** property should reflect the use of temporary profiles.

</dd> <dt>

**LastProfileDownloadIntervalCautionInHours**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This is the time threshold, in hours, after which the profile health is reported as **Caution** when the profile has not been downloaded yet.

If the last time the profile was downloaded plus this threshold is greater than the current time, the [**Win32\_UserProfile**](win32-userprofile.md) class's **HealthStatus** property is set to **Caution**.

</dd> <dt>

**LastProfileDownloadIntervalUnhealthyInHours**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This is the time threshold, in hours, after which the profile health is reported as **Unhealthy** when the profile has not been downloaded yet.

The value of this property should be greater than the value of the **LastProfileDownloadIntervalCautionInHours** property.

If the last time the profile was downloaded plus this threshold is greater than the current time, the [**Win32\_UserProfile**](win32-userprofile.md) class's **HealthStatus** property is set to **Unhealthy**.

</dd> <dt>

**LastProfileUploadIntervalCautionInHours**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This is the time threshold, in hours, after which the profile health is reported as **Caution** when the profile has not been uploaded yet.

If the last time the profile was uploaded plus this threshold is greater than the current time, the [**Win32\_UserProfile**](win32-userprofile.md) class's **HealthStatus** property is set to **Caution**.

</dd> <dt>

**LastProfileUploadIntervalUnhealthyInHours**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This is the time threshold, in hours, after which the profile health is reported as **Unhealthy** when the profile has not been uploaded yet.

The value of this property should be greater than the value of the **LastProfileUploadIntervalCautionInHours** property.

If the last time the profile was uploaded plus this threshold is greater than the current time, the [**Win32\_UserProfile**](win32-userprofile.md) class's **HealthStatus** property is set to **Unhealthy**.

</dd> </dl>

## Remarks

This class defines the thresholds used to calculate the Roaming User Profile Health. If the last time the profile was uploaded or downloaded plus the threshold is greater than the current time, then the health status is set accordingly.

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



 

 





