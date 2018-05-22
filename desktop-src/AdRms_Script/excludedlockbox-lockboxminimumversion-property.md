---
Description: 'Specifies or retrieves the minimum lockbox version that must be installed before licenses and certificates can be issued.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '816585cc-24a6-4090-a1e3-f2457f6d35fe'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ExcludedLockbox.LockboxMinimumVersion property'
---

# ExcludedLockbox.LockboxMinimumVersion property

The **LockboxMinimumVersion** property specifies or retrieves the minimum lockbox version that must be installed before licenses and certificates can be issued.

## Syntax


```VB
ExcludedLockbox.LockboxMinimumVersion
```



## Property value

This property specifies and returns a [**Version**](version-object.md) object.

## Remarks

Lockbox exclusion prohibits AD RMS from issuing an end-user license, certificate, or client licensor certificate if the minimum version of the lockbox installed on the client is less than the version specified and lockbox exclusion has been enabled.

Exclusion must be enabled before this property can be set or retrieved. For more information, see [**Enabled**](excludedlockbox-enabled-property.md).

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

[**ExcludedLockbox**](excludedlockbox-object.md)
</dt> </dl>

 

 




