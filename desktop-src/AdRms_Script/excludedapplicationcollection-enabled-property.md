---
Description: Specifies or retrieves a Boolean value that indicates whether the collection is enabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 88cb1795-08ed-4616-b853-90823c94ec86
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedApplicationCollection.Enabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExcludedApplicationCollection.Enabled property

The **Enabled** property specifies or retrieves a Boolean value that indicates whether the collection is enabled. The collection must be enabled before you can add items to it or retrieve information from it.

## Syntax


```VB
ExcludedApplicationCollection.Enabled
```



## Property value

This property specifies or returns a Boolean value. If this value is **False**, no item in the collection will be excluded.

## Remarks

If this property is **True**, the server issues an end-user license that includes a list of excluded applications. If an application that is on the list attempts to bind to the license, binding will fail.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExcludedApplication**](excludedapplication-object.md)
</dt> <dt>

[**ExcludedApplicationCollection**](excludedapplicationcollection-object.md)
</dt> </dl>

 

 




