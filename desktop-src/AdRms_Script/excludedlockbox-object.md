---
Description: 'Identifies the minimum lockbox version that must be installed on the client before a use license can be granted.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '3df53049-9cfb-4b22-a696-f22e74240e00'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ExcludedLockbox object
---

# ExcludedLockbox object

The **ExcludedLockbox** object identifies the minimum lockbox version that must be installed on the client before a use license can be granted. When you enable this feature and specify a minimum version, clients that are using a version of the lockbox that precedes the specified version cannot acquire rights account certificates or use licenses. You can retrieve this object by calling the [**Lockbox**](exclusionpolicy-lockbox-property.md) property on the [**ExclusionPolicy**](exclusionpolicy-object.md) object.

## Members

The **ExcludedLockbox** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExcludedLockbox** object has these properties.



| Property                                                                                   | Description                                                                                                                          |
|:-------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**Enabled**](excludedlockbox-enabled-property.md)<br/>                             | Specifies or retrieves a Boolean value that indicates whether lockbox exclusion is enabled.<br/>                               |
| [**LockboxMinimumVersion**](excludedlockbox-lockboxminimumversion-property.md)<br/> | Specifies or retrieves the minimum lockbox version that must be installed before licenses and certificates can be issued.<br/> |



 

## Examples


```VB
DIM config_manager
DIM admin_role

' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()
    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

END SUB

' *******************************************************************
' Exclude lockboxes.

SUB ExcludeLockbox()

  DIM exclusionPolicy
  DIM lockbox
  DIM minVersion

  ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Retrieve the ExcludedLockbox object.
  SET lockbox = exclusionPolicy.Lockbox
  CheckError()

  IF IsObject(lockbox) <> TRUE THEN
    CALL RaiseError(-870, "Failed to retrieve ExcludedLockbox")
  END IF

  ' Enable lockbox exclusion.
  lockbox.Enabled = TRUE
  CheckError()

  ' Create a Version object.
  SET minVersion = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.Version")

  ' Set the minimum version to 5.0.0.0.
  minVersion.Major = 5
  minVersion.Minor = 0
  minVersion.Build = 0
  minVersion.Revision = 0

  lockbox.LockboxMinimumVersion = minVersion

END SUB

' *******************************************************************
' Error checking function.

FUNCTION CheckError()
  CheckError = Err.number
  IF Err.number <> 0 THEN
    CALL WScript.Echo( vbTab & "*****Error Number: " _
                       & Err.number _
                       & " Desc:" _
                       & Err.Description _
                       & "*****")
    WScript.StdErr.Write(Err.Description)
    WScript.Quit( Err.number )
  END IF
END FUNCTION

' *******************************************************************
' Generate a runtime error.

SUB RaiseError(errId, desc)
  CALL Err.Raise( errId, "", desc )
  CheckError()
END SUB
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




