---
Description: Specifies or retrieves a Boolean value that indicates whether lockbox exclusion is enabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bc47bf36-be09-4acd-a83c-505ea47109cd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedLockbox.Enabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExcludedLockbox.Enabled property

The **Enabled** property specifies or retrieves a Boolean value that indicates whether lockbox exclusion is enabled.

## Syntax


```VB
ExcludedLockbox.Enabled
```



## Property value

This property specifies or returns a Boolean value. If this value is **False**, exclusion is not enabled.

## Remarks

Lockbox exclusion prohibits AD RMS from issuing an end-user license, certificate, or client licensor certificate if the minimum version of the lockbox installed on the client is less than the version specified and lockbox exclusion has been enabled.

Exclusion must be enabled before you can set or retrieve the [**LockboxMinimumVersion**](excludedlockbox-lockboxminimumversion-property.md) property value.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExcludedLockbox**](excludedlockbox-object.md)
</dt> </dl>

 

 




