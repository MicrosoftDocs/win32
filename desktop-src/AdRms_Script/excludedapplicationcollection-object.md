---
Description: 'Contains a collection of ExcludedApplication objects that represent applications prohibited from decrypting RMS-protected content. You can retrieve this collection by calling the Applications property on the ExclusionPolicy object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '9b92040f-918f-4e42-aecb-f14e31729b83'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ExcludedApplicationCollection object
---

# ExcludedApplicationCollection object

The **ExcludedApplicationCollection** object contains a collection of [**ExcludedApplication**](excludedapplication-object.md) objects that represent applications prohibited from decrypting RMS-protected content. You can retrieve this collection by calling the [**Applications**](exclusionpolicy-applications-property.md) property on the [**ExclusionPolicy**](exclusionpolicy-object.md) object.

## Members

The **ExcludedApplicationCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ExcludedApplicationCollection** object has these methods.



| Method                                                              | Description                                                                                                                                                          |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)               | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)             | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)          | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)            | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)           | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)            | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [**Refresh**](trustedpublishingdomaincollection-refresh-method.md) | Refreshes the collection from the collection saved on the server.<br/>                                                                                         |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)            | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)          | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **ExcludedApplicationCollection** object has these properties.



| Property                                                                     | Description                                                                                                                                            |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/>           | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [**Enabled**](excludedapplicationcollection-enabled-property.md)<br/> | Specifies or retrieves a Boolean value that indicates whether the collection is enabled.<br/>                                                    |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>            | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**ExcludedApplication**](excludedapplication-object.md)
</dt> </dl>

 

 




