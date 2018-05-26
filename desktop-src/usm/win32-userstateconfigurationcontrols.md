---
title: Win32\_UserStateConfigurationControls class
description: Contains properties that control the user state configuration for a computer. The property value settings for this class determine whether Group Policy or WMI should be the configuration mechanism for user state components.
ms.assetid: 9428e8d4-72a7-4661-8e1a-b2b6712d2c60
keywords:
- Win32_UserStateConfigurationControls class User State Manageability API
- Win32_UserStateConfigurationControls class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_UserStateConfigurationControls
- Win32_UserStateConfigurationControls.FolderRedirection
- Win32_UserStateConfigurationControls.RoamingUserProfile
- Win32_UserStateConfigurationControls.OfflineFiles
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

# Win32\_UserStateConfigurationControls class

Contains properties that control the user state configuration for a computer. The property value settings for this class determine whether Group Policy or WMI should be the configuration mechanism for user state components.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_UserStateConfigurationControls
{
  uint8 FolderRedirection;
  uint8 RoamingUserProfile;
  uint8 OfflineFiles;
};
```

## Members

The **Win32\_UserStateConfigurationControls** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_UserStateConfigurationControls** class has these properties.

<dl> <dt>

**FolderRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the computer's folder redirection feature settings are configured by using the User State Manageability WMI classes or by using Group Policy.

One of the following values.

<dl> <dt>

<span id="GroupPolicy"></span><span id="grouppolicy"></span><span id="GROUPPOLICY"></span>**GroupPolicy** (0)
</dt> <dt>

<span id="WMI"></span><span id="wmi"></span>**WMI** (1)
</dt> </dl>

</dd> <dt>

**OfflineFiles**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the computer's offline files feature settings are configured by using the User State Manageability WMI classes or by using Group Policy.

One of the following values.

<dl> <dt>

<span id="GroupPolicy"></span><span id="grouppolicy"></span><span id="GROUPPOLICY"></span>**GroupPolicy** (0)
</dt> <dt>

<span id="WMI"></span><span id="wmi"></span>**WMI** (1)
</dt> </dl>

</dd> <dt>

**RoamingUserProfile**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the computer's roaming user profile feature settings are configured by using the User State Manageability WMI classes or by using Group Policy.

One of the following values.

<dl> <dt>

<span id="GroupPolicy"></span><span id="grouppolicy"></span><span id="GROUPPOLICY"></span>**GroupPolicy** (0)
</dt> <dt>

<span id="WMI"></span><span id="wmi"></span>**WMI** (1)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                              |
| MOF<br/>                      | <dl> <dt>UserStateWmiProvider.mof</dt> </dl> |



 

 





