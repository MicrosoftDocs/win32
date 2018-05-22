---
Description: 'Represents a trusted user domain associated with an AD RMS installation in a different Active Directory forest.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'd445cb49-65b5-47e8-8776-46ebb0c37972'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: TrustedUserDomain object
---

# TrustedUserDomain object

The **TrustedUserDomain** object represents a trusted user domain associated with an AD RMS installation in a different Active Directory forest. A collection of trusted domains enables AD RMS to process license requests from users whose rights account certificates were issued by AD RMS installations in other forests. To import the external domains associated with another AD RMS installation, you can call the [**Import**](trusteduserdomaincollection-import-method.md) method on the [**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md) object and specify the external server licensor certificate. You can retrieve the collection by calling the [**TrustedUserDomains**](trustpolicy-trusteduserdomains-property.md) property on the [**TrustPolicy**](trustpolicy-object.md) object.

## Members

The **TrustedUserDomain** object has these types of members:

-   [Properties](#properties)

### Properties

The **TrustedUserDomain** object has these properties.



| Property                                                                                                   | Description                                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertificateExpirationTime**](trusteduserdomain-certificateexpirationtime-property.md)<br/>       | Retrieves the time at which the server licensor certificate associated with the trusted domain expires.<br/>                                     |
| [**DisplayName**](trusteduserdomain-displayname-property.md)<br/>                                   | Retrieves a display name for the trusted domain.<br/>                                                                                            |
| [**DomainNames**](trusteduserdomain-domainnames-property.md)<br/>                                   | Retrieves a collection of trusted email domain names for this trusted user domain.<br/>                                                          |
| [**Id**](trusteduserdomain-id-property.md)<br/>                                                     | Retrieves a unique ID for the trusted domain object.<br/>                                                                                        |
| [**IsADFederationSvcTrusted**](trusteduserdomain-isadfederationsvctrusted-property.md)<br/>         | Specifies or retrieves a Boolean value that indicates whether the federated users included in an imported user domain are trusted.<br/>          |
| [**IsImported**](trusteduserdomain-isimported-property.md)<br/>                                     | Retrieves a Boolean value that specifies whether the trusted domain has been imported from another AD RMS installation.<br/>                     |
| [**IsSecurityIdentifiersAllowed**](trusteduserdomain-issecurityidentifiersallowed-property.md)<br/> | Specifies or retrieves a Boolean value that indicates whether the security identifiers associated with the trusted domain are also trusted.<br/> |



 

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
' Retrieve trusted user domain information.

SUB GetTudInfo()

  DIM trustPolicy
  DIM tudColl
  DIM Tud
  DIM domainNames
  DIM Index

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted user domain collection object.
  SET tudColl = trustPolicy.TrustedUserDomains
  CheckError()

  ' Import a server licensor certificate into the collection
  ' and retrieve a trusted user domain object.
  SET Tud = tudColl.Import( "TUD_Name", _
                            "c:\certFile.bin", _
                            False)
  CheckError()

  IF tudColl.Count < 1 OR IsNull(Tud.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  CALL WScript.Echo("Trusted user domain information: ");
  CALL WScript.Echo("Name = " & _
                    Tud.DisplayName)
  CALL WScript.Echo("Expiration = " & _
                    Tud.CertificateExpirationTime)
  CALL WScript.Echo("ID = " & _
                    Tud.Id)
  CALL WScript.Echo("ADFS trusted = " & _
                    Tud.IsADFederationSvcTrusted)
  CALL WScript.Echo("Imported = " & _
                    Tud.IsImported)
  CALL WScript.Echo("SIDs allowed = " & _
                    Tud.IsSecurityIdentifiersAllowed
  CALL WScript.Echo("Trusted domain names:")

  SET domainNames = Tud.DomainNames
  For Index = 0 To domainNames.Count - 1
    CALL WScript.Echo("Domain Name = " & domainNames.Item(Index))
  Next

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
</dt> </dl>

 

 




