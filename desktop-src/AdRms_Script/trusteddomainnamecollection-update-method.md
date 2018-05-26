---
Description: Updates the collection on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8a7c0754-8fa5-44fb-91bf-b1a0679c56ca
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedDomainNameCollectionUpdate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustedDomainNameCollection::Update method

The **Update** method updates the collection on the server.

## Syntax


```VB
Sub Update()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method updates the collection on the server with your changes while preserving the changes made by others.

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

  ' Retrieve the TrustedDomainNameCollection.
  SET domainNames = Tud.DomainNames

  ' Add new email domains.
  CALL domainNames.Add("domain1.com")
  CALL domainNames.Add("domain2.com")
  CheckError()

  ' Update the collection on the server.
  domainNames.Update()
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

[**TrustedDomainNameCollection**](trusteddomainnamecollection-object.md)
</dt> </dl>

 

 




