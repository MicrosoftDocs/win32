---
Description: 'Retrieves the minimum lockbox version that must be installed before an end-user license, certificate, or client licensor certificate (CLC) can be granted.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '082be71b-1ad3-4da1-b0ba-0ed23076f74e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ExclusionPolicy.Lockbox property'
---

# ExclusionPolicy.Lockbox property

The **Lockbox** property retrieves the minimum lockbox version that must be installed before an end-user license, certificate, or client licensor certificate (CLC) can be granted.

This property is read-only.

## Syntax


```VB
ExclusionPolicy.Lockbox
```



## Property value

This property returns an [**ExcludedLockbox**](excludedlockbox-object.md) object.

## Remarks

Lockbox exclusion prohibits AD RMS from issuing an end-user license, certificate, or CLC if the minimum version of the lockbox installed on the client is less than the version specified and lockbox exclusion has been enabled.

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
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusionPolicy**](exclusionpolicy-object.md)
</dt> </dl>

 

 




