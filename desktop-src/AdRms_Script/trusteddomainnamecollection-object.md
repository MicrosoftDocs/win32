---
Description: 'Contains a collection of the email domain names that can be trusted from a TrustedUserDomain object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '8434cb44-ca09-4225-81bd-eabebcccb9ae'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: TrustedDomainNameCollection object
---

# TrustedDomainNameCollection object

The **TrustedDomainNameCollection** object contains a collection of the email domain names that can be trusted from a [**TrustedUserDomain**](trusteduserdomain-object.md) object. Each element in the collection is a string. You can retrieve the collection by calling the [**DomainNames**](trusteduserdomain-domainnames-property.md) property on the [**TrustedUserDomain**](trusteduserdomain-object.md) object.

## Members

The **TrustedDomainNameCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TrustedDomainNameCollection** object has these methods.



| Method                                                      | Description                                                                                                                                                          |
|:------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)       | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)     | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)  | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)    | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)   | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)    | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)    | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)  | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |
| [**Update**](trusteddomainnamecollection-update-method.md) | Updates the collection on the server.<br/>                                                                                                                     |



 

### Properties

The **TrustedDomainNameCollection** object has these properties.



| Property                                                           | Description                                                                                                                                            |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/> | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>  | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

## Remarks

To trust all email domains in a user domain, call the [Add](http://go.microsoft.com/fwlink/p/?linkid=87269) method and supply an asterisk (\*) between double quotes.

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
  ' and retrieve a trusted user domain object
  SET Tud = tudColl.Import( "ServerLicensorCert", _
                            "c:\certFile.bin", _
                            False)
  CheckError()

  IF tudColl.Count < 1 OR IsNull(Tud.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  CALL WScript.Echo("Trusted user domain information: ")
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
                    Tud.IsSecurityIdentifiersAllowed)
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

 

 




