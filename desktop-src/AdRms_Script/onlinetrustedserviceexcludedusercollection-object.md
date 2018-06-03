---
Description: Contains a collection of users excluded from the Windows Live ID user domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f5514bdb-19f3-4c09-a997-3e21f5704819
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineTrustedServiceExcludedUserCollection object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# OnlineTrustedServiceExcludedUserCollection object

The **OnlineTrustedServiceExcludedUserCollection** object contains a collection of users excluded from the Windows Live ID user domain. Each user is identified by a string value in the form *user@example.com*. You can retrieve this object by calling the [**ExcludedUsers**](onlinetrustedserviceuserdomain-excludedusers-property.md) property on the [**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md) object.

## Members

The **OnlineTrustedServiceExcludedUserCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **OnlineTrustedServiceExcludedUserCollection** object has these methods.



| Method                                                                     | Description                                                                                                                                                          |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)                      | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)                    | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)                 | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)                   | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)                  | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)                   | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)                   | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)                 | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |
| [**Update**](onlinetrustedserviceexcludedusercollection-update-method.md) | Updates the collection on the server.<br/>                                                                                                                     |



 

### Properties

The **OnlineTrustedServiceExcludedUserCollection** object has these properties.



| Property                                                           | Description                                                                                                                                            |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/> | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>  | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

## Remarks

To exclude all users in a domain, add only the domain name, in the form *DomainName.com*, to the collection. That is, do not include the user name.

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
' Retrieve Windows Live ID user domain information.

SUB GetLiveIdInfo()

  DIM trustPolicy
  DIM LiveIdDomain

  ' Retrieve the trust policy object. 
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the Windows Live ID user domain object.
  SET LiveIdDomain = trustPolicy.OnlineTrustedServiceUserDomain
  CheckError()

  ' Enable Windows Live ID user domains.
  LiveIdDomain.Enabled = TRUE
  CheckError()

  IF IsNull(LiveIdDomain.Id) OR LEN(LiveIdDomain.Id) = 0 THEN
    CALL RaiseError(-601, "Enable Live ID user domain failed.")
  END IF
  CALL WScript.Echo("OnlineTrustedServiceUserDomain.Enabled: Id = " _
                    & LiveIdDomain.Id _
                    & " Certification Name = " _
                    & LiveIdDomain.CertificationName _
                    & " Certificate Expiration = " _
                    & LiveIdDomain.CertificateExpirationTime)

  ' Add excluded users to the domain.
  LiveIdDomain.ExcludedUsers.Clear()
  LiveIdDomain.ExcludedUsers.Add("LiveId1@example.com")
  LiveIdDomain.ExcludedUsers.Add("LiveId2@example.com")
  LiveIdDomain.ExcludedUsers.Update()
  CheckError()
  CALL WScript.Echo("LiveIdUserDomain: excluded count=" & _
                    LiveIdDomain.ExcludedUsers.Count)
 
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

[**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)
</dt> </dl>

 

 




