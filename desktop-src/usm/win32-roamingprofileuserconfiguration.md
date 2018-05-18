---
title: Win32\_RoamingProfileUserConfiguration class
description: Represents a roaming profile user configuration.
ms.assetid: 'a78056d2-d916-4f36-8b7a-1de8353a6e14'
keywords: ["Win32_RoamingProfileUserConfiguration class User State Manageability API", "Win32_RoamingProfileUserConfiguration class User State Manageability API , described"]
topic_type:
- apiref
api_name:
- Win32_RoamingProfileUserConfiguration
- Win32_RoamingProfileUserConfiguration.ExcludedProfileDirs
- Win32_RoamingProfileUserConfiguration.DirectoriesToSyncAtLogonLogoff
- Win32_RoamingProfileUserConfiguration.IsEffective
api_location:
- Root\CIMv2
api_type:
- Schema
---

# Win32\_RoamingProfileUserConfiguration class

Represents a roaming profile user configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RoamingProfileUserConfiguration
{
  string  ExcludedProfileDirs[];
  string  DirectoriesToSyncAtLogonLogoff[];
  boolean IsEffective;
};
```

## Members

The **Win32\_RoamingProfileUserConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RoamingProfileUserConfiguration** class has these properties.

<dl> <dt>

**DirectoriesToSyncAtLogonLogoff**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing network directories to synchronize at when the user logs on to or off of a local computer.

</dd> <dt>

**ExcludedProfileDirs**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing directories to exclude from the roaming profile.

</dd> <dt>

**IsEffective**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the configuration settings are in effect.

</dd> </dl>

## Remarks

This class requires a context object to be passed as the *pCtx* parameter to the [**IWbemServices::GetObject**](https://msdn.microsoft.com/library/aa392109) method. This context object has the following properties, which should be set to the following values:



| Property Name                                        | Type     | Specify This Value                                                                                                                                                                                                                 |
|------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PolicyPlatformContext\_PrincipalContext\_Type        | VT\_BSTR | "PolicyPlatform\_UserContext"                                                                                                                                                                                                      |
| PolicyPlatformContext\_PrincipalContext\_Id          | VT\_BSTR | The user's SID in SDDL format                                                                                                                                                                                                      |
| PolicyPlatformContext\_PrincipalContext\_UserSession | VT\_I4   | The identifier of a Windows session to which the user is interactively logged on. It is possible that there are multiple sessions to which the user is logged on interactively. The MPP will pass the id of one of these sessions. |
| PolicyPlatformContext\_PrincipalContext\_Flags       | VT\_I4   | This property is reserved for future use. Set it to zero.                                                                                                                                                                          |
| PolicyPlatformContext\_PrincipalContext\_ProcessId   | VT\_I4   | The process identifier of the process that owns the user's impersonation token                                                                                                                                                     |
| PolicyPlatformContext\_PrincipalContext\_UserToken   | VT\_I8   | The user's impersonation token                                                                                                                                                                                                     |



 

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



 

 





