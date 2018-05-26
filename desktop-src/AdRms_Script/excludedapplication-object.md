---
Description: Represents an application that is prohibited from decrypting RMS-protected content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 42865e1d-5680-411e-b3b4-200e25979eed
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedApplication object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ExcludedApplication object

The **ExcludedApplication** object represents an application that is prohibited from decrypting RMS-protected content. An excluded application cannot obtain a new end-user license by using formerly valid rights account certificates or issuance licenses. You can enable this functionality to make sure that users install a newer, more secure version of an application when one becomes available. RMS-enabled applications are excluded by name and version number.

## Members

The **ExcludedApplication** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExcludedApplication** object has these properties.



| Property                                                                         | Description                                                             |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**AppName**](excludedapplication-appname-property.md)<br/>               | Specifies or retrieves the name of the excluded application.<br/> |
| [**MaximumVersion**](excludedapplication-maximumversion-property.md)<br/> | Specifies or retrieves the maximum version number.<br/>           |
| [**MinimumVersion**](excludedapplication-minimumversion-property.md)<br/> | Specifies or retrieves the minimum version number.<br/>           |



 

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
' Exclude an application

SUB Exclude()

  DIM exclusionPolicy
  DIM excludedAppColl   
  DIM excludedApplication
  DIM minVersion
  DIM maxVersion

  ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Retrieve the collection of exclusion policies.
  Set excludedAppColl = exclusionPolicy.Applications
  CheckError()

  IF IsObject(excludedAppColl) <> TRUE THEN
    CALL RaiseError(-810, "Cannot retrieve exclusion policies.")
  END IF

  ' Exclude Notepad.exe.
  SET excludedApplication = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.ExcludedApplication")
  CheckError()
  SET minVersion = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.Version")
  SET maxVersion = CreateObject(_
    "Microsoft.RightsManagementServices.Admin.Version")
  CheckError()
    
  minVersion.Major = 1
  minVersion.Minor = 1
  minVersion.Build = 1
  minVersion.Revision = 1
  maxVersion.Major = 1
  maxVersion.Minor = 1
  maxVersion.Build = 1
  maxVersion.Revision = 1
  excludedApplication.AppName = "Notepad.exe"
  excludedApplication.MinimumVersion = minVersion
  excludedApplication.MaximumVersion = maxVersion

  ' Add the excluded application to the collection.
  excludedAppColl.Add( excludedApplication )
  CheckError()

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**ExcludedApplicationCollection**](excludedapplicationcollection-object.md)
</dt> </dl>

 

 




