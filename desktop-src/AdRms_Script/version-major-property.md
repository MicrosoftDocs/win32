---
Description: 'Specifies or retrieves the major version number.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'e7c6911b-7661-4e8b-9c85-866afd474719'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Version.Major property'
---

# Version.Major property

The **Major** property specifies or retrieves the major version number.

## Syntax


```VB
Version.Major
```



## Property value

This property specifies or returns an integer value.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Build**](version-build-property.md)
</dt> <dt>

[**ExcludedApplication**](excludedapplication-object.md)
</dt> <dt>

[**ExcludedLockbox**](excludedlockbox-object.md)
</dt> <dt>

[**Minor**](version-minor-property.md)
</dt> <dt>

[**Revision**](version-revision-property.md)
</dt> <dt>

[**Version**](version-object.md)
</dt> </dl>

 

 




