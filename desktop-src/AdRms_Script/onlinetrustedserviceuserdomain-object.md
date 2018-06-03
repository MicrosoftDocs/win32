---
Description: Can be used to represent Windows Live ID user domains in the trust policy of an enterprise.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6e445049-062e-4820-bab1-b6148521d114
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineTrustedServiceUserDomain object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# OnlineTrustedServiceUserDomain object

The **OnlineTrustedServiceUserDomain** object can be used to represent Windows Live ID user domains in the trust policy of an enterprise. You can enable Windows Live ID domains, retrieve information about them, and identify excluded users. Call the [**OnlineTrustedServiceUserDomain**](trustpolicy-onlinetrustedserviceuserdomain-property.md) property on the [**TrustPolicy**](trustpolicy-object.md) object to retrieve this object.

> [!Note]  
> You must specify proxy server settings by using the [**ProxySettings**](proxysettings-object.md) object before enabling a Windows Live ID domain.

 

## Members

The **OnlineTrustedServiceUserDomain** object has these types of members:

-   [Properties](#properties)

### Properties

The **OnlineTrustedServiceUserDomain** object has these properties.



| Property                                                                                                          | Description                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**CertificateExpirationTime**](onlinetrustedserviceuserdomain-certificateexpirationtime-property.md)<br/> | Retrieves the date and time at which the Windows Live ID certificate expires.<br/>                    |
| [**CertificationName**](onlinetrustedserviceuserdomain-certificatename-property.md)<br/>                   | Retrieves the common name of the Windows Live ID service.<br/>                                        |
| [**Enabled**](onlinetrustedserviceuserdomain-enabled-property.md)<br/>                                     | Specifies and retrieves a Boolean value that can be used to enable Windows Live ID user domains.<br/> |
| [**ExcludedUsers**](onlinetrustedserviceuserdomain-excludedusers-property.md)<br/>                         | Retrieves a collection of excluded Windows Live ID user identities.<br/>                              |
| [**Id**](onlinetrustedserviceuserdomain-id-property.md)<br/>                                               | Retrieves a unique integer ID for the **OnlineTrustedServiceUserDomain** object.<br/>                 |



 

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
</dt> </dl>

 

 




