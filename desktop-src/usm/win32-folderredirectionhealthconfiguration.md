---
title: Win32\_FolderRedirectionHealthConfiguration class
description: Represents the health configuration properties for a known folder that is being redirected.
ms.assetid: cde52493-4f84-4ce4-9432-41a01879d60a
keywords:
- Win32_FolderRedirectionHealthConfiguration class User State Manageability API
- Win32_FolderRedirectionHealthConfiguration class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_FolderRedirectionHealthConfiguration
- Win32_FolderRedirectionHealthConfiguration.LastSyncDurationCautionInHours
- Win32_FolderRedirectionHealthConfiguration.LastSyncDurationUnhealthyInHours
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

# Win32\_FolderRedirectionHealthConfiguration class

Represents the health configuration properties for a known folder that is being redirected.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_FolderRedirectionHealthConfiguration
{
  uint32 LastSyncDurationCautionInHours;
  uint32 LastSyncDurationUnhealthyInHours;
};
```

## Members

The **Win32\_FolderRedirectionHealthConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_FolderRedirectionHealthConfiguration** class has these properties.

<dl> <dt>

**LastSyncDurationCautionInHours**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Cautious threshold, in hours. If the number of hours since the last attempted synchronization is greater than or equal to this threshold, the **HealthStatus** property of the [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) class is set to **Caution**.

The default value for this property is 240 hours (10 days).

</dd> <dt>

**LastSyncDurationUnhealthyInHours**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Unhealthy threshold, in hours. If the number of hours since the last attempted synchronization is greater than or equal to this threshold, the **HealthStatus** property of the [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) class is set to **Unhealthy**.

The default value for this property is 480 hours (20 days).

</dd> </dl>

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_FolderRedirection**](win32-folderredirection.md)
</dt> <dt>

[**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md)
</dt> <dt>

[**Win32\_FolderRedirectionUserConfiguration**](win32-folderredirectionuserconfiguration.md)
</dt> </dl>

 

 





