---
Description: Represents a version number in the format Major.Minor.Build.Revision.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 452960bc-2642-4f07-8726-23af66d72ad4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Version object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Version object

The **Version** object represents a version number in the format *Major.Minor.Build.Revision*. Version numbers are used by the [**ExcludedApplication**](excludedapplication-object.md) and [**ExcludedLockbox**](excludedlockbox-object.md) objects.

## Members

The **Version** object has these types of members:

-   [Properties](#properties)

### Properties

The **Version** object has these properties.



| Property                                                 | Description                                                 |
|:---------------------------------------------------------|:------------------------------------------------------------|
| [**Build**](version-build-property.md)<br/>       | Specifies or retrieves the build number.<br/>         |
| [**Major**](version-major-property.md)<br/>       | Specifies or retrieves the major version number.<br/> |
| [**Minor**](version-minor-property.md)<br/>       | Specifies or retrieves the minor version number.<br/> |
| [**Revision**](version-revision-property.md)<br/> | Specifies or retrieves the revision number.<br/>      |



 

## Examples


```VB
' *******************************************************************
' Test version number creation.

SUB TestVersion()
    
  DIM excludedApplication
  DIM minVersion
  DIM maxVersion

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**ExcludedApplication**](excludedapplication-object.md)
</dt> <dt>

[**ExcludedLockbox**](excludedlockbox-object.md)
</dt> </dl>

 

 




