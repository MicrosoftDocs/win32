---
Description: 'Refreshes the collection from the collection saved on the server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'b6993b53-6119-47dc-b884-ca4bd76b313e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ExcludedApplicationCollection.Refresh method'
---

# ExcludedApplicationCollection.Refresh method

The **Refresh** method refreshes the collection from the collection saved on the server.

## Syntax


```VB
ExcludedApplicationCollection.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

All of the items in the current collection object will be overwritten. Use this method to refresh your collection to ensure that you have the latest updates made by other administrators.

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

  ' Enable application exclusion
  excludedAppColl.Enabled = True

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

  ' Add the excluded application to the collection, and update
  ' the collection on the server.
  excludedAppColl.Add( excludedApplication )
  CheckError()

  ' Refresh the collection. This is not needed here, but the call
  ' displays the syntax.
  excludedAppColl.Refresh()
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExcludedApplication**](excludedapplication-object.md)
</dt> <dt>

[**ExcludedApplicationCollection**](excludedapplicationcollection-object.md)
</dt> </dl>

 

 




