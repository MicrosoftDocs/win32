---
Description: 'Specifies and retrieves a Boolean value that can be used to enable Windows Live ID user domains.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '26d7db23-a7b0-421c-b145-128c509001b9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'OnlineTrustedServiceUserDomain.Enabled property'
---

# OnlineTrustedServiceUserDomain.Enabled property

The **Enabled** property specifies and retrieves a Boolean value that can be used to enable Windows Live ID user domains.

## Syntax


```VB
OnlineTrustedServiceUserDomain.Enabled
```



## Property value

This property is read/write.

## Remarks

The Windows Live ID user domain must be enabled before any of the following properties can be set or retrieved:

-   [**CertificateExpirationTime**](onlinetrustedserviceuserdomain-certificateexpirationtime-property.md)
-   [**CertificationName**](onlinetrustedserviceuserdomain-certificatename-property.md)
-   [**ExcludedUsers**](onlinetrustedserviceuserdomain-excludedusers-property.md)
-   [**Id**](onlinetrustedserviceuserdomain-id-property.md)

Before calling this property, you must specify proxy server settings by using the [**ProxySettings**](proxysettings-object.md) object.

If you enable Windows Live ID user domains, an [**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md) object [**Id**](onlinetrustedserviceuserdomain-id-property.md) property value is generated.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)
</dt> </dl>

 

 




