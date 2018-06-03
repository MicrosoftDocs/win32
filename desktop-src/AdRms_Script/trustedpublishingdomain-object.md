---
Description: Contains information about a trusted publishing domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e17ad56b-ad4d-47a0-a53b-d21fec12413f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedPublishingDomain object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TrustedPublishingDomain object

The **TrustedPublishingDomain** object contains information about a trusted publishing domain. This includes information about AD RMS servers that reside in a domain that has a different root of trust than the server currently being administered. By default, an AD RMS server can issue end-user licenses only for content published by itself or by another RMS server in the same cluster. To issue end-user licenses for content published on a server under a different root of trust, the following items must be imported:

-   The server licensor certificate
-   The private key used to sign end-user licenses
-   All rights policy templates

These items are saved in a password-protected file. The file and the password are then securely shared to the current AD RMS server. The imported data is referred to as a trusted publishing domain. For more information, see the [**Import**](trustedpublishingdomaincollection-import-method.md) method on the [**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md) object.

## Members

The **TrustedPublishingDomain** object has these types of members:

-   [Properties](#properties)

### Properties

The **TrustedPublishingDomain** object has these properties.



| Property                                                                                   | Description                                                                                                                        |
|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**CryptoSvcProvider**](trustedpublishingdomain-cryptosvcprovider-property.md)<br/> | Retrieves the name of the cryptographic service provider (CSP) for the trusted domain.<br/>                                  |
| [**DisplayName**](trustedpublishingdomain-displayname-property.md)<br/>             | Retrieves the display name for the trusted domain object.<br/>                                                               |
| [**Id**](trustedpublishingdomain-id-property.md)<br/>                               | Retrieves a unique ID for the trusted domain object.<br/>                                                                    |
| [**IsImported**](trustedpublishingdomain-isimported-property.md)<br/>               | Retrieves a Boolean value that specifies whether the trusted domain has been imported from another AD RMS installation.<br/> |
| [**KeyContainer**](trustedpublishingdomain-keycontainer-property.md)<br/>           | Retrieves the name of the key container in the CSP.<br/>                                                                     |



 

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
' Retrieve trusted publishing domain information.

SUB GetTPDInfo()

  DIM trustPolicy
  DIM TPDs
  DIM TPD
  DIM Index

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted publishing domain collection object.
  SET TPDs = trustPolicy.TrustedPublishingDomains
  CheckError()

  ' Import a trusted publishing domain into the collection.
  SET TPD = TPDs.Import( "TPD_Name", _
                         "password", _
                         "c:\TPDfile.dat")
  CheckError()

  IF TPDs.Count < 1 OR IsNull(TPD.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  CALL WScript.Echo("Trusted publishing domain information: ")
  CALL WScript.Echo("Display name = " & _
                    TPD.DisplayName)
  CALL WScript.Echo("Unique ID = " & _
                    TPD.Id)
  CALL WScript.Echo("Imported = " & _
                    TPD.IsImported)
  CALL WScript.Echo("CSP name = " & _
                    TPD.CryptoSvcProvider)
  CALL WScript.Echo("Key container name = " & _
                    TPD.KeyContainer)

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

[**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




