---
Description: Can be used to retrieve multiple objects that collectively define the AD RMS trust policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3966a595-c3a6-4d3f-ad27-437d391fb2a3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustPolicy object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TrustPolicy object

The **TrustPolicy** object can be used to retrieve multiple objects that collectively define the AD RMS trust policy. You can use these objects to manage trusted domains, Windows Live ID domains, and the interaction between Active Directory Federation Services (ADFS) and AD RMS. You can retrieve the trust policy object by calling the [**TrustPolicy**](enterprise-trustpolicy-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **TrustPolicy** object has these types of members:

-   [Properties](#properties)

### Properties

The **TrustPolicy** object has these properties.



| Property                                                                                                 | Description                                                             |
|:---------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**ADFederationService**](trustpolicy-adfederationservice-property.md)<br/>                       | Retrieves an object that manages AD RMS use of ADFS.<br/>         |
| [**OnlineTrustedServiceUserDomain**](trustpolicy-onlinetrustedserviceuserdomain-property.md)<br/> | Retrieves a Windows Live ID domain object.<br/>                   |
| [**TrustedPublishingDomains**](trustpolicy-trustedpublishingdomains-property.md)<br/>             | Retrieves a collection of trusted publishing domain objects.<br/> |
| [**TrustedUserDomains**](trustpolicy-trusteduserdomains-property.md)<br/>                         | Retrieves a collection of trusted user domain objects.<br/>       |



 

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
' Retrieve the trust policy object.

SUB GetTrustPolicy()

  DIM trustPolicy

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**ADFederationService**](adfederationservice-object.md)
</dt> <dt>

[**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)
</dt> <dt>

[**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
</dt> <dt>

[**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md)
</dt> </dl>

 

 




