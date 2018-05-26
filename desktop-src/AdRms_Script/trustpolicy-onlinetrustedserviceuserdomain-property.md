---
Description: Retrieves a Windows Live ID user domain object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 17e24a81-0781-4a1a-973f-278646283710
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustPolicy.OnlineTrustedServiceUserDomain property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustPolicy.OnlineTrustedServiceUserDomain property

The **OnlineTrustedServiceUserDomain** property retrieves a Windows Live ID user domain object.

This property is read-only.

## Syntax


```VB
TrustPolicy.OnlineTrustedServiceUserDomain
```



## Property value

This property returns a [**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md) object.

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

SUB GetLiveIDInfo()

  DIM trustPolicy
  DIM LiveIDDomain

  ' Retrieve the trust policy object. 
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the Windows Live ID user domain object.
  SET LiveIDDomain = trustPolicy.OnlineTrustedServiceUserDomain
  CheckError()

  ' Enable Windows Live ID user domains.
  LiveIDDomain.Enabled = TRUE
  CheckError()

  IF IsNull(LiveIDDomain.Id) OR LEN(LiveIDDomain.Id) = 0 THEN
    CALL RaiseError(-601, "Enable Live ID user domain failed.")
  END IF
  CALL WScript.Echo("LiveID_UserDomain.Enabled: Id = " _
                    & LiveIDDomain.Id _
                    & " Certification Name = " _
                    & LiveIDDomain.CertificationName _
                    & " Certificate Expiration = " _
                    & LiveIDDomain.CertificateExpirationTime)

  ' Add excluded users to the domain.
  LiveIDDomain.ExcludedUsers.Clear()
  LiveIDDomain.ExcludedUsers.Add("liveid1@example.com")
  LiveIDDomain.ExcludedUsers.Add("liveid2@example.com")
  LiveIDDomain.ExcludedUsers.Update()
  CheckError()
  CALL WScript.Echo("LiveID_UserDomain: excluded count=" & _
                    LiveIDDomain.ExcludedUsers.Count)
 
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

[**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




