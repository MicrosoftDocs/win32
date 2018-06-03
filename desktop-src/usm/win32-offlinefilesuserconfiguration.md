---
title: Win32\_OfflineFilesUserConfiguration class
description: Represents the user's offline files configuration properties.
ms.assetid: 60283f0a-7c48-40a0-afa4-2b0b4e88c4af
keywords:
- Win32_OfflineFilesUserConfiguration class User State Manageability API
- Win32_OfflineFilesUserConfiguration class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_OfflineFilesUserConfiguration
- Win32_OfflineFilesUserConfiguration.AssignedOfflineFiles
- Win32_OfflineFilesUserConfiguration.WorkOfflineButtonRemoved
- Win32_OfflineFilesUserConfiguration.MakeAvailableOfflineButtonRemoved
- Win32_OfflineFilesUserConfiguration.IsEffective
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

# Win32\_OfflineFilesUserConfiguration class

Represents the user's offline files configuration properties.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_OfflineFilesUserConfiguration
{
  string  AssignedOfflineFiles[];
  boolean WorkOfflineButtonRemoved;
  boolean MakeAvailableOfflineButtonRemoved;
  boolean IsEffective;
};
```

## Members

The **Win32\_OfflineFilesUserConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesUserConfiguration** class has these properties.

<dl> <dt>

**AssignedOfflineFiles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing administratively assigned offline files. Each string contains a file path. The file path should be no longer than **MAX\_PATH** characters. The array size is not fixed; the caller can specify as many file paths as needed.

</dd> <dt>

**IsEffective**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the configuration settings are in effect.

</dd> <dt>

**MakeAvailableOfflineButtonRemoved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the **Make Available Offline** button is removed.

</dd> <dt>

**WorkOfflineButtonRemoved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the **Work Offline** button is removed.

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



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                              |
| MOF<br/>                      | <dl> <dt>OfflineFilesConfigurationWmiProvider.mof</dt> </dl> |



 

 





