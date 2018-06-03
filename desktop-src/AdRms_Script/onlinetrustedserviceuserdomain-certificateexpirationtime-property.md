---
Description: Retrieves the date and time at which the Windows Live ID certificate expires.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 064640a4-6ba7-4b60-a2e2-23624b0e9a0a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineTrustedServiceUserDomain.CertificateExpirationTime property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnlineTrustedServiceUserDomain.CertificateExpirationTime property

The **CertificateExpirationTime** property retrieves the date and time at which the Windows Live ID certificate expires.

This property is read-only.

## Syntax


```VB
OnlineTrustedServiceUserDomain.CertificateExpirationTime
```



## Property value

This property returns a **Variant** subtype **Date**.

## Remarks

This property value is available only after the [**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md) object has been enabled. For more information, see [**Enabled**](onlinetrustedserviceuserdomain-enabled-property.md).

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

[**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)
</dt> </dl>

 

 




