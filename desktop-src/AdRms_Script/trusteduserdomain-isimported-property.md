---
Description: 'Retrieves a Boolean value that specifies whether the trusted domain has been imported from another AD RMS installation.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '52befe53-0ad3-4d8a-9efb-d0bfff6bf111'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'TrustedUserDomain.IsImported property'
---

# TrustedUserDomain.IsImported property

The **IsImported** property retrieves a Boolean value that specifies whether the trusted domain has been imported from another AD RMS installation.

This property is read-only.

## Syntax


```VB
TrustedUserDomain.IsImported
```



## Property value

This property returns a Boolean value. **True** specifies that the trusted domain is imported from another AD RMS installation. **False** specifies that the domain represents the current AD RMS server.

## Remarks

For more information, see the [**Import**](trusteduserdomaincollection-import-method.md) method on the [**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md) object.

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

[**TrustedUserDomain**](trusteduserdomain-object.md)
</dt> </dl>

 

 




