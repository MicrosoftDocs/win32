---
title: Win32\_RoamingProfileBackgroundUploadParams class
description: Represents a roaming profile background upload operation.
ms.assetid: 3cb2b0ed-708d-4df4-96b0-48ab21e2e9eb
keywords:
- Win32_RoamingProfileBackgroundUploadParams class User State Manageability API
- Win32_RoamingProfileBackgroundUploadParams class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_RoamingProfileBackgroundUploadParams
- Win32_RoamingProfileBackgroundUploadParams.SchedulingMethod
- Win32_RoamingProfileBackgroundUploadParams.Interval
- Win32_RoamingProfileBackgroundUploadParams.Time
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_RoamingProfileBackgroundUploadParams class

Represents a roaming profile background upload operation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RoamingProfileBackgroundUploadParams
{
  uint8  SchedulingMethod;
  uint16 Interval;
  uint16 Time;
};
```

## Members

The **Win32\_RoamingProfileBackgroundUploadParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RoamingProfileBackgroundUploadParams** class has these properties.

<dl> <dt>

**Interval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (720)
</dt> </dl>

The time interval, in hours.

</dd> <dt>

**SchedulingMethod**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates when a background upload should be performed. One of the following values can be specified.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <span id="SpecificTime"></span><span id="specifictime"></span><span id="SPECIFICTIME"></span><dl> <dt>**SpecificTime**</dt> <dt>1</dt> </dl> | Perform the background upload at the time of day specified in the **Time** property.<br/>  |
| <span id="SetInterval"></span><span id="setinterval"></span><span id="SETINTERVAL"></span><dl> <dt>**SetInterval**</dt> <dt>2</dt> </dl>     | Perform the background upload at the interval specified in the **Interval** property.<br/> |



 

</dd> <dt>

**Time**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (23)
</dt> </dl>

The time of day. Must be an integer value from 0 to 23.

</dd> </dl>

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



 

 





