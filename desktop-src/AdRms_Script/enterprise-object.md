---
Description: 'Can be used for enterprise administration.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'e699669c-e59b-4454-8723-15b3a3e67d6e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: Enterprise object
---

# Enterprise object

The **Enterprise** object can be used for enterprise administration. You can create this object if the access control list on the AD RMS Administration website supports the Administrator (0x4) role. You can retrieve this object by calling the [**Enterprise**](configurationmanager-enterprise-property.md) property on the [**ConfigurationManager**](configurationmanager-object.md) object. The object enables you to retrieve the following objects:

-   [**EnterpriseDatabase**](enterprisedatabase-object.md)
-   [**ExclusionPolicy**](exclusionpolicy-object.md)
-   [**IssuancePolicy**](issuancepolicy-object.md)
-   [**ProxySettings**](proxysettings-object.md)
-   [**SecurityPolicy**](securitypolicy-object.md)
-   [**ServerLicensorCertificate**](serverlicensorcertificate-object.md)
-   [**ServiceConnectionPoint**](serviceconnectionpoint-object.md)
-   [**ServicePrivateKeyProtectionInformation**](serviceprivatekeyprotectioninformation-object.md)
-   [**TrustPolicy**](trustpolicy-object.md)

## Members

The **Enterprise** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Enterprise** object has these methods.



| Method                                                                                                   | Description                                                                      |
|:---------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**ResetServiceKeyPassword**](enterprise-resetservicekeypassword-method.md)                             | Specifies a password used to encrypt the server licensor private key.<br/> |
| [**UpdateAdminContactEmail**](enterprise-updateadmincontactemail-method.md)                             | Specifies an email contact address.<br/>                                   |
| [**UpdateExtranetCertificationClusterUrl**](enterprise-updateextranetcertificationclusterurl-method.md) | Specifies an extranet URL for the certification cluster.<br/>              |
| [**UpdateExtranetLicensingClusterUrl**](enterprise-updateextranetlicensingclusterurl-method.md)         | Specifies an extranet URL for the certification or licensing cluster.<br/> |
| [**UpdateIntranetLicensingClusterUrl**](enterprise-updateintranetlicensingclusterurl-method.md)         | Specifies an intranet URL for the licensing cluster.<br/>                  |



 

### Properties

The **Enterprise** object has these properties.



| Property                                                                                                                | Description                                                                                                                           |
|:------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**EnterpriseDatabase**](enterprise-enterprisedatabase-property.md)<br/>                                         | Retrieves an object that can be used to manage the configuration, directory services, and logging databases.<br/>               |
| [**ExclusionPolicy**](enterprise-exclusionpolicy-property.md)<br/>                                               | Retrieves an object that can be used to manage server exclusion policies.<br/>                                                  |
| [**IssuancePolicy**](enterprise-issuancepolicy-property.md)<br/>                                                 | Retrieves an object that can be used to specify the amount of time for which rights account certificates (RACs) are valid.<br/> |
| [**ProxySettings**](enterprise-proxysettings-property.md)<br/>                                                   | Retrieves an object that can be used to manage configuration settings of a proxy server.<br/>                                   |
| [**SecurityPolicy**](enterprise-securitypolicy-property.md)<br/>                                                 | Retrieves an object that can be used to decommission a server and to specify a super users group.<br/>                          |
| [**ServerLicensorCertificate**](enterprise-serverlicensorcertificate-property.md)<br/>                           | Retrieves an object that can be used to manage the server licensor certificate.<br/>                                            |
| [**ServiceConnectionPoint**](enterprise-serviceconnectionpoint-property.md)<br/>                                 | Retrieves an object that can be used to manage a service connection point (SCP).<br/>                                           |
| [**ServicePrivateKeyProtectionInformation**](enterprise-serviceprivatekeyprotectioninformation-property.md)<br/> | Retrieves an object that contains information about the server licensor private key.<br/>                                       |
| [**TrustPolicy**](enterprise-trustpolicy-property.md)<br/>                                                       | Retrieves an object that can be used to define the server trust policy.<br/>                                                    |



 

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
' Retrieve the Enterprise object.

SUB GetEnterprise()

  DIM enterprise

  ' Retrieve the Enterprise object.
  SET enterprise = config_manager.Enterprise
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
</dt> </dl>

 

 




